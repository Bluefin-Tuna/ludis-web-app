from ludis.app.routes import auth, base
from flask import Flask

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(base)

if __name__ == "__main__":

    app.run(debug=True)