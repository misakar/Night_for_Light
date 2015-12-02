# coding: utf-8

"""
    form.py
    ~~~~~~
    不设登录,只登录管理后台

    网站只是夜晚的缩影~~复之以图片
"""

from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import Required


class LoginForm(Form):
    """登录表单"""
    username = StringField('用户名', validators=[Required()])
    password = PasswordField('密码', validators=[Required()])
    submit = SubmitField('登录')


class TonightForm(Form):
    """每夜上传表单"""
    url = StringField('url', validators=[Required()])
    day = StringField('day', validators=[Required()])
    time = StringField('time', validators=[Required()])
    tag = StringField('tag', validators=[Required()])
