from flask import Flask, request, abort, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.checkmate

@app.route('/retrieve', methods = ['POST'])
def retrieve():
    if not request.json or not 'key' in request.json or not 'email' in request.json:
        abort(400)
    else:
        user = db.registry.find_one({
            'key_hash': request.json['key'],
            'email_hash': request.json['email']
        })
        if user is None:
            abort(400)
        return jsonify({
            'w1': user['w1'],
            'w2': user['w2'],
            'w3': user['w3'],
            'pin': user['pin']
        }), 200

@app.route('/register', methods = ['POST'])
def register():
    if not request.json or not 'key' in request.json or not 'email' in request.json:
        abort(400)
    else:
        abort(400)

@app.route('/add', methods = ['POST'])
def add():
    if not request.json or not 'key' in request.json:
        abort(400)
    else:
        abort(400)