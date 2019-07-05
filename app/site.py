from flask import Flask, request, abort, jsonify, Blueprint, render_template

bp = Blueprint('site', __name__)

@bp.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@bp.route('/register', methods = ['GET'])
def register():
    return render_template("register.html")

@bp.route('/docs', methods = ['GET'])
def docs():
    return render_template("docs/index.html")

@bp.route('/docs/add', methods = ['GET'])
def docs_add():
    return render_template("docs/add.html")

@bp.route('/docs/register', methods = ['GET'])
def docs_register():
    return render_template("docs/register.html")