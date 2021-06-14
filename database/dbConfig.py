import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 配置数据库连接的对象
class Config(object):
    """配置参数"""
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(os.getcwd(), "flask.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 设置sqlalchemy自动更跟踪数据库（数据库表手动更新是同步跟新到对象）
    SQLALCHEMY_ECHO = True  # 查询时会显示原始SQL语句


app = Flask(__name__)

# 加载数据库配置对象
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


def init_database():
    # 清除数据库里的所有数据
    db.drop_all()
    # 创建所有的表
    db.create_all()
