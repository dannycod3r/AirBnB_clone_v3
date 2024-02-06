#!/usr/bin/python3
"""A simple Flask server for HBNB project
"""
from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify, make_response
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.url_map.strict_slashes = False

# configure CORS for flask
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_db(exception):
    """close database after performing opration
    """
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """return 404 if resource not found
    """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':

    host = os.environ.get('HBNB_API_HOST')
    port = os.environ.get('HBNB_API_PORT')

    app.run(host=host, port=port, threaded=True)
