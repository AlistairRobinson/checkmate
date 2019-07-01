from pymongo import MongoClient

with open('secret/dbpass.txt') as f:
    dbpass = [l.rstrip('\n') for l in f]
    dbpass = dbpass[0]

with open('secret/sitekey.txt') as f:
    sitekeypass = [l.rstrip('\n') for l in f]
    sitekeypass = sitekeypass[0]

client = MongoClient('mongodb+srv://alistair:' + dbpass + '@checkmate-kyna9.azure.mongodb.net/test?retryWrites=true&w=majority')
db = client.Checkmate

def apis():
    return db.api.count()

def accounts():
    return db.registry.count()

def sitekey():
    return sitekeypass