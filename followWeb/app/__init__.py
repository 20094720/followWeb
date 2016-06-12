import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,MetaData
from flask_login import LoginManager
from flask_openid import OpenID
from config import SQLALCHEMY_DATABASE_URI,basedir


app = Flask(__name__)
app.config.from_object('config')
ENGINE = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
metadata = MetaData()
metadata.create_all(ENGINE)

lm = LoginManager()
lm.setup_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views
