from pymongo import MongoClient
import hashlib
import datetime
import jwt

client = MongoClient('localhost', 27017)
db = client.dbmini

lastname = "길"
last_hash = hashlib.sha256(lastname.encode('utf-8')).hexdigest()
doc = {
    'num' : 1,
    'firstname' : '인식',
    'lastname' : last_hash
    }
db.user.insert_one(doc)

lastname = "윤"
last_hash = hashlib.sha256(lastname.encode('utf-8')).hexdigest()
doc = {
    'num' : 2,
    'firstname' : '중선',
    'lastname' : last_hash
    }
db.user.insert_one(doc)