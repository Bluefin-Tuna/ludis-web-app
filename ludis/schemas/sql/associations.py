from ludis.schemas.sql import db
from datetime import datetime

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