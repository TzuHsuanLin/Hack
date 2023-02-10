from crypt import methods
from urllib import response
from venv import create
from flask import Flask, jsonify, request,abort,g
from flask_cors import CORS
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
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

@app.route('/')
def index():
    # Create data
    with app.app_context():
        db.create_all()
    return 'ok'

@app.route('/records',methods=['POST','GET'])
def save():
    if request.method == 'POST':
        response = request.json
        print(response.get('location'))
        print(response.get('data').get('a'))
        print(response.get('timestamp'))
        date = datetime.strptime(response.get('timestamp'), "%Y-%m-%dT%H:%M:%S%z")
        
        print("date:", date.strftime("%Y-%m-%dT%H:%M:%S%z"))
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
    else:
        return 0




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8300, debug=True)