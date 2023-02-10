from crypt import methods
from sqlite3 import Timestamp
from urllib import response
from venv import create
from flask import Flask, jsonify, request,abort,g
from flask_cors import CORS
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true
app = Flask(__name__)
CORS(app)
#  取得目前文件資料夾路徑
pjdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#  新版本的部份預設為none，會有異常，再設置True即可。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#  設置sqlite檔案路徑
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(pjdir, 'data.sqlite')
db = SQLAlchemy(app)
class data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime)
    signature = db.Column(db.String(20))
    material = db.Column(db.Float)
    a = db.Column(db.Float, unique=False)
    b = db.Column(db.Float, unique=False)
    c = db.Column(db.Float, unique=False)
    d = db.Column(db.Float)
    def __init__(self, location, timestamp,signature,material,a,b,c,d):
        self.location = location
        self.timestamp = timestamp
        self.signature = signature
        self.material = material
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def toJSON(self):
        return{
            'location': self.location, 
            'timestamp': self.timestamp.strftime("%Y-%m-%dT%H:%M:%S%z"),
            'signature': self.signature,
            'material': self.material,
            'a':self.a, 
            'b':self.b, 
            'c':self.c, 
            'd':self.d 
        }

@app.route('/')
def index():
    # Create data
    with app.app_context():
        db.create_all()
    return 'ok'

@app.route('/api/records',methods=['POST'])
def save():
    response = request.json   
    date = datetime.strptime(response.get('timestamp'), "%Y-%m-%dT%H:%M:%S%z")
    
    datas = data(
        location = response.get('location'),
        timestamp = date,
        signature = response.get('signature'),
        material = response.get('material'),
        a = response.get('data').get('a'),
        b = response.get('data').get('b'),
        c = response.get('data').get('c'),
        d = response.get('data').get('d')
    )
    try: 
        db.session.add(datas)
        db.session.commit()
        return 'ok'
    except Exception as error:
        abort(500,error)
from sqlalchemy import func
@app.route('/api/records',methods=['GET'])
def records():
    location = request.args['location']
    date = request.args['date']
    d_date = datetime.strptime(date,"%Y-%m-%d")
    datas = data.query.filter_by(location = location ,timestamp = d_date).all()
    if datas is None:
        return []
    detail_data = [data.toJSON() for data in datas]
    return detail_data


@app.route('/api/report',methods=['GET'])
def report():
    location = request.args['location']
    date = request.args['date']
    d_date = datetime.strptime(date,"%Y-%m-%d")
    datas = data.query.filter_by(location = location ,timestamp = d_date).all()
    if datas is None:
        data_list = {}
    else:
        data_list = {
            "location" : location,
            "date" : date,
            "count" : len(datas),
            "material" : sum(r.material for r in datas),
            "a" : sum(r.a for r in datas),
            "b" : sum(r.b for r in datas),
            "c" : sum(r.c for r in datas),
            "d" : sum(r.d for r in datas)
        }
    return data_list
        




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8300, debug=True)