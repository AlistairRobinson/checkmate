from flask import Flask, request, abort, jsonify, Blueprint
from pymongo import MongoClient
from datetime import datetime
from hashlib import pbkdf2_hmac
import random
import secrets
import binascii

with open('secret/dbpass.txt') as f:
    dbpass = [l.rstrip('\n') for l in f]
    dbpass = dbpass[0]

client = MongoClient('mongodb+srv://alistair:' + dbpass + '@checkmate-kyna9.azure.mongodb.net/test?retryWrites=true&w=majority')
db = client.Checkmate

with open('dict/nouns.txt') as f:
    nouns = [l.rstrip('\n') for l in f]

with open('dict/verbs.txt') as f:
    verbs = [l.rstrip('\n') for l in f]

with open('dict/adjectives.txt') as f:
    adjectives = [l.rstrip('\n') for l in f]

with open('dict/adverbs.txt') as f:
    adverbs = [l.rstrip('\n') for l in f]

with open('secret/salt.txt') as f:
    key_salt = [l.rstrip('\n') for l in f]
    key_salt = key_salt[0]

def generate_pin():
    random.seed(datetime.now())
    return ''.join(map(str, random.sample(range(10), 4)))

def generate_words():
    random.seed(datetime.now())
    case_of = {
        1: [random.choice(nouns), random.choice(verbs), random.choice(nouns)],
        2: [random.choice(nouns), random.choice(verbs), random.choice(adverbs)],
        3: [random.choice(adjectives), random.choice(nouns), random.choice(verbs)],
        4: [random.choice(verbs), random.choice(nouns), random.choice(adverbs)],
        5: [random.choice(adverbs), random.choice(verbs), random.choice(nouns)],
        6: [random.choice(adjectives), random.choice(adjectives), random.choice(nouns)],
        7: [random.choice(adverbs), random.choice(nouns), random.choice(verbs)]
    }
    return case_of.get(random.randint(1, 7))

def generate_key():
    return secrets.token_urlsafe(64)

def hash(password, salt):
    return binascii.b2a_base64(pbkdf2_hmac('sha512', password.encode(), salt.encode(), 2048))

bp = Blueprint('api', __name__)

@bp.route('/retrieve', methods = ['POST'])
def retrieve():
    if not request.json or not 'key' in request.json or not 'email' in request.json:
        abort(400)
    else:
        api = db.api.find_one({
            'key_hash': hash(request.json['key'], key_salt)
        })
        if api is None:
            abort(400)
        salt = api['api_salt']
        user = db.registry.find_one({
            'key_hash': hash(request.json['key'], key_salt),
            'email_hash': hash(request.json['email'].lower(), salt)
        })
        if user is None:
            abort(400)
        return jsonify({
            'w1': user['w1'],
            'w2': user['w2'],
            'w3': user['w3'],
            'pin': user['pin']
        }), 200

@bp.route('/register', methods = ['POST'])
def register():
    if not request.json or not 'key' in request.json or not 'email' in request.json:
        abort(400)
    else:
        api = db.api.find_one({
            'key_hash': hash(request.json['key'], key_salt)
        })
        if api is None:
            abort(403)
        user = db.registry.find_one({
            'key_hash': hash(request.json['key'], key_salt),
            'email_hash': hash(request.json['email'].lower(), salt)
        })
        if user is not None:
            abort(400)
        salt = api['api_salt']
        words = generate_words()
        pin = generate_pin()
        db.registry.insert_one({
            'key_hash': hash(request.json['key'], key_salt),
            'email_hash': hash(request.json['email'].lower(), salt),
            'w1': words[0],
            'w2': words[1],
            'w3': words[2],
            'pin': pin
        })
        return jsonify({
            'w1': words[0],
            'w2': words[1],
            'w3': words[2],
            'pin': pin
        }), 200

@bp.route('/add', methods = ['POST'])
def add():
    if not request.json or not 'email' in request.json:
        abort(400)
    else:
        api = db.api.find_one({
            'api_email': request.json['email']
        })
        if api is not None:
            abort(400)
        key = generate_key()
        db.api.insert_one({
            'api_email': request.json['email'],
            'key_hash': hash(key, key_salt),
            'api_salt': generate_key(),
            'date_registered': datetime.now()
        })
        return jsonify({
            'key': key
        }), 200

@bp.route('/showcase', methods = ['POST'])
def showcase():
    words = generate_words()
    pin = generate_pin()
    return jsonify({
        'w1': words[0],
        'w2': words[1],
        'w3': words[2],
        'pin': pin
    }), 200

@bp.route('/delete', methods = ['POST'])
def delete():
    if not request.json or not 'key' in request.json or not 'email' in request.json:
        abort(400)
    else:
        api = db.api.find_one({
            'key_hash': hash(request.json['key'], key_salt)
        })
        if api is None:
            abort(403)
        user = db.registry.find_one({
            'email_hash': hash(request.json['email'].lower(), api['api_salt'])
        })
        if user is None:
            abort(400)
        db.registry.remove({
            'email_hash': hash(request.json['email'].lower(), api['api_salt'])
        })
        return jsonify({
            'email': request.json['email']
        }), 200