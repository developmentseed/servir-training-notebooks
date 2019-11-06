# import numpy as np
from sklearn.ensemble import RandomForestClassifier
# from treeinterpreter import treeinterpreter as ti
from sklearn.metrics import confusion_matrix
from ml_crop.utils_data import train_raw, train_split, crop_classes

import lightgbm as lgb

from sklearn import svm

import pickle

def train(model_id, raster_file, train_geo, bands):
    class_dict = crop_classes(train_geo)
    X_raw, Y_raw = train_raw(raster_file, train_geo, bands)
    X_train, X_test, y_train, y_test, class_weight_dict, labels = train_split(X_raw, Y_raw)
    if model_id =="randomforest":
        model = RandomForestClassifier(
                n_estimators=200,
                class_weight=class_weight_dict,
                max_depth=6,
                n_jobs=-1,
                verbose=1,
                random_state=0)

    elif model_id =="lightgbm":
        model = lgb.LGBMClassifier(
               objective='multiclass',
               class_weight = class_weight_dict,
               num_class = len(class_dict),
               metric = 'multi_logloss')

    elif model_id == "svm":
        model = svm.SVC(
               class_weight = class_weight_dict,
               gamma='scale',
               decision_function_shape='ovo')
    model.fit(X_train, y_train)
    print("training {} model!".format(model_id))
    preds = model.predict(X_test)
    cm = confusion_matrix(y_test, preds, labels=labels)
    print("model confusion_matrix is {}".format(cm))
    print(cm)
    return model
