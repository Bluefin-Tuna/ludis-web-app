# import functools
# import json
# import os
#
# import flask
#
# from authlib.client import OAuth2Session
# import google.oauth2.credentials
# import googleapiclient.discovery
#
# import google_auth
#
# app = flask.Flask(__name__)
# app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)
#
# app.register_blueprint(google_auth.app)
#
# @app.route('/')
# def index():
#     if google_auth.is_logged_in():
#         user_info = google_auth.get_user_info()
#         return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"
#
#     return 'You are not currently logged in.'

# Google Auth v2 testing flask app

# import os
# import pathlib
# import requests
# from flask import Flask, session, abort, redirect, request
# from google.oauth2 import id_token
# from google_auth_oauthlib.flow import Flow
# from pip._vendor import cachecontrol
# import google.auth.transport.requests
#
# app = Flask("Google Auth")
# app.secret_key = "password"
# os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  #this is to set our environment to https because OAuth 2.0 only supports https environments
#
# GOOGLE_CLIENT_ID = "313919470376-dhl9qq87macvamgif9fjjnba21cmogva.apps.googleusercontent.com"
# client_secrets_file = os.path.join(pathlib.Path(r"C:\Users\mohsi\ludis-web-app\ludis\app\client_secret.json").parent, "client_secret.json")  #set the path to where the .json file you got Google console is
#
# flow = Flow.from_client_secrets_file(  #Flow is OAuth 2.0 a class that stores all the information on how we want to authorize our users
#     client_secrets_file=client_secrets_file,
#     scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],  #here we are specifying what do we get after the authorization
#     redirect_uri="http://127.0.0.1:5000/callback"
# )

# JWT Auth Flask App

from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
from settings import MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

app = Flask(__name__)

app.config["MYSQL_USER"] = MYSQL_USER
app.config["MYSQL_PASSWORD"] = MYSQL_PASSWORD
app.config["MYSQL_DB"] = MYSQL_DB
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

db = MySQL(app)

from blueprint_auth import authentication

app.register_blueprint(authentication, url_prefix="/api/auth")