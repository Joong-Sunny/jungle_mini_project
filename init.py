from pymongo import MongoClient
import hashlib
import datetime
import jwt

client = MongoClient('localhost', 27017)
db = client.dbmini

def init():
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

def install():
    name_list = [
        "길 인식", "윤 종선", "김 기운", "유 수민", "김 승덕", "박 선도", "김 희산", "김 진섭", "김 현진", "김 성태",
        "김 영우", "최 의균", "홍 리경", "오 기윤", "임 지우", "김 채욱", "정 성훈", "윤 연운", "우 수연", "최 준만",
        "홍 창섭", "이 송희", "정 재훈", "박 예린", "조 성배"
    ]
    num = 1
    for i in name_list:
        name_cut = i.split(' ')
        last_hash = hashlib.sha256(name_cut[0].encode('utf-8')).hexdigest()
        doc = {
            'num' : num,
            'firstname' : name_cut[0],
            'lastname' : last_hash
        }
        db.user1.insert_one(doc)
        num += 1

    
install()