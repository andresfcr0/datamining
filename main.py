import pickle
from flask import Flask, Response, request
import json
from manager import DAO

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello_world():
    try:
        clf_xgb = pickle.load(open("model.pkl", "rb"))
        json_req = request.get_json()

        dict = json.load(open("model_dict.json", "r"))

        proba = predict(json_req["attr"], dict["mortalidad"], clf_xgb)

        dao = DAO()

        res = {
            "message": "Prediction calculated successfully",
            "mortality": "Alto Riesgo" if proba > 0.6 else "Bajo Riesgo",
            "probability": f"{proba * 100:.2f} %",
        }

        for i in res:
            json_req[i] = res[i]

        dao.insertCalculation(json_req)

        return json_response(res, 200)
    except KeyError:
        missing = [
            validate_params(json_req, dict["min_attributes"]),
            validate_params(json_req["attr"], dict["mortalidad"]),
        ]
        return json_response(
            {
                "message": "Incomplete params",
                "details": "Request body does not fit the requirements",
                "params_missing": [x for x in missing if x is not False][0],
            },
            409,
        )


def predict(params, dict, model):
    vals = [params[key] for key in dict]
    return float(model.predict_proba([vals])[:, 1])


def validate_params(json_obj, dict):
    values = [i for i in dict if i not in list(json_obj.keys())]
    return False if len(values) == 0 else values


def json_response(json_obj, status):
    return Response(json.dumps(json_obj), status=status, mimetype="application/json")
