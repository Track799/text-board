# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:41:18 2019

@author: Dell
"""
#
from flask import Flask
#没有flask.ext模块，更改import指令
from flask_sqlalchemy  import SQLAlchemy
#flask.ext改为flask_login, flask.ext.openid改为flask_openid
from flask_login import LoginManager
from flask_migrate import Migrate


#创建Flask和数据库对象
app = Flask(__name__)
#读取配置文件
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#创建登录管理器对象，作为form和database的联系
lm = LoginManager(app)
lm.login_view = 'login'


#记录错误日志，限制日志文件为1M，保留最后20个日志文件作为备份
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/say.log', 'a', 1 * 1024 * 1024, 20)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('say startup')
    
from app import views, models, errors
