from flask import Flask, request, abort, jsonify, Blueprint, render_template

bp = Blueprint('site', __name__)

@bp.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@bp.route('/register', methods = ['GET'])
@bp.route('/register/', methods = ['GET'])
def register():
    return render_template("register.html")

@bp.route('/docs', methods = ['GET'])
@bp.route('/docs/', methods = ['GET'])
def about():
    return render_template("docs/index.html")

@bp.route('/about', methods = ['GET'])
@bp.route('/about/', methods = ['GET'])
def docs():
    return render_template("about.html")

@bp.route('/docs/add', methods = ['GET'])
@bp.route('/docs/add/', methods = ['GET'])
def docs_add():
    return render_template("docs/add.html")

@bp.route('/docs/register', methods = ['GET'])
@bp.route('/docs/register/', methods = ['GET'])
def docs_register():
    return render_template("docs/register.html")

@bp.route('/docs/retrieve', methods = ['GET'])
@bp.route('/docs/retrieve/', methods = ['GET'])
def docs_retrieve():
    return render_template("docs/retrieve.html")

@bp.route('/docs/delete', methods = ['GET'])
@bp.route('/docs/delete/', methods = ['GET'])
def docs_delete():
    return render_template("docs/delete.html")

@bp.route('/static/js/typewriter/core.js', methods = ['GET'])
def static_typewriter_js():
    return render_template("../static/js/typewriter/core.js")

@bp.route('/static/js/main.js', methods = ['GET'])
def static_main_js():
    return render_template("../static/js/main.js")

@bp.route('/static/js/reg.js', methods = ['GET'])
def static_reg_js():
    return render_template("../static/js/reg.js")