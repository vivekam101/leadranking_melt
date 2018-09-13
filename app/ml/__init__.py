from app.data.loader import load_from_file, load_object
from app.ml.metrics import get_accuracy, get_probablity
from sklearn.preprocessing import LabelEncoder
import pickle
import numpy as np
import pandas as pd

def leadranking_preprocess(config,lead):
    _category_cols = config.get('category_cols')

    print("Loading data... ")
    _df = load_object(lead)
    print("Data Loaded... ")
    print(_df.head())
    print("Shape: ", _df.shape)
    print('Original df \n')
    print(_df)

    _df['LeadCategory'] =_df['LeadCategory'].str.lower()
    _df['LeadSubCategory'] = _df['LeadSubCategory'].str.lower()
    _df['LeadSource'] = _df['LeadSource'].str.lower()

    if (_category_cols):
        print("Encoding data")
        print(_category_cols)
        for _col, _classes in _category_cols.items():
            encoder = LabelEncoder()
            encoder.classes_ = _classes
            _df[_col] = encoder.transform(_df[_col])
    _df["Is_mobileno_given"] = ~_df["Mobile"].isnull()
    _df["Is_telephoneno_given"] = ~_df["Telephone"].isnull()
    _df["DND_Count"] = _df[["donotemail", "donotfax", "donotphone"]].apply(lambda x: sum(
        [1 if x["donotfax"] == True else 0, 1 if x["donotphone"] == True else 0, 1 if x["donotemail"] == True else 0]),
                                                                           axis=1)
    _df["Is_pref_start_date_given"] = ~_df["po_prefered_start_date1"].isnull()

    _selected_fields = ['LeadCategory', 'LeadSource',\
                        'LeadSubCategory', 'Is_mobileno_given', 'DND_Count',\
                        ]
    _df = _df[_selected_fields]
    print('Transformed df \n')
    print(_df)

    _score, _cls = _predict_class(config, lead, _df)
    return _score, _cls

def melt_preprocess(config,lead):
    _category_cols = config.get('category_cols')

    print("Loading data... ")
    _df = load_object(lead)
    print("Data Loaded... ")
    print(_df.head())
    print("Shape: ", _df.shape)
    print('Original df \n')
    print(_df)

    _df['experience_level'] =_df['experience_level'].str.lower()
    _df['batch_code'] = _df['batch_code'].str.lower()
    _df['mentor'] = _df['mentor'].str.lower()

    if (_category_cols):
        print("Encoding data")
        print(_category_cols)
        for _col, _classes in _category_cols.items():
            encoder = LabelEncoder()
            encoder.classes_ = _classes
            _df[_col] = encoder.transform(_df[_col])
    _selected_fields = ['experience_level','batch_code','mentor'
                        ]
    _df = _df[_selected_fields]
    print('Transformed df \n')
    print(_df)
    _score, _cls = _predict_class(config, lead, _df)
    return _score, _cls


def _predict_class(config, lead, _df):
    _true_status = config.get("true_status")
    _model = load_from_file(config.get("model_dump_file_path"))
    print('Predicting the score...')
    _cls , _probability = get_probablity(_model, _df.iloc[:,:].values, _true_status) #iloc to skip first column which has id
    print(_cls, _probability)
    _score = round(_probability*100, 2)

    return _score, _cls


