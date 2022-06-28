from ludis.schemas.sql import db
from datetime import datetime

class ProfileEventAssociation(db.Model):
    
    __tablename__ = "profiles_events"

    profile = db.Column(db.Integer, db.ForeignKey("profiles.id", ondelete = "CASCADE"), primary_key = True)
    event = db.Column(db.Integer, db.ForeignKey("events.id", ondelete = "CASCADE"), primary_key = True)

    users = db.relationship("Profiles", back_populates = "events")
    events = db.relationship("Events", back_populates = "profiles")

    joined_on = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"<ProfileEvent: {self.user}, {self.event}>"

class ProfileGroupAssociation(db.Model):

    __tablename__ = "profiles_groups"

    profile = db.Column(db.Integer, db.ForeignKey("profiles.id", ondelete = "CASCADE"), primary_key = True)
    group = db.Column(db.Integer, db.ForeignKey("groups.id", ondelete = "CASCADE"), primary_key = True)

    nickname = db.Column(db.String(255))
    num_texts = db.Column(db.Integer, default = 0)

    profiles = db.relationship("Profiles", back_populates = "groups")
    groups = db.relationship("Groups", back_populates = "profiles")

    joined_on = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"<ProfileGroup: {self.user}, {self.group}>"

locations_activities = db.Table(
    
    "locations_activities",

    db.Column("location", db.Integer, db.ForeignKey("locations.id", ondelete = "CASCADE"), primary_key = True),
    db.Column("activity", db.Integer, db.ForeignKey("activities.id", ondelete = "CASCADE"), primary_key = True)

)