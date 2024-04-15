import pickle, json
from manager import DAO


def mortality_risk(json_req):
    try:
        dict = json.load(open("model_dict.json", "r"))
        clf_xgb = pickle.load(open("model.pkl", "rb"))

        proba = predict(json_req["attr"], dict["mortalidad"], clf_xgb)

        dao = DAO()

        res = {
            "message": "Predicción calculada con éxito",
            "mortality": "Alto Riesgo" if proba > 0.6 else "Bajo Riesgo",
            "probability": f"{proba * 100:.2f} %",
        }

        for i in res:
            json_req[i] = res[i]

        dao.insertCalculation(json_req)

        return {"response": res, "status": 200}
    except KeyError:
        missing = [
            validate_params(json_req, dict["min_attributes"]),
            validate_params(json_req["attr"], dict["mortalidad"]),
        ]
        return {
            "response": {
                "message": "Parámetros incompletos",
                "details": "El cuerpo de la petición no cumple con los requisitos mínimos",
                "params_missing": [x for x in missing if x is not False][0],
            },
            "status": 409,
        }


def mortality_risk():
    return 0


def predict(params, dict, model):
    vals = [params[key] for key in dict]
    return float(model.predict_proba([vals])[:, 1])


def validate_params(json_obj, dict):
    values = [i for i in dict if i not in list(json_obj.keys())]
    return False if len(values) == 0 else values
