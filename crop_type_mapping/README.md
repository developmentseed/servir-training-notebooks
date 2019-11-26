# Crop Type Mapping with Satellite Machine Learning
Crop type mapping machine learning scripts and documentation have been divided into three sections:

<<<<<<< HEAD
- **The first section** contains the [Jupyter Notebook](/notebooks) that we created to run crop type mapping with Sentinel-2 on Google Colab. Users can run independent notebook in local machine (Window, Linux or Mac OS), Google Colab, AWS EC2 or other cloud providers.

- **The second section** is a stand-alone python command-line tool, called [`ml_crop` ](/ml_crop_cli)that the users can pip install, parse the parameters to run the models. Please see the following section for the installation instruction.

For more details about these three sections, please read through the following contents.


## Crop type mapping ML models in notebooks
We prepared three machine learning models for crop type mapping, and you can find the notebook for RandomForstClassifier under [this GitHub repo](/notebooks/). If you are interested in running `LightGBM` and  `SVM` notebooks on the Google Colab, please find the following links.

- Notebook 1: `LightGBM.ipynb`. You can find the Google Colab notebook we hosted online directly through this [link](https://colab.research.google.com/drive/1wcz5PRDmM3MvSccqgb5WXpWmVuGB2jYh).

=======
- **The first section** is about how to create training dataset generation for the coming pixel-wise crop type mapping with machine learnings.

- **The second section** contains the Jupyter Notebooks that we created to run crop type mapping with Sentinel-2 on Google Colab. Users can run independent notebook in local machine (Window, Linux or Mac OS), Google Colab, AWS EC2 or other cloud providers.

- **The third section** is a stand-alone python command-line tool, called `ml_crop` that the users can pip install, parse the parameters to run the models. Please see the following section for the installation instruction.

For more details about these three sections, please read through the following contents.

## Training dataset generation
A high-quality training dataset produces a good machine learning model output. We have the training dataset to run this workshop saved on Google Drive ([link](https://drive.google.com/drive/folders/1jM2mBsJ81QfmyaKZNeXSTyi_IOVr_3Vs?usp=sharing)). Two datasets are in the google drive folder named "servir_croptype_workshop_data":

- `training_data.geojson` is the land use and cover polygons;

- `Trans_nzoia_2019_05-02.tif` is the Sentinel-2 image that has 6 bands from B, G, R, Red edge, NIR, SWIR1, SWIR2.


## Crop type mapping ML models in notebooks

Three notebooks under the GitHub repo `crop_type_mapping/notebooks`.

- Notebook 1: `LightGBM.ipynb`. You can find the Google Colab notebook we hosted online directly through this [link](https://colab.research.google.com/drive/1wcz5PRDmM3MvSccqgb5WXpWmVuGB2jYh).

- Notebook 2: `randomforest.ipynb`. You can find the Google Colab notebook we hosted online directly through this [link](https://colab.research.google.com/drive/1NIuDieA5ep45hFboJFbaI3Lg6iZX5GFG).

>>>>>>> b74b3ee31dcad682359d4d1c628c348eed0c947a
- Notebook 3: `SVM_crop_type.ipynb`. You can find the Google Colab notebook we hosted online directly through this [link](https://colab.research.google.com/drive/1Q1Wki8m4iL8q1hU3S4rr83c8V0dPTMLl).


## Python CLI tool for crop type mapping

You can pip install the packaged command-line tool, pass your training dataset to the package.
To do so, you can go through these steps:

<<<<<<< HEAD
- Step 1: `git clone https://github.com/developmentseed/servir-training-notebooks.git `;
=======
- Step 1: `git clone:xxx `;
>>>>>>> b74b3ee31dcad682359d4d1c628c348eed0c947a

- Step 2: `cd crop_type_mapping/ml_crop_cli`;

- Step 3: under the directory 'ml_crop_cli', run `pip install -e .` to install the python package called `ml_crop`;

- Step 4: train and predict model with your sentinel-2 image and associated crop type training dataset.

<<<<<<< HEAD
To `train` a randomforest model you can run command line:

```
ml_crop train --model_id=randomforest  --raster_file=../training_data/Trans_nzoia_2019_05-02.tif  --train_geo=../training_data/training_data.geojson --out_model=model.sav
=======
To `train` the model you can run command line:

```
ml_crop train --model_id=randomforest  --raster_file=../training_data/Trans_nzoia_2019_05-02.tif  --train_geo=../training_data/training_data.geojson --bands=6
>>>>>>> b74b3ee31dcad682359d4d1c628c348eed0c947a
```

To make prediction with `predict`, you can run:

```
<<<<<<< HEAD
ml_crop predict --out_model="model.sav" --pred_tiff=../training_data/Trans_nzoia_2019_05-02.tif --output_image=classification.tif
```

We have three machine learning models built-in the command-line tool. Besides, `randomforest`, you can also call `lightgbm` and `svm`. Simply, replace `--model_id=randomforest` with `--model_id=lightgbm` or `--model_id=svm` in for the `ml_crop train`.
=======
ml_crop predict --model_id=randomforest  --raster_file=../training_data/Trans_nzoia_2019_05-02.tif  --train_geo=../training_data/training_data.geojson --bands=6 --pred_tiff=../training_data/Trans_nzoia_2019_05-02.tif
```

We have three machine learning models built-in the command-line tool. Besides, `randomforest`, you can also call `lightgbm` and `svm`. Simply, replace `--model_id=randomforest` with `--model_id=lightgbm` or `--model_id=svm` in the train and predict.
>>>>>>> b74b3ee31dcad682359d4d1c628c348eed0c947a
