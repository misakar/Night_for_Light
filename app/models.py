# coding: utf-8
"""
    models.py
    ~~~~~~~~~

        数据库文件

        class: Night
        class: Comments
        class: Author
"""
from . import db
from datetime import datetime


class Night(db.Model):
    """
    每一夜:
    时间地点最是重要,还有那一点点新晴
    """
    __tablename__ = 'nights'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(164))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    url = db.Column(db.String(200))
    comments = db.relationship('Comments', backref='nights', lazy='dynamic')
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return "this is %r night..." % self.title


class Users(db.Model):
    """
    作者,用户
    just for me
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(164))
    password_hash = db.Column(db.String(128))
    nights = db.relationship('Night', backref='users', lazy='dynamic')
    comments = db.relationship('Comments', backref='users', lazy='dynamic')

    # deal with password hash
    @property
    def password(self):
        raise AttributeError('已加密，不是可读形式!')

    @password.setter  # @property生成setter装饰器,限定password
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "this is %r" % self.username


class Comments(db.Model):
    """
    评论: 自己对自己的点评
    或许是个遮罩层(最新)
    """
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    night_id = db.Column(db.Integer, db.ForeignKey('nights.id'))

    def __repr__():
        return "just a comment!"
