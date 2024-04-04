import pickle
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello_world():
    clf_xgb = pickle.load(open("model.pkl", "rb"))
    vals = request.get_json().values()
    proba = clf_xgb.predict_proba([list(vals)])

    return {
        "mortalidad": "Alto Riesgo" if float(proba[:, 1]) > 0.6 else "Bajo Riesgo",
        "probabilidad": float(proba[:, 1]),
    }
