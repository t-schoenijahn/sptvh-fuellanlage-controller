#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/actuator', methods=['GET'])
def actuator():
    return jsonify({'status': 'up'})

@app.route('/token/validate', methods=['GET'])
def validate():
    authorized = False
    key = request.headers.get('X-API-KEY')
    token = request.get_json()['token']
    if token == key:
        authorized = True
    return jsonify({'authorized': authorized})

app.run()
