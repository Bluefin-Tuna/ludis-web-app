from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):

    __tablename__ = "users"
    id = db.Columm(db.Integer, primary_key = True)