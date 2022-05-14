from flask import Blueprint, abort

base = Blueprint("base", __name__)

@base.route("/", methods = ['GET'])
def root():
    return '''<h1>Ludis</h1>
<p>Backend server for Ludis. Don't fuck around or else I'll fuck you up.</p>'''