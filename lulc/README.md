# Land use and cover (LULC) mapping with Fastai

It's a deep learning workflow that utilize [fastai](https://github.com/fastai/fastai) dynamics UNet to train LULC model in Slovenia.
In the [lulc notebook](/LULC_with_fastai_Servir_2019.ipynb), we  build the workflow that walk trainees into three steps:

Step 1. Training data generation from multiple GeoTiffs we prepared using eo-learn package.

Step 2. Training model on the cloud with fast.ai dynamic Unet; Trainees can run the notebook on any cloud provider's GPU machines or run the exact notebook on [Google Colab](https://colab.research.google.com/drive/10Eup8QtXl1OzqjuuaduRHeFwOKQPkuX0).

Step 3. Prediction and model inference over an unseen area.
