# coding: utf-8
"""
    views.py
    ~~~~~~~~
    夜晚的视图
    /night: 首页: 开始的开始:每一页的链接
    /night/<int:day>: 每一夜
    /night/upload: 上传页面(admin site)
"""

from app import app, db
from app.forms import LoginForm, TonightForm
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from models import Night, Comments, Users


@app.route('/night/')
def index():
    """首页: 首夜"""
    nights = Night.query.all()
    return render_template(
        'index.html',
        nights=nights,
        )


@app.route('/tonight/')
def tonight():
    """
    今夜
    :return: 今夜的图片笔记、日期、自己的一点点评、
        遮罩层显示最新评论、其下显示历史评论
    """
    tonight = Night.query.first()
    if tonight == None:
        photo = "http://7xj431.com1.z0.glb.clouddn.com/20151201_031351.jpg"
    else:
        photo = tonight
    return render_template("tonight.html", photo=photo)

@login_required
@app.route('/create/', methods=["POST", "GET"])
def create():
    """
    sign up tonight
    :return:
    """
    form = TonightForm()
    if form.validate_on_submit():
        tonight = Night(
            url=form.url.data,
            day=form.day.data,
            time=form.time.data,
            tag=form.tag.data,
            author_id=current_user.id
        )
        db.session.add(tonight)
        db.session.commit()
        return redirect(url_for('tonight'))
    return render_template('create.html', form=form)



@app.route('/login/', methods=["POST", "GET"])
def login():
    """登录页面"""
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password:
            login_user(user)
            # use next to redirect
            return redirect(url_for('create'))
        flash("用户名或密码不存在")
    return render_template("login.html", form=form)


@login_required
@app.route('/logout/')
def logout():
    """
    和这个夜晚说再见
    :return:
    """
    logout_user()
    return redirect(url_for('index'))


