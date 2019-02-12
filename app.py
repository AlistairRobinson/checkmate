from flask import Flask, request, abort
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.checkmate

@app.route('/retrieve', methods = ['POST'])
def retrieve():
    if not request.json or not 'key' in request.json or not 'email' in request.json:
        abort(400)
    else:
        abort(400)

@app.route('/register', methods = ['POST'])
def register():
    if not request.json or not 'key' in request.json or not 'email' in request.json:
        abort(400)
    else:
        abort(400)

@app.route('/register', methods = ['POST'])
def register():
    if not request.json or not 'key' in request.json:
        abort(400)
    else:
        abort(400)