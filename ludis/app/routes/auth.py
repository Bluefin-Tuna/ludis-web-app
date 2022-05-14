from functools import wraps
from flask import jsonify, Blueprint
import flask
import google_auth_oauthlib

auth = Blueprint("auth", __name__)

def login_required(test):

    @wraps(test)    
    def wrap(*args, **kwargs):

        return

    return wrap

def admin_required(test):

    @wraps(test)
    def wrap(*args, **kwargs):

        return

    return

@auth.route('/auth/sign-in')
def sign_in():

    return

@auth.route('/auth/authorize')
def authorize():

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.redirect_uri = flask.url_for('callback', _external=True)

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')

    flask.session['state'] = state

    return flask.redirect(authorization_url)


@auth.route('/auth/callback')
def callback():
    
    state = flask.session['state']

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = flask.url_for('callback', _external=True)

    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    flask.session['credentials'] = credentials_to_dict(credentials)

    return flask.redirect(flask.url_for('sign_in'))

@auth.route('/auth/sign-out')
@login_required
def sign_out():
    
    return

def credentials_to_dict(credentials):

    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }