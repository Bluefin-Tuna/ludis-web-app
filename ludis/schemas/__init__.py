from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):

    __tablename__ = "users"

    id = db.Columm(db.Integer, primary_key = True)

    username = db.Column(db.String(15), unique = True, nullable = True)
    password = db.Column(db.String(20), unique = False, nullable = False)
    email = db.Column(db.String(320), unique = True, nullable = False)
    first_name = db.Column(db.String(255), unique = False, nullable = False)
    last_name = db.Column(db.String(255), unique = False, nullable = False)

    fp = db.relationship('Profiles', backref = 'users', uselist = False)

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class Profiles(db.Model):

    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), unique = True)

    gender = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    description = db.Column(db.String(200))

    preferences = db.relationship("Preferences", backref='profiles', lazy = True)
    
    updated_at = db.Column(db.DateTime)

class Preferences(db.Model):

    __tablename__ = "preferences"

    id = db.Column(db.Integer, primary_key = True)
    fp = db.Column(db.Integer, db.ForeignKey("profiles.id"))
    
    level = db.Column(db.Integer)
    user_popularity = db.Column(db.Integer)

    activity = db.relationship("Activities", backref = "preferences", lazy = True)

class Activities(db.Model):

    __tablename__ = "activities"

    id = db.Column(db.Integer, primary_key = True)

    attribute = db.Column(db.Integer)
    name = db.Column(db.String(50))
    description = db.Column(db.String(255))
    popularity = db.Column(db.Integer)

class Locations(db.Model):

    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String())
    geo_location = db.Column(db.String(255))

    events = db.relationship("Events", backref='locations', lazy = True)

class Events(db.Model):

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key = True)
    location = db.Column(db.Integer, db.ForeignKey("locations.id", nullable = False))

    chat_log = db.Column(db.String(255), unique = True)


    created_at = db.Column(db.DateTime)
    starts_at = db.Column(db.DateTime)
    ends_at = db.Column(db.DateTime)


