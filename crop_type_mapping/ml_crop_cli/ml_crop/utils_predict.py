import numpy as np
from sklearn.ensemble import RandomForestClassifier
# from treeinterpreter import treeinterpreter as ti
from sklearn.metrics import confusion_matrix
from ml_crop.utils_data import train_raw, train_split, crop_classes, norm_inds
from ml_crop.utils_train import train
import rasterio
import lightgbm as lgb

from sklearn import svm

import pickle

def predict(model_id, raster_file,train_geo, bands, pred_tiff):
    model = train(model_id, raster_file, train_geo, bands)
    output_image = "{}_classification.tif".format(model_id)
    src = rasterio.open(pred_tiff, 'r')
    profile = src.profile
    profile.update(
        dtype=rasterio.uint8,
        count=1,
    )
    dst = rasterio.open(output_image, 'w', **profile)

    # perform prediction on each small image patch to minimize required memory
    patch_size = 500

    for i in range((src.shape[0] // patch_size) + 1):
        for j in range((src.shape[1] // patch_size) + 1):
            # define the pixels to read (and write)
            window = rasterio.windows.Window(
                j * patch_size,
                i * patch_size,
                # don't read past the image bounds
                min(patch_size, src.shape[1] - j * patch_size),
                min(patch_size, src.shape[0] - i * patch_size)
            )

            data = src.read(window=window)
            # read the image into the proper format, adding indices if necessary
            img_swp = np.moveaxis(data, 0, 2)
            img_flat = img_swp.reshape(-1, img_swp.shape[-1])

            img_ndvi = norm_inds(img_flat, 3, 2)
            img_ndwi = norm_inds(img_flat, 1, 3)

            img_w_ind = np.concatenate([img_flat, img_ndvi, img_ndwi], axis=1)

            # remove no data values, store the indices for later use
            # a later cell makes the assumption that all bands have identical no-data value arrangements
            m = np.ma.masked_invalid(img_w_ind)
            to_predict = img_w_ind[~m.mask].reshape(-1, img_w_ind.shape[-1])

            # predict
            if not len(to_predict):
                continue
            img_preds = model.predict(to_predict)

            # add the prediction back to the valid pixels (using only the first band of the mask to decide on validity)
            # resize to the original image dimensions
            output = np.zeros(img_flat.shape[0])
            output[~m.mask[:,0]] = img_preds.flatten()
            output = output.reshape(*img_swp.shape[:-1])

            # create our final mask
            mask = (~m.mask[:,0]).reshape(*img_swp.shape[:-1])

            # write to the final file
            dst.write(output.astype(rasterio.uint8), 1, window=window)
            dst.write_mask(mask, window=window)
            # write to the final file
            dst.write(output.astype(rasterio.uint8), 1, window=window)
            dst.write_mask(mask, window=window)

    src.close()
    dst.close()
