from flask import Flask
from ludis.schemas.sql import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'

migrate = Migrate()

def create_app():

    db.init_app(app)
    migrate.init_app(app, db)
    return