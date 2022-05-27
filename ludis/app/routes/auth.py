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
import functools
import os

import flask

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

ACCESS_TOKEN_URI = 'https://www.googleapis.com/oauth2/v4/token'
AUTHORIZATION_URL = 'https://accounts.google.com/o/oauth2/v2/auth?access_type=offline&prompt=consent'

AUTHORIZATION_SCOPE = 'openid email profile'

# AUTH_REDIRECT_URI = os.environ.get("FN_AUTH_REDIRECT_URI", default=False)
# BASE_URI = os.environ.get("FN_BASE_URI", default=False)
CLIENT_ID = os.environ.get("313919470376-dhl9qq87macvamgif9fjjnba21cmogva.apps.googleusercontent.com", default=False)
CLIENT_SECRET = os.environ.get("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", default=False)

AUTH_TOKEN_KEY = 'auth_token'
AUTH_STATE_KEY = 'auth_state'

app = flask.Blueprint('google_auth', __name__)


def is_logged_in():
    return True if AUTH_TOKEN_KEY in flask.session else False


def build_credentials():
    if not is_logged_in():
        raise Exception('User must be logged in')

    oauth2_tokens = flask.session[AUTH_TOKEN_KEY]

    return google.oauth2.credentials.Credentials(
        oauth2_tokens['access_token'],
        refresh_token=oauth2_tokens['refresh_token'],
        client_id="313919470376-dhl9qq87macvamgif9fjjnba21cmogva.apps.googleusercontent.com",
        client_secret="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",
        token_uri=ACCESS_TOKEN_URI)


def get_user_info():
    credentials = build_credentials()

    oauth2_client = googleapiclient.discovery.build(
        'oauth2', 'v2',
        credentials=credentials)

    return oauth2_client.userinfo().get().execute()


def no_cache(view):
    @functools.wraps(view)
    def no_cache_impl(*args, **kwargs):
        response = flask.make_response(view(*args, **kwargs))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return functools.update_wrapper(no_cache_impl, view)


@app.route('/google/login')
@no_cache
def login():
    session = OAuth2Session("313919470376-dhl9qq87macvamgif9fjjnba21cmogva.apps.googleusercontent.com", "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",
                            scope=AUTHORIZATION_SCOPE,
                            redirect_uri=AUTH_REDIRECT_URI)

    uri, state = session.authorization_url(AUTHORIZATION_URL)

    flask.session[AUTH_STATE_KEY] = state
    flask.session.permanent = True

    return flask.redirect(uri, code=302)


@app.route('/google/auth')
@no_cache
def google_auth_redirect():
    req_state = flask.request.args.get('state', default=None, type=None)

    if req_state != flask.session[AUTH_STATE_KEY]:
        response = flask.make_response('Invalid state parameter', 401)
        return response

    session = OAuth2Session(CLIENT_ID, CLIENT_SECRET,
                            scope=AUTHORIZATION_SCOPE,
                            state=flask.session[AUTH_STATE_KEY],
                            redirect_uri=AUTH_REDIRECT_URI)

    oauth2_tokens = session.fetch_access_token(
        ACCESS_TOKEN_URI,
        authorization_response=flask.request.url)

    flask.session[AUTH_TOKEN_KEY] = oauth2_tokens

    return flask.redirect(BASE_URI, code=302)


@app.route('/google/logout')
@no_cache
def logout():
    flask.session.pop(AUTH_TOKEN_KEY, None)
    flask.session.pop(AUTH_STATE_KEY, None)

    return flask.redirect(BASE_URI, code=302)
