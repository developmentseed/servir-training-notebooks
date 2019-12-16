# Land Use and Land Cover (LULC) mapping with fastai

This folder demonstrates a deep learning workflow that uses the [`fastai`](https://github.com/fastai/fastai) dynamic U-Net to train a LULC model in Slovenia. In the [Jupyter notebook](/LULC_with_fastai_Servir_2019.ipynb), we build the workflow that walks trainees through three steps:
  1. Training data generation from multiple GeoTiffs we prepared using the [`eo-learn`](https://github.com/sentinel-hub/eo-learn) package.
  2. Training model on the cloud with `fastai` dynamic U-Net; Trainees can run the notebook on any cloud provider's GPU machines or run the exact notebook on [Google Colab](https://colab.research.google.com/drive/10Eup8QtXl1OzqjuuaduRHeFwOKQPkuX0).
  3. Prediction and model inference over an unseen area.
