from enum import unique
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserEventAssociation(db.Model):
    
    __tablename__ = "users_events"

    user = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key = True)
    event = db.Column(db.Integer, db.ForeignKey("events.id"), primary_key = True)

    users = db.relationship("Users", back_populates = "events")
    events = db.relationship("Events", back_populates = "users")

    joined_on = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"<UserEvent: {self.user}, {self.event}>"

class UserGroupAssociation(db.Model):

    __tablename__ = "users_groups"

    user = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key = True)
    group = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key = True)

    nickname = db.Column(db.String(255))
    num_texts = db.Column(db.Integer, default = 0)

    users = db.relationship("Users", back_populates = "groups")
    groups = db.relationship("Groups", back_populates = "users")

    joined_on = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"<UserGroup: {self.user}, {self.group}>"

locations_activities = db.Table(
    
    "locations_activities",

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

    events_created = db.relationship("Events", backref = "user")
    events_joined = db.relationship("UserEventAssociation", back_populates = "users")
    requests_created = db.relationship("Relationships", backref = "user")
    requests_received = db.relationship("Relationships", backref = "user")
    groups_joined = db.relationship("UserGroupAssociation", back_populates = "users")
    profile = db.relationship('Profiles', backref = 'user', uselist = False)

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"<User {self.id}>"

class Profiles(db.Model):

    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), unique = True)

    fitness_level = db.Column(db.Integer, default = 5)
    gender = db.Column(db.Integer, default = -1)
    weight = db.Column(db.Integer, default = -1)
    description = db.Column(db.Text, default = "")
    phone_number = db.Column(db.String(20), unique = True)

    preferences = db.relationship("Preferences", backref='profile', lazy = True)
    
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Profile {self.id}>"

class Preferences(db.Model):

    __tablename__ = "preferences"

    id = db.Column(db.Integer, primary_key = True)
    profile = db.Column(db.Integer, db.ForeignKey("profiles.id"))
    
    experience_level = db.Column(db.Integer, default = 5)
    user_popularity = db.Column(db.Integer, default = 0)

    activity = db.relationship("Activities", backref = "preference", lazy = True)

    def __repr__(self) -> str:
        return f"<Preference {self.id}>"

class Activities(db.Model):

    __tablename__ = "activities"

    id = db.Column(db.Integer, primary_key = True)

    attribute = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String(50), nullable = False, unique = True)
    description = db.Column(db.String(255))
    popularity = db.Column(db.Integer, default = 0)

    locations = db.relationship("Locations", secondary = locations_activities, backref = "activities")

    def __repr__(self) -> str:
        return f"<Activity {self.id}>"

class Locations(db.Model):

    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(255))
    geo_location = db.Column(db.String(255))

    events = db.relationship("Events", backref='location', lazy = True)

    def __repr__(self) -> str:
        return f"<Location {self.id}>"

class Events(db.Model):

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key = True)
    location = db.Column(db.Integer, db.ForeignKey("locations.id"))
    author = db.Column(db.Integer, db.ForeignKey("users.id"))

    chat = db.Column(db.String(255), unique = True)
    recurring = db.Column(db.Boolean, default = False)

    participants = db.relationship("UserEventAssociation", back_populates = "events")

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    starts_at = db.Column(db.DateTime, nullable = False)
    ends_at = db.Column(db.DateTime, nullable = False)

    def __repr__(self) -> str:
        return f"<Event {self.id}>"

class Relationships(db.Model):

    __tablename__ = "relationships"

    id = db.Column(db.Integer, primary_key = True)
    requester = db.Column(db.Integer, db.ForeignKey("users.id"))
    addressee = db.Column(db.Integer, db.ForeignKey("users.id"))

    status = db.Column(db.Integer, default = 0) # Status Codes --> (0: Requested), (1: Accepted), (2: Declined)

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Relationship {self.id}>"

class Groups(db.Model):

    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key = True)

    chat = db.Column(db.String(255))

    users = db.relationship("UserGroupAssociation", back_populates = "groups")

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    last_used = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Group {self.id}>"