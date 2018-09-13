from app.ml import  leadranking_preprocess,melt_preprocess
from app import config
import random

def lead_ranking_predict(lead_data):
    _config = config.LEAD_RANKING_API_CONFIG
    _lead_data = lead_data

    _map = _config.get("data_map")
    if _map:
        print("mapping")
        _lead_data = _map(_lead_data)

    print("Mapped Data from config -----\n")
    print(_lead_data)

    # classification problem
    
    _prob, _cls = leadranking_preprocess(_config, _lead_data)
    _id = _lead_data.get("_id")
    return _prob, _cls, _id


def melt_predict(lead_data):
    _config = config.MELT_API_CONFIG
    _lead_data = lead_data

    _map = _config.get("data_map")
    if _map:
        print("mapping")
        _lead_data = _map(_lead_data)

    print("Mapped Data from config -----\n")
    print(_lead_data)

    # classification problem

    _prob, _cls = melt_preprocess(_config, _lead_data)
    _id = _lead_data.get("_id")
    return _prob, _cls, _id

# regression
#
# def lead_conversion(lead_data):
#     _config = config.LEAD_CONVERSION_API_CONFIG
#     _lead_data = lead_data
#
#     _map = _config.get("data_map")
#     if _map:
#         print("mapping")
#         _lead_data = _map(_lead_data)
#
#     print("Mapped Data from config -----\n")
#     print(_lead_data)
#
#     # classification problem
#
#     _prob, _cls = _predict_class(_config, _lead_data)
#     _id = _lead_data.get("_id")
#     return _prob, _cls, _id
