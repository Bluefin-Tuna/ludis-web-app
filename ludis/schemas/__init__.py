from enum import unique
from ludis.db import db
from datetime import datetime

class UserEventAssociation(db.Model):
    
    __tablename__ = "users_events"

    user = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key = True)
    event = db.Column(db.Integer, db.ForeignKey("events.id"), primary_key = True)

    joined_on = db.Column(db.DateTime, default = datetime.utcnow)


class UserGroupAssociation(db.Model):

    __tablename__ = "users_groups"

    user = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key = True)
    group = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key = True)

    nickname = db.Column(db.String(255))
    num_texts = db.Column(db.Integer)

    joined_on = db.Column(db.DateTime, default = datetime.utcnow)

locations_activities = db.Table(
    "locations",
    db.Column("location", db.Integer, db.ForeignKey("locations.id"), primary_key = True),
    db.Column("activity", db.Integer, db.ForeignKey("activities.id"), primary_key = True)
)

class Users(db.Model):

    __tablename__ = "users"

    id = db.Columm(db.Integer, primary_key = True)

    username = db.Column(db.String(15), unique = True, nullable = True)
    password = db.Column(db.String(20), unique = False, nullable = False)
    email = db.Column(db.String(320), unique = True, nullable = False)
    first_name = db.Column(db.String(255), unique = False, nullable = False)
    last_name = db.Column(db.String(255), unique = False, nullable = False)

    events_created = db.relationship("Events", backref = "users")
    requests_created = db.relationship("Relationships", backref = "users")
    requests_received = db.relationship("Relationships", backref = "users")
    profile = db.relationship('Profiles', backref = 'users', uselist = False)

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)

class Profiles(db.Model):

    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), unique = True)

    gender = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    description = db.Column(db.String(200))

    preferences = db.relationship("Preferences", backref='profiles', lazy = True)
    
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)

class Preferences(db.Model):

    __tablename__ = "preferences"

    id = db.Column(db.Integer, primary_key = True)
    profile = db.Column(db.Integer, db.ForeignKey("profiles.id"))
    
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
    author = db.Column(db.Integer, db.ForeignKey("users.id", nullable = False))

    chat = db.Column(db.String(255), unique = True)

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    starts_at = db.Column(db.DateTime)
    ends_at = db.Column(db.DateTime)

class Relationships(db.Model):

    __tablename__ = "relationships"

    id = db.Column(db.Integer, primary_key = True)
    requester = db.Column(db.Integer, db.ForeignKey("users.id"))
    addressee = db.Column(db.Integer, db.ForeignKey("users.id"))

    status = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)

class Groups(db.Model):

    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key = True)

    chat = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    last_used = db.Column(db.DateTime, default = datetime.utcnow)