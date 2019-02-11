from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from hashlib import pbkdf2_hmac

app = Flask(__name__)

@app.route('/register', methods=('POST'))
def register():
    key = pbkdf2_hmac('sha512', request.form['api'], "", 100)
    email = pbkdf2_hmac('sha512', request.form['email'], "", 100)
