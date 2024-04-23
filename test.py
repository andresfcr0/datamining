import json, pickle


def handler(event):
    dict = json.load(open("model_dict.json", "r"))
    clf_xgb = pickle.load(open("model.pkl", "rb"))

    if validate_params(event, dict["min_attributes"]):
        return incomplete_error(validate_params(event, dict["min_attributes"]))
    elif validate_params(event["attr"], dict["mortalidad"]):
        return incomplete_error(validate_params(event["attr"], dict["mortalidad"]))
    
    proba = predict(event["attr"], dict["mortalidad"], clf_xgb)

    return {
        "message": "Prediccion calculada con exito",
        "mortality": "Alto Riesgo" if proba > 0.6 else "Bajo Riesgo",
        "probability": f"{proba * 100:.2f} %",
    }


def predict(params, dict, model):
    vals = [params[key] for key in dict]
    return model.predict_proba([vals])[:, 1][0]


def validate_params(json_obj, dict):
    values = [i for i in dict if i not in list(json_obj.keys())]
    return values if len(values) > 0 else False


def incomplete_error(error):
    return {
        "message": "Parametros incompletos",
        "details": "El cuerpo de la peticion no cumple con los requisitos minimos",
        "params_missing": error,
    }


event = {
    "user_id": "0fe0d662-8196-4293-87d1-0e775ce1dbd2",
    "attr": {
        "edadmintervencion": 80,
        "sexopte": 1,
        "taaquismo": 0,
        "mtabaco": 0,
        "imc": 35,
        "hta": 0,
        "arritmiacard": 0,
        "erc": 0,
        "fallacardcron": 0,
        "dislipidemia": 0,
        "dm": 0,
        "epoc": 0,
        "trantiroideo": 0,
        "diagcovid19": 0,
        "covid19menor2": 0,
        "esquemavacu": 0,
        "estratosocioecono": 2,
        "afiliacionsistema": 2,
        "asascore": 3,
        "complejidadprocedimiento": 2,
        "momntointerven": 0,
        "inestabilidadhemodinamica": 0,
        "parocardiacopreoperatorio": 0,
        "tipocx": 1000,
        "tipodeabordajecx": 1,
    },
}


print(handler(event))
