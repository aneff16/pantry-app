import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from configparser import ConfigParser

# get config file for database user and password
config = ConfigParser()
config.read('/home/aneff/web-dev/config/keys_config.cfg')

app = Flask(__name__)

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


# this route will test the database connection and nothing more
@app.route('/')
def testdb():
    try:
        """new_pantry_item = PantryItem('Bread')
        db.session.add(new_pantry_item)
        db.session.commit()
        users = User.query.all()
        items = PantryItem.query.all()
        add_to_pantry = Pantry(user_id=users[0].id, item_id=items[0].id, quantity=1)
        db.session.add(add_to_pantry)
        db.session.commit()"""
        pantry = Pantry.query.filter_by(user_id=1).all()
        """text = '<h1>'
        for item in pantry:
            text += item.pantry_items.name + '<h1>'"""
        return pantry

    except Exception as e:
        # see Terminal for description of the error
        print("\nThe error:\n" + str(e) + "\n")
        return '<h1>Something is amiss.</h1>'

if __name__ == '__main__':
    app.run(debug=True)