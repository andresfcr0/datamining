import pickle
from flask import Flask, request
import numpy as np

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello_world():
    clf_xgb = pickle.load(open('model.pkl', 'rb'))
    vals = request.get_json().values()
    pred = clf_xgb.predict([list(vals)])
    proba = clf_xgb.predict_proba([list(vals)])
    
    return {'mortalidad': int(pred), 'probabilidad': float(proba[:, 1])}