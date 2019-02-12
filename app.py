from flask import Flask, request, abort, jsonify
from pymongo import MongoClient
from datetime import datetime
import random

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.checkmate

with open('dict/nouns.txt') as f:
    nouns = [l.rstrip('\n') for l in f]

with open('dict/verbs.txt') as f:
    verbs = [l.rstrip('\n') for l in f]

with open('dict/adjectives.txt') as f:
    adjectives = [l.rstrip('\n') for l in f]

with open('dict/adverbs.txt') as f:
    adverbs = [l.rstrip('\n') for l in f]

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

print(generate_pin())
print(generate_words())

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
        api = db.api.find_one({
            'key_hash': request.json['key'],
        })
        if api is None:
            abort(400)
        words = generate_words()
        pin = generate_pin()
        db.registry.insert_one({
            'key_hash': request.json['key'],
            'email_hash': request.json['email'],
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

@app.route('/add', methods = ['POST'])
def add():
    if not request.json or not 'key' in request.json:
        db.api.insert_one({
            'key_hash': request.json['key'],
            'date_registered': datetime.now()
        })
        return 200
    else:
        abort(400)