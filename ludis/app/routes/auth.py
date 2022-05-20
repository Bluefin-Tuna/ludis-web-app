# from functools import wraps
# from flask import jsonify, Blueprint
# import flask
# import google_auth_oauthlib
#
# auth = Blueprint("auth", __name__)
#
# def login_required(test):
#
#     @wraps(test)
#     def wrap(*args, **kwargs):
#
#         return
#
#     return wrap
#
# def admin_required(test):
#
#     @wraps(test)
#     def wrap(*args, **kwargs):
#
#         return
#
#     return
#
# @auth.route('/auth/sign-in')
# def sign_in():
#
#     return
#
# @auth.route('/auth/authorize')
# def authorize():
#
#     flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
#     flow.redirect_uri = flask.url_for('callback', _external=True)
#
#     authorization_url, state = flow.authorization_url(
#         access_type='offline',
#         include_granted_scopes='true')
#
#     flask.session['state'] = state
#
#     return flask.redirect(authorization_url)
#
#
# @auth.route('/auth/callback')
# def callback():
#
#     state = flask.session['state']
#
#     flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
#         CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
#     flow.redirect_uri = flask.url_for('callback', _external=True)
#
#     authorization_response = flask.request.url
#     flow.fetch_token(authorization_response=authorization_response)
#
#     credentials = flow.credentials
#     flask.session['credentials'] = credentials_to_dict(credentials)
#
#     return flask.redirect(flask.url_for('sign_in'))
#
# @auth.route('/auth/sign-out')
# @login_required
# def sign_out():
#
#     return
#
# def credentials_to_dict(credentials):
#
#     return {
#         'token': credentials.token,
#         'refresh_token': credentials.refresh_token,
#         'token_uri': credentials.token_uri,
#         'client_id': credentials.client_id,
#         'client_secret': credentials.client_secret,
#         'scopes': credentials.scopes
#     }

import pyrebase

# import firebase_admin
# from firebase_admin import credentials

# config = {
#     "apiKey": "AIzaSyDE0qn7eQH9NQy1AlHDXg1rsdFw6Z6RcKU",
#     "authDomain": "ludiswebapp.firebaseapp.com",
#     "projectId": "ludiswebapp",
#     "storageBucket": "ludiswebapp.appspot.com",
#     "messagingSenderId": "1060610658237",
#     "appId": "1:1060610658237:web:3fd927055703f383420cd4",
#     "measurementId": "G-02HN41C522"
# }
from ludis.app import config

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


# EMAIL AUTH
def signup(email, password):
    # redirect to signup page
    try:
        user = auth.create_user_with_email_and_password(email, password)
    except:
        pass
#     There is already a user with this email


def login(email, password):
    #  redirect to login page
    login = auth.sign_in_with_email_and_password(email, password)

# GOOGLE AUTH
# cred = credentials.Certificate("path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
