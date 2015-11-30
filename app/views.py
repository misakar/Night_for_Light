# coding: utf-8
"""
    views.py
    ~~~~~~~~
    夜晚的视图
    /night: 首页: 开始的开始:每一页的链接
    /night/<int:day>: 每一夜
    /night/upload: 上传页面(admin site)
"""

from app import app
from flask import render_template
from models import Night, Comments, Users


@app.route('/night')
def index():
    """首页: 今夜"""
    nights = Night.query.all()
    return render_template(
        'index.html',
        nights=nights,
        )


# @app.route('/night/<int:day>')
