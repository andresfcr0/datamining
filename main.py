import json
from flask import Flask, Response, request
from functions import mortality_risk, outcome_calculation

app = Flask(__name__)


@app.route("/", methods=["POST"])
def mortality():
    json_req = request.get_json()
    mort = mortality_risk(json_req)
    return json_response(mort["response"], mort["status"])


@app.route("/", methods=["GET"])
def pending_outcomes():
    return json_response(outcome_calculation(), 200)


def json_response(json_obj, status):
    return Response(json.dumps(json_obj), status=status, mimetype="application/json")
