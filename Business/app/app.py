from crypt import methods
import json
from urllib import response
from flask import Flask, request
from flask_cors import CORS
import requests

from config import INVENTORY_URL,STORAGE_URL
app = Flask(__name__)
CORS(app)
URL_MATERIAL = f'{INVENTORY_URL}/material/'
URL_SAVE = f'{STORAGE_URL}/records/'
@app.route('/api/order',methods=['POST'])
def order():
    data = request.json
    response = requests.post(url=URL_MATERIAL,json=data.get('data'))
    z = data.copy()
    z.update(response.json())
    return requests.post(url=URL_SAVE,json=z).text

@app.route('/api/record/',methods=['GET'])
def query():
    location = request.args['location']
    date = request.args['date']
    response = requests.get(url=f'{STORAGE_URL}/records?location={location}&date={date}')
    return response.content


@app.route('/api/report/',methods=['GET'])
def report():
    location = request.args['location']
    date = request.args['date']
    response = requests.get(url=f'{STORAGE_URL}/report?location={location}&date={date}')
    return response.content


@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8100, debug=True)