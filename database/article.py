import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database.dbConfig import Config

app = Flask(__name__)

# 加载数据库配置对象
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = "article"

    id = db.Column(db.Integer, primary_key=True)  # 整型的主键，会默认设置为自增主键
    title = db.Column(db.String(512))
    time_created = db.Column(db.Integer, default=str(datetime.datetime.now()).split(".")[0])
    tag = db.Column(db.String(512))
    text = db.Column(db.Text)
    desc = db.Column(db.String(512))

    def __repr__(self):
        return f"article id-{self.id} title-{self.title} time_created-{self.time_created} tag-{self.tag} text-{self.text[:10]}"


if __name__ == '__main__':
    pass
