from crypt import methods
import json
from urllib import response
from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
# URL_MATERIAL = f'{INVENTORY_URL}/material'
@app.route('/material',methods=['POST'])
def order():
    print('RRRRR')
    # data = request.json
    # print(data.get('data'))
    # # response = requests.post(url=URL_MATERIAL,json=data.get('data'))
    # print(data.get('location'))
    # print(data.get('timestamp'))
    # print(data)
    return 'True'


@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8200, debug=True)