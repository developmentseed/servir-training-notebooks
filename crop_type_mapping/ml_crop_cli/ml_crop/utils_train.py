import pickle

import lightgbm as lgb
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

from ml_crop.utils_data import train_raw, train_split, crop_classes


def train(model_id, raster_file, train_geo, out_model):
    class_dict = crop_classes(train_geo)
    X_raw, Y_raw = train_raw(raster_file, train_geo)
    X_train, X_test, y_train, y_test, class_weight_dict, labels = train_split(X_raw, Y_raw)
    if model_id == "randomforest":
        model = RandomForestClassifier(
                n_estimators=200,
                class_weight=class_weight_dict,
                max_depth=6,
                n_jobs=-1,
                verbose=1,
                random_state=0)

    elif model_id == "lightgbm":
        model = lgb.LGBMClassifier(
               objective='multiclass',
               class_weight=class_weight_dict,
               num_class=len(class_dict),
               metric='multi_logloss')

    elif model_id == "svm":
        model = svm.SVC(
               class_weight=class_weight_dict,
               gamma='scale',
               decision_function_shape='ovo')
    model.fit(X_train, y_train)
    with open(out_model, 'wb') as modelfile:
        pickle.dump(model, modelfile)
    print("training {} model!".format(model_id))
    preds = model.predict(X_test)
    f1 = f1_score(y_test, preds, average='weighted')
    # cm = confusion_matrix(y_test, preds, labels=labels)
    print("*"*30)
    print("The model f1 score is {:0.2f}".format(f1))
    print("*"*30)
    return model
