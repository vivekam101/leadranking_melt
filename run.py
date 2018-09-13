from flask import Flask, jsonify, request, render_template,send_file,send_from_directory
from app.controllers import classification
import json
import numpy as np
import sys
from app.json_encoder import myJSONEncoder

_app = Flask(__name__)
_app.json_encoder = myJSONEncoder


@_app.route('/')
def index():
    return render_template("index.html")

@_app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@_app.route('/leadranking', methods=['POST'])
def lead_ranking():
    try:
        _data = request.json
        print("JSON DATA")
        print(_data)
        # _score, _rank, _ownerid, _cls, _id, _importance, _owner_reccomendations = classification.predict(_data)
        _score, _cls,_id = classification.lead_ranking_predict(_data)
        # if _cls =='1':
        #     _cls = "Enrolled"
        # else:
        #     _cls = "Not Enrolled"
        if _score < 35:
            _r = "Cold"
        elif _score < 70:
            _r = "Warm"
        else:
            _r = "Hot"

        print(_r)
        # _reccomendations = reccomendation_controller.get_program_reccomendations(_data)

        return jsonify({
            "success": True,
            "lead_id": _id,
            "status": 200,
            "score": _score,
            "class": str(_r),
            # "owner_id": _ownerid,
            # "feature_importance": _importance,
            # "program_reccomendations": _reccomendations,
            # "owner_reccomendations": _owner_reccomendations
        })
    except Exception as e:
        return jsonify({"success": False, "status": 500, "err": e.args, })

@_app.route('/melt', methods=['POST'])
def melt():
    try:
        _data = request.json
        print("JSON DATA")
        print(_data)
        _score, _cls, _id = classification.melt_predict(_data)
        return jsonify({"success": True, "lead_id":_id, "status":200, "probability": _score, "class": str(_cls)})
    except Exception as e:
        return jsonify({"success": False, "status":500 ,"err":e.args,})

if __name__ == '__main__':
    _app.run(host="0.0.0.0", port=8089)
