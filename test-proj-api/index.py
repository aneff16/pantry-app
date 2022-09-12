from crypt import methods
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from configparser import ConfigParser

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# get config file for database user and password
config = ConfigParser()
config.read('/home/aneff/web-dev/config/keys_config.cfg')

username = config.get('pantry_db', 'user')
password = config.get('pantry_db', 'password')
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server  = '127.0.0.1:9999'
dbname   = '/pantry_tracker'

app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# database tables
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    pantry = db.relationship('Pantry', backref='users', lazy=True)

    def __init__(self, name) -> None:
        self.user_name = name


class PantryItem(db.Model):
    __tablename__ = 'pantry_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    pantries = db.relationship('Pantry', backref='pantry_items', lazy=True)

    def __init__(self, name) -> None:
        self.name = name


class Pantry(db.Model):
    __tablename__ = 'pantry'

    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('users.id'),
        primary_key=True,
        autoincrement=False, 
        nullable=False
    )
    item_id = db.Column(
        db.Integer, 
        db.ForeignKey('pantry_items.id'),
        primary_key=True,
        autoincrement=False,
        nullable=False
    )
    quantity = db.Column(db.Integer, nullable=False)

    # function to convert Pantry object to a dictionary
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


items = []

@app.route('/items')
def get_items():
    try:
        pantry = Pantry.query.filter_by(user_id=1).all()
        pantry_dict = []
        for p in pantry:
            # get the name of the pantry item
            name = p.pantry_items.name
            # convert Pantry object to a dictionary
            temp = p.as_dict()
            # add the item name to the dictionary
            temp['name'] = name
            pantry_dict.append(temp)
            
        print(f"The pantry is: ", pantry_dict)
        return jsonify(pantry_dict)

    except Exception as e:
        # see Terminal for description of the error
        print("\nThe error:\n" + str(e) + "\n")
        return


@app.route('/items/<id>', methods=['POST'])
def add_item(id):
    items.append(request.get_json())
    return '', 204

@app.route('/items/<id>', methods=['PUT'])
def edit_item(id):
    item = request.get_json()
    for i in range(len(items)):
        if items[i]['name'] == item['name']:
            items[i] = item
    return '', 204

@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    temp = []
    global items
    for i in items:
        if i['id'] != int(id):
            temp.append(i)
    items = temp
    return '', 204