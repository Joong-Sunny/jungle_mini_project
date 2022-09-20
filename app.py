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

ran_num = random.randrange(1,3)
print(ran_num)
student_data = {
    1: {"first_name": "인식", "last_name": "길"},
    2: {"first_name": "중선", "last_name": "윤"}
}


@app.route('/')
def index():
    return render_template("index.html",
        template_first_name = student_data[ran_num]["first_name"],
        template_last_name = student_data[ran_num]["last_name"])

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
            'id' : first_name_receive,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=5)
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



if __name__ == '__main__':
    app.run(debug=True)