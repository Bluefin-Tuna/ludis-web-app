# from flask import Flask
# from flask_graphql import GraphQLView

# from schema import schema

# app = Flask(__name__)

# app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
#     'graphql',
#     schema=schema,
#     graphiql=True,
# ))

# # Optional, for adding batch query support (used in Apollo-Client)
# app.add_url_rule('/graphql/batch', view_func=GraphQLView.as_view(
#     'graphql',
#     schema=schema,
#     batch=True
# ))

# if __name__ == '__main__':
#     app.run()


from flask import Flask
from ludis.schemas.sql import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

migrate = Migrate()
db.init_app(app)
migrate.init_app(app, db)

if __name__ == "__main__":

    app.run(debug=True)