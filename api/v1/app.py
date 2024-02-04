#!/usr/bin/python3
"""A simple Flask server for HBNB project
"""
from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify
import os

host = os.environ.get('HBNB_API_HOST')
port = os.environ.get('HBNB_API_PORT')

app = Flask(__name__)
app.url_map.strict_slashes = False

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(exception):
    """close database after performing opration
    """
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """return 404 if resource not found
    """
    return jsonify({"error": "Not found"})


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)
