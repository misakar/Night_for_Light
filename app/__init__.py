# coding: utf-8
"""
    night for light
    ~~~~~~~~~~~~~~~

      a personal website: just for me and night
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config


app = Flask(__name__)


app.config.from_object(config['default'])


db = SQLAlchemy(app)


from . import views, models, forms
