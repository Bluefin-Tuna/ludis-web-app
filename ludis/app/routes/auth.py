# # from functools import wraps
# # from flask import jsonify, Blueprint
# # import flask
# # import google_auth_oauthlib
# #
# # auth = Blueprint("auth", __name__)
# #
# # def login_required(test):
# #
# #     @wraps(test)
# #     def wrap(*args, **kwargs):
# #
# #         return
# #
# #     return wrap
# #
# # def admin_required(test):
# #
# #     @wraps(test)
# #     def wrap(*args, **kwargs):
# #
# #         return
# #
# #     return
# #
# # @auth.route('/auth/sign-in')
# # def sign_in():
# #
# #     return
# #
# # @auth.route('/auth/authorize')
# # def authorize():
# #
# #     flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
# #     flow.redirect_uri = flask.url_for('callback', _external=True)
# #
# #     authorization_url, state = flow.authorization_url(
# #         access_type='offline',
# #         include_granted_scopes='true')
# #
# #     flask.session['state'] = state
# #
# #     return flask.redirect(authorization_url)
# #
# #
# # @auth.route('/auth/callback')
# # def callback():
# #
# #     state = flask.session['state']
# #
# #     flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
# #         CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
# #     flow.redirect_uri = flask.url_for('callback', _external=True)
# #
# #     authorization_response = flask.request.url
# #     flow.fetch_token(authorization_response=authorization_response)
# #
# #     credentials = flow.credentials
# #     flask.session['credentials'] = credentials_to_dict(credentials)
# #
# #     return flask.redirect(flask.url_for('sign_in'))
# #
# # @auth.route('/auth/sign-out')
# # @login_required
# # def sign_out():
# #
# #     return
# #
# # def credentials_to_dict(credentials):
# #
# #     return {
# #         'token': credentials.token,
# #         'refresh_token': credentials.refresh_token,
# #         'token_uri': credentials.token_uri,
# #         'client_id': credentials.client_id,
# #         'client_secret': credentials.client_secret,
# #         'scopes': credentials.scopes
# #     }
#
# import pyrebase
#
# # config = {
# #     "apiKey": "AIzaSyDE0qn7eQH9NQy1AlHDXg1rsdFw6Z6RcKU",
# #     "authDomain": "ludiswebapp.firebaseapp.com",
# #     "projectId": "ludiswebapp",
# #     "storageBucket": "ludiswebapp.appspot.com",
# #     "messagingSenderId": "1060610658237",
# #     "appId": "1:1060610658237:web:3fd927055703f383420cd4",
# #     "measurementId": "G-02HN41C522"
# # }
# from ludis.app import config
#
# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
#
#
# # EMAIL AUTH
# def signup(email, password):
#     # redirect to signup page
#     try:
#         user = auth.create_user_with_email_and_password(email, password)
#     except:
#         raise Exception('There is already a user with this email.')
#
#
# def login(email, password):
#     #  redirect to login page
#     login = auth.sign_in_with_email_and_password(email, password)
#
# # GOOGLE AUTH
# import functools
# import os
#
# import flask
#
# from authlib.client import OAuth2Session
# import google.oauth2.credentials
# import googleapiclient.discovery
#
# ACCESS_TOKEN_URI = 'https://www.googleapis.com/oauth2/v4/token'
# AUTHORIZATION_URL = 'https://accounts.google.com/o/oauth2/v2/auth?access_type=offline&prompt=consent'
#
# AUTHORIZATION_SCOPE = 'openid email profile'
#
# AUTH_REDIRECT_URI = os.environ.get("http://localhost:8040/google/auth", default=False)    #comment line
# BASE_URI = os.environ.get("FN_BASE_URI", default=False)                      #comment line
# CLIENT_ID = os.environ.get("313919470376-dhl9qq87macvamgif9fjjnba21cmogva.apps.googleusercontent.com", default=False)
# CLIENT_SECRET = os.environ.get("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", default=False)
#
# AUTH_TOKEN_KEY = 'auth_token'
# AUTH_STATE_KEY = 'auth_state'
#
# app = flask.Blueprint('google_auth', __name__)
#
#
# def is_logged_in():
#     return True if AUTH_TOKEN_KEY in flask.session else False
#
#
# def build_credentials():
#     if not is_logged_in():
#         raise Exception('User must be logged in')
#
#     oauth2_tokens = flask.session[AUTH_TOKEN_KEY]
#
#     return google.oauth2.credentials.Credentials(
#         oauth2_tokens['access_token'],
#         refresh_token=oauth2_tokens['refresh_token'],
#         client_id="313919470376-dhl9qq87macvamgif9fjjnba21cmogva.apps.googleusercontent.com",
#         client_secret="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",
#         token_uri=ACCESS_TOKEN_URI)
#
#
# def get_user_info():
#     credentials = build_credentials()
#
#     oauth2_client = googleapiclient.discovery.build(
#         'oauth2', 'v2',
#         credentials=credentials)
#
#     return oauth2_client.userinfo().get().execute()
#
#
# def no_cache(view):
#     @functools.wraps(view)
#     def no_cache_impl(*args, **kwargs):
#         response = flask.make_response(view(*args, **kwargs))
#         response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
#         response.headers['Pragma'] = 'no-cache'
#         response.headers['Expires'] = '-1'
#         return response
#
#     return functools.update_wrapper(no_cache_impl, view)
#
#
# @app.route('/google/login')
# @no_cache
# def login():
#     session = OAuth2Session("313919470376-dhl9qq87macvamgif9fjjnba21cmogva.apps.googleusercontent.com", "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",
#                             scope=AUTHORIZATION_SCOPE,
#                             redirect_uri="http://localhost:8040/google/auth")
#
#     uri, state = session.authorization_url(AUTHORIZATION_URL)
#
#     flask.session[AUTH_STATE_KEY] = state
#     flask.session.permanent = True
#
#     return flask.redirect(uri, code=302)
#
#
# @app.route('/google/auth')
# @no_cache
# def google_auth_redirect():
#     req_state = flask.request.args.get('state', default=None, type=None)
#
#     if req_state != flask.session[AUTH_STATE_KEY]:
#         response = flask.make_response('Invalid state parameter', 401)
#         return response
#
#     session = OAuth2Session("313919470376-dhl9qq87macvamgif9fjjnba21cmogva.apps.googleusercontent.com", "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",
#                             scope=AUTHORIZATION_SCOPE,
#                             state=flask.session[AUTH_STATE_KEY],
#                             redirect_uri="http://localhost:8040/google/auth")
#
#     oauth2_tokens = session.fetch_access_token(
#         ACCESS_TOKEN_URI,
#         authorization_response=flask.request.url)
#
#     flask.session[AUTH_TOKEN_KEY] = oauth2_tokens
#
#     return flask.redirect(BASE_URI, code=302)
#
#
# @app.route('/google/logout')
# @no_cache
# def logout():
#     flask.session.pop(AUTH_TOKEN_KEY, None)
#     flask.session.pop(AUTH_STATE_KEY, None)
#
#     return flask.redirect(BASE_URI, code=302)

# Google Auth TAKE 2

# def login_is_required(function):  #checks if authorized
#     def wrapper(*args, **kwargs):
#         if "google_id" not in session:
#             return abort(401)
#         else:
#             return function()
#
#     return wrapper
#
#
# @app.route("/login")  #PUT LOGIN PAGE HERE
# def login():
#     authorization_url, state = flow.authorization_url()
#     session["state"] = state
#     return redirect(authorization_url)
#
#
# @app.route("/callback")  #PUT HOME PAGE HERE
# def callback():
#     flow.fetch_token(authorization_response=request.url)
#
#     if not session["state"] == request.args["state"]:
#         abort(500)
#
#     credentials = flow.credentials
#     request_session = requests.session()
#     cached_session = cachecontrol.CacheControl(request_session)
#     token_request = google.auth.transport.requests.Request(session=cached_session)
#
#     id_info = id_token.verify_oauth2_token(
#         id_token=credentials._id_token,
#         request=token_request,
#         audience=GOOGLE_CLIENT_ID
#     )
#
#     session["google_id"] = id_info.get("sub")
#     session["name"] = id_info.get("name")
#     return redirect("/protected_area")  #PUT HOME PAGE HERE
#
#
# @app.route("/logout")  #MAKE A SIMPLE SIGNOUT PAGE?
# def logout():
#     session.clear()
#     return redirect("/")
#
#
# @app.route("/")  #PUT SIGNUP PAGE HERE
# def index():
#     return "you're in <a href='/login'><button>Login</button></a>"
#
#
# @app.route("/protected_area")  #HOME PAGE
# @login_is_required
# def protected_area():
#     return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

# JWT AUTH

from flask import Blueprint, request, Response, jsonify

from ludis.app.routes.utils import validate_user, db_write, generate_hash, validate_user_input, generate_salt

authentication = Blueprint("authentication", __name__)

@authentication.route("/register", methods=["POST"])
def register_user():
    pass

@authentication.route("/login", methods=["POST"])
def login_user():
    pass


def register_user():
    user_email = request.json["email"]
    user_password = request.json["password"]
    user_confirm_password = request.json["confirm_password"]

    if user_password == user_confirm_password and validate_user_input(
        "authentication", email=user_email, password=user_password
    ):
        password_salt = generate_salt()
        password_hash = generate_hash(user_password, password_salt)

        if db_write(
            """INSERT INTO users (email, password_salt, password_hash) VALUES (%s, %s, %s)""",
            (user_email, password_salt, password_hash),
        ):
            # Registration Successful
            return Response(status=201)
        else:
            # Registration Failed
            return Response(status=409)
    else:
        # Registration Failed
        return Response(status=400)

def login_user():
    user_email = request.json["email"]
    user_password = request.json["password"]

    user_token = validate_user(user_email, user_password)

    if user_token:
        return jsonify({"jwt_token": user_token})
    else:
        Response(status=401)