# ===============================================================
# Author: Rodolfo Ferro
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro,
# for his workshop at RIIAA 2.0. Any explicit usage of
# this script or its contents is granted according to
# the license provided and its conditions.
# ===============================================================

# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from iris import iris_classifier
from pprint import pprint
import numpy as np
import requests
import json

# Main app:
app = Flask(__name__)

# Global:
version = 'v0.0'
# Load iris classifier
species = {'0': 'I. setosa', '1': 'I. versicolor', '2': 'I. virginica'}


# API MAIN STRUCTURE:
@app.route('/api/' + version, methods=['GET'])
def test():
    """
    GET method to test the API.
    """

    # Output message:
    message = {"response": [{"text": "Hello world!"}]}
    return jsonify(message)


@app.route('/api/' + version + '/predict', methods=['POST'])
def predict():
    """
    POST method to predict with our classification model.
    """

    # Get data from JSON object in POST method:
    req_data = request.get_json()

    # Parse data from JSON:
    # sl <- 'sepal_length' from req_data
    # sw <- 'sepal_width' from req_data
    # pl <- 'petal_length' from req_data
    # pw <- 'petal_width' from req_data

    # Predict with model:
    input_data = np.array([[sl, sw, pl, pw]])
    prediction = classifier.predict(input_data)
    print(prediction)

    # Output message:
    message = {"response": [
        {"input": {
            'sepal_length': sl,
            'sepal_width': sw,
            'petal_length': pl,
            'petal_width': pw
        }},
        {"prediction": int(prediction[0])},
        {"species": species[str(prediction[0])]}]}
    return jsonify(message)


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404

    return response


if __name__ == '__main__':
    app.run(debug=True, port=5000)
