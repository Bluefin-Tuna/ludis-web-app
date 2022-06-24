from ludis.schemas.sql import db
from ludis.schemas.sql.associations import locations_activities, UserEventAssociation, UserGroupAssociation
from datetime import datetime

class Users(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)

    username = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(20), unique = False, nullable = False)
    email = db.Column(db.String(255), unique = True, nullable = False)
    first_name = db.Column(db.String(255), unique = False, nullable = False)
    last_name = db.Column(db.String(255), unique = False, nullable = False)

    events_created = db.relationship("Events", backref = "user", passive_deletes = True)
    events_joined = db.relationship("UserEventAssociation", back_populates = "users", passive_deletes = True)
    requests_created = db.relationship("Relationships", backref = "user", passive_deletes = True)
    requests_received = db.relationship("Relationships", backref = "user", passive_deletes = True)
    groups = db.relationship("UserGroupAssociation", back_populates = "users", passive_deletes = True)
    profile = db.relationship('Profiles', backref = 'user', uselist = False, passive_deletes = True)

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"<User {self.id}>"

class Profiles(db.Model):

    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Integer, db.ForeignKey('users.id', ondelete = "CASCADE"), nullable = False)

    fitness_level = db.Column(db.Integer, default = 5)
    gender = db.Column(db.Integer, default = -1)
    weight = db.Column(db.Integer, default = -1)
    description = db.Column(db.Text, default = "")
    phone_number = db.Column(db.String(255), unique = True)

    preferences = db.relationship("Preferences", backref='profile', lazy = True, passive_deletes = True)
    
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Profile {self.id}>"

class Preferences(db.Model):

    __tablename__ = "preferences"

    id = db.Column(db.Integer, primary_key = True)
    profile = db.Column(db.Integer, db.ForeignKey("profiles.id", ondelete = "CASCADE"), nullable = False)
    activity = db.Column(db.Integer, db.ForeignKey("activities.id", ondelete = "CASCADE"), nullable = False)

    experience = db.Column(db.Integer, default = 5)
    user_popularity = db.Column(db.Integer, default = 0)

    last_used = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return f"<Preference {self.id}>"

class Activities(db.Model):

    __tablename__ = "activities"

    id = db.Column(db.Integer, primary_key = True)

    attribute = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String(255), nullable = False, unique = True)
    description = db.Column(db.String(255))
    popularity = db.Column(db.Integer, default = 0)

    preferences = db.relationship("Preferences", backref = "activity", lazy = True, passive_deletes = True)
    locations = db.relationship("Locations", secondary = locations_activities, backref = db.backref("activities", passive_deletes = True))
    events = db.relationship("Events", backref = "activity", lazy = True, passive_deletes = True)

    def __repr__(self) -> str:
        return f"<Activity {self.id}>"

class Locations(db.Model):

    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(255))
    geo_location = db.Column(db.String(255))

    activities = db.relationship("Activities", secondary = locations_activities, backref = db.backref("locations", passive_deletes = True))
    events = db.relationship("Events", backref='location', lazy = True, passive_deletes = True)

    def __repr__(self) -> str:
        return f"<Location {self.id}>"

class Events(db.Model):

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key = True)
    location = db.Column(db.Integer, db.ForeignKey("locations.id", ondelete = "SET NULL"), nullable = True)
    author = db.Column(db.Integer, db.ForeignKey("users.id", ondelete = "SET NULL"), nullable = True)
    activity = db.Column(db.Integer, db.ForeignKey("activities.id", ondelete = "SET NULL"), nullable = True)

    chat = db.Column(db.String(255), unique = True, nullable = False)
    recurring = db.Column(db.Boolean, default = False)

    participants = db.relationship("UserEventAssociation", back_populates = "events", passive_deletes = True)

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    starts_at = db.Column(db.DateTime, nullable = False)
    ends_at = db.Column(db.DateTime, nullable = False)

    def __repr__(self) -> str:
        return f"<Event {self.id}>"

class Relationships(db.Model):

    __tablename__ = "relationships"

    id = db.Column(db.Integer, primary_key = True)
    requester = db.Column(db.Integer, db.ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)
    addressee = db.Column(db.Integer, db.ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)

    status = db.Column(db.Integer, default = 0) # Status Codes --> (0: Requested), (1: Accepted), (2: Declined)

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Relationship {self.id}>"

class Groups(db.Model):

    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key = True)

    chat = db.Column(db.String(255))

    users = db.relationship("UserGroupAssociation", back_populates = "groups", passive_deletes = True)

    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    last_used = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Group {self.id}>"