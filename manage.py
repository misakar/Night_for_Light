# coding: utf-8

import sys
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_admin import Admin
# from flask.ext.admin.contrib.sqla import ModelView
from app import app, db
from app.models import Users, Night, Comments


# 编码设置
reload(sys)
sys.setdefaultencoding('utf-8')


manager = Manager(app)
migrate = Migrate(app, db)
admin = Admin(app, name="")


def make_shell_context():
    """自动加载环境"""
    return dict(
        app = app,
        db = db,
        Users = Users,
        Night = Night,
        Comments = Comments
    )


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


# 后台数据库管理界面
# admin.add_view(ModelView([models], db.session))


@manager.command
def test():
    """运行测试"""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def adduser(username):
    from getpass import getpass
    password = getpass('password ')
    confirm = getpass('comfirm ')
    if password == confirm:
        u = Users(
            username = username,
            password = password
        )
        db.session.add(u)
        db.session.commit()
        print "user %s add in database" % username
    else:
        print "password not confirmed"
        sys.exit(0)


if __name__ == '__main__':
    app.debug = True
    manager.run()
