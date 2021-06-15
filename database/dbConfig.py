import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# 配置数据库连接的对象
class Config(object):
    """配置参数"""
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(os.getcwd(), "flask.db")}'
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:53thcn@127.0.0.1:3306'

    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 设置sqlalchemy自动更跟踪数据库（数据库表手动更新是同步跟新到对象）
    SQLALCHEMY_ECHO = True  # 查询时会显示原始SQL语句

