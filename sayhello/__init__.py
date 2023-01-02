from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap4
from flask_moment import Moment


app = Flask("sayhello")
app.config.from_pyfile("settings.py")   # 利用文件来集中管理配置
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap4(app)
moment = Moment(app)

from sayhello import views, errors, commands
