# Python CLI tool for crop type mapping

You can pip install the packaged command-line tool, pass your training dataset to the package.
To do so, you can go through these steps:

- Step 1: `git clone https://github.com/developmentseed/servir-training-notebooks.git`;

- Step 2: `cd crop_type_mapping/ml_crop_cli`;

- Step 3: under the directory 'ml_crop_cli', run `pip install -e .` to install the python package called `ml_crop`;

- Step 4: train and predict model with your sentinel-2 image and associated crop type training dataset.

To `train` the model you can run command line:

```
ml_crop train --model_id=randomforest  --raster_file=../training_data/Trans_nzoia_2019_05-02.tif  --train_geo=../training_data/training_data.geojson --out_model=model.sav
```

To make prediction with `predict`, you can run:

```
ml_crop predict --out_model="model.sav" --pred_tiff=../training_data/Trans_nzoia_2019_05-02.tif --output_image=classification.tif
```

We have three machine learning models built-in the command-line tool. Besides, `randomforest`, you can also call `lightgbm` and `svm`. Simply, replace `--model_id=randomforest` with `--model_id=lightgbm` or `--model_id=svm` in the train and predict.

Note: svm model is about 20 times slower than lightgbm model for training when apply to the same training dataset.
