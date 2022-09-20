from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
import random
import hashlib
import datetime
import jwt

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbmini

SECRET_KEY = 'SPARTA'

@app.route('/')
def index():
    ran_num = random.randrange(1,26)
    member = db.user.find_one({'num':ran_num})
    return render_template("index.html",
        template_first_name = member["firstname"],
        template_last_name = member["lastname"],
        template_url = member["url"])

@app.route('/api/login', methods=['POST'])
def api_login():
    first_name_receive = request.form['first_name_give']
    last_name_receive = request.form['last_name_give']

    pw_hash = hashlib.sha256(last_name_receive.encode('utf-8')).hexdigest()
    result = db.user.find_one({'firstname':first_name_receive, 'lastname':pw_hash})

    print(first_name_receive)
    print(last_name_receive)
    print(pw_hash)
    print(result)

    if result is not None:
        payload = {
            'id': first_name_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        print(token)
        
        return jsonify({'result':'success', 'token':token})
    else:
        return jsonify({'result':'fail', 'msg':'아이디/비밀번호가 일치하지 않습니다.'})

@app.route('/main')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        print(token_receive)
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})
        return render_template("main.html")
    except jwt.ExpiredSignatureError:
        return redirect(url_for("index", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("index", msg="로그인 정보가 존재하지 않습니다."))

#save comments to DB
@app.route('/api/comments', methods=['POST'])
def submitComment():
    comment_receive = request.form['comment_give']
    store_receive = request.form['store_name']
    comment_push = {'store_name': store_receive, 'comment':comment_receive}
    db.comments.insert_one(comment_push)
    return jsonify({'result': 'success', 'msg': str(comment_push) + "db에 저장되었습니다!"})

if __name__ == '__main__':
    app.run(debug=True)
