from flask import flash, render_template, request, url_for 

from application import app
from application import auth
from application import db
from application import scrap
from application.models import User, Role

@app.route('/')
def top_page():
    title = 'ようこそ日本語!!'
    msg = 'TEST 一覧ページ'
    return render_template('index.html', title = title, msg = msg)

@app.route('/list')
def show_list():
    title = "はてな人気リスト"
    results = scrap.get_hatena_entries('https://b.hatena.ne.jp/hotentry/it')
    # URLを変更すれば別ジャンルも取得できます。
    # results = scrap.get_hatena_entries('https://b.hatena.ne.jp/hotentry/life') 
    return render_template('list.html', title = title, results = results)

@app.route('/user-list')
def show_users():
    title = '登録済み会員'
    users = User.query.all()
    return render_template('user-list.html', title = title, users = users)

@app.route('/new-user')
def new_user():
    title = '新規登録'
    roles = Role.query.all()
    return render_template('new-user.html', title = title, roles = roles)

@app.route('/create-user', methods=['POST'])
def create_user():
    title = '登録完了'
    password =  request.form['password']
    salt = auth.create_salt()
    hash_password = auth.create_hash(password, salt)
    email = request.form['email']
    user = User(
        name = request.form['name'],
        password = hash_password,
        email = email,
        role_id = request.form['role'],
        salt = salt
    ) 
    email_exist = User.query.filter_by(email=email).first()
    if email_exist is None:
        db.session.add(user) 
        db.session.commit()
        flash('登録を完了しました。')
        users = User.query.all()
        return render_template('user-list.html', title = title, users = users)
    else:
        title = '登録エラー'
        msg = 'すでに登録済みです。'
        return render_template('error.html', title = title, message = msg)
