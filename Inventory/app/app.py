from crypt import methods
import json
from urllib import response
from flask import Flask, jsonify, request,abort
from flask_cors import CORS
import requests
import logging
import base64

app = Flask(__name__)
CORS(app)
formula = {'a':3,'b':2,'c':4,'d':10}
# URL_MATERIAL = f'{INVENTORY_URL}/material'
@app.route('/api/material',methods=['POST'])
def order():
    data = request.json
    try:
        material = 0
        total = 0
        for item,count in data.items():
            material += formula.get(item)*count
            total += count
            
        return jsonify(
                material = material,
                signature = _signature(total)
            )
    except Exception as error:
        abort(500,error)
    return jsonify(
        material = 0,
        signature = _signature(0)
        )

def _signature(total):
    return base64.b64encode(str(total).encode('UTF-8')).decode('UTF-8')


@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8200, debug=True)