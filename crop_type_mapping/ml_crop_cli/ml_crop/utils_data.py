import geopandas as gpd
import numpy as np
import rasterio
from rasterio.features import rasterize
from rasterstats.io import bounds_window

from sklearn.model_selection import train_test_split


def crop_classes(train_geo):
    training_vectors = gpd.read_file(train_geo)
    classes = np.unique(training_vectors.name)
    class_dict = dict(zip(classes, range(len(classes))))
    return class_dict


def all_values(x):
    return x


def train_raw(raster_file, train_geo):
    training_vectors = gpd.read_file(train_geo)
    class_dict = crop_classes(train_geo)
    print(class_dict)
    # set up our training data lists
    # this larger cell reads data from a raster file for each training vector
    x_raw = []
    y_raw = []
    with rasterio.open(raster_file, 'r') as src:
        for (label, geom) in zip(
                                training_vectors.name,
                                training_vectors.geometry):
            # read the raster data matching the geometry bounds
            window = bounds_window(geom.bounds, src.transform)
            # store our window information
            window_affine = src.window_transform(window)
            fsrc = src.read(window=window)
            # rasterize the geometry into the larger shape and affine
            mask = rasterize(
                [(geom, 1)],
                out_shape=fsrc.shape[1:],
                transform=window_affine,
                fill=0,
                dtype='uint8',
                all_touched=True
            ).astype(bool)
            # for each label pixel (places where the mask is true)...
            label_pixels = np.argwhere(mask)
            for (row, col) in label_pixels:
                # add a pixel of data to X
                data = fsrc[:, row, col]
                one_x = np.nan_to_num(data, nan=1e-3)
                x_raw.append(one_x)
                y_raw.append(class_dict[label])

    return x_raw, y_raw


def norm_inds(arr, a, b):
    inds = np.expand_dims((arr[..., a] - arr[..., b]) /
                          (arr[..., a] + arr[..., b]), axis=1)
    return inds


def train_split(X_raw, Y_raw):
    X = np.array(X_raw)
    y = np.array(Y_raw)
    print("training data shape is")
    print(X.shape, y.shape)
    ndvi = norm_inds(X, 3, 2)
    ndwi = norm_inds(X, 1, 3)

    X = np.concatenate([X, ndvi, ndwi], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    labels, counts = np.unique(y_train, return_counts=True)
    class_weight_dict = dict(zip(labels, 1/counts))

    return X_train, X_test, y_train, y_test, class_weight_dict, labels
