# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:25:00 2019

@author: Dell
"""

#跨站点请求伪造
CSRF_ENABLED = True
SECRET_KEY = 'guess what'

"""
OPENID_PROVIDERS = [
        {'name' : 'QQ', 'url' : 'https://graph.z.qq.com/moc2/me'},
        {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
        ]
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

#配置数据库文件路径和目录
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
