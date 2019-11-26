# Crop Type Mapping with Satellite Machine Learning
Crop type mapping machine learning scripts and documentation have been divided into three sections:

- **The first section** contains the [Jupyter Notebook](/notebooks) that we created to run crop type mapping with Sentinel-2 on Google Colab. Users can run independent notebook in local machine (Window, Linux or Mac OS), Google Colab, AWS EC2 or other cloud providers.

- **The second section** is a stand-alone python command-line tool, called [`ml_crop` ](/ml_crop_cli)that the users can pip install, parse the parameters to run the models. Please see the following section for the installation instruction.

For more details about these three sections, please read through the following contents.


## Crop type mapping ML models in notebooks
We prepared three machine learning models for crop type mapping, and you can find the notebook for RandomForstClassifier under [this GitHub repo](/notebooks/). If you are interested in running `LightGBM` and  `SVM` notebooks on the Google Colab, please find the following links.

- Notebook 1: `LightGBM.ipynb`. You can find the Google Colab notebook we hosted online directly through this [link](https://colab.research.google.com/drive/1wcz5PRDmM3MvSccqgb5WXpWmVuGB2jYh).

- Notebook 3: `SVM_crop_type.ipynb`. You can find the Google Colab notebook we hosted online directly through this [link](https://colab.research.google.com/drive/1Q1Wki8m4iL8q1hU3S4rr83c8V0dPTMLl).


## Python CLI tool for crop type mapping

You can pip install the packaged command-line tool, pass your training dataset to the package.
To do so, you can go through these steps:

- Step 1: `git clone https://github.com/developmentseed/servir-training-notebooks.git `;

- Step 2: `cd crop_type_mapping/ml_crop_cli`;

- Step 3: under the directory 'ml_crop_cli', run `pip install -e .` to install the python package called `ml_crop`;

- Step 4: train and predict model with your sentinel-2 image and associated crop type training dataset.

To `train` a randomforest model you can run command line:

```
ml_crop train --model_id=randomforest  --raster_file=../training_data/Trans_nzoia_2019_05-02.tif  --train_geo=../training_data/training_data.geojson --out_model=model.sav
```

To make prediction with `predict`, you can run:

```
ml_crop predict --out_model="model.sav" --pred_tiff=../training_data/Trans_nzoia_2019_05-02.tif --output_image=classification.tif
```

We have three machine learning models built-in the command-line tool. Besides, `randomforest`, you can also call `lightgbm` and `svm`. Simply, replace `--model_id=randomforest` with `--model_id=lightgbm` or `--model_id=svm` in for the `ml_crop train`.
