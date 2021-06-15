#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jesse
# @Time    : 2021/6/15 14:40
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from database.dbConfig import Config
from database.article import Article

app = Flask(__name__)

# 加载数据库配置对象
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)
