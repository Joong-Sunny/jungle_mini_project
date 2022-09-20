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
        "길 인식", "윤 중선", "김 기운", "유 수민", "김 승덕", "박 선도", "김 희산", "김 진섭", "김 현진", "김 성태",
        "김 영우", "최 의균", "홍 리경", "오 기윤", "임 지우", "김 채욱", "정 성훈", "윤 영운", "우 수연", "최 준만",
        "홍 창섭", "이 송희", "정 재훈", "박 예린", "조 성배"
    ]
    url = [
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042TNJPM7D-1f754fb89dbd-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U043HGVNYG0-0e138ac4c550-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042TNJUFJP-63c9380f4514-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U043HGW0HJ4-0521232ce622-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042W9AJG2G-b26d79eedcb6-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042TRPHL0J-6a380eef1014-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042TRPCUSE-2f79bdbb391d-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U043HGW0VC0-05042554f81c-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U043HGVP9B2-3b51aa83b5a2-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042TR8D1PV-2e4d30451244-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042QSPBEUD-413241b1c9c5-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042W9AJULU-4d29a9ce24b5-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042W9AA43E-03a36cef2b92-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042QSPEZLM-fedd11412751-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U043HGW19QQ-da4fa3dd4f6d-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042D951K7Z-350027b626c7-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042TRPA5U2-867945fabab9-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U0436EQ98RX-bc09a7219ed0-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042D94TVL7-0933b052c65b-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042M7KDJCE-f8ec8a7797ab-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042W9AF0A0-0b610ab5e5a9-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U043HGVS0PJ-70fcaec56d38-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042QSPELDB-055fe14122f8-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U042TNJLVPD-cd84856a7089-512",
        "https://ca.slack-edge.com/T01FZU4LB4Y-U0436EQ6A8Z-7a3a807e3afe-512"
    ]
    num = 1
    for i in name_list:
        name_cut = i.split(' ')
        last_hash = hashlib.sha256(name_cut[0].encode('utf-8')).hexdigest()
        doc = {
            'num' : num,
            'firstname' : name_cut[1],
            'lastname' : last_hash,
            'url' : url[num-1]
        }
        db.user1.insert_one(doc)
        num += 1

    
install()

