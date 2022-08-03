from flask import Flask
from ludis.schemas.sql import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ludis/db.sqlite3'

migrate = Migrate()
db.init_app(app)
migrate.init_app(app, db)

if __name__ == "__main__":

    app.run(debug=True)