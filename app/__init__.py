from flask import Flask, request, abort, jsonify, Blueprint

def create_app(test_config=None):

    app = Flask(__name__)

    from . import api
    app.register_blueprint(api.bp)
    
    return app