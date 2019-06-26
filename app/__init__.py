from flask import Flask, request, abort, jsonify, Blueprint, render_template

def create_app(test_config=None):

    app = Flask(__name__)

    from . import api
    app.register_blueprint(api.bp)
    
    @app.route('/', methods = ['GET'])
    def index():
        return render_template("index.html")

    return app