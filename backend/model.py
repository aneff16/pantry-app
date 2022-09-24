from flask_sqlalchemy import SQLAlchemy

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy()

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
