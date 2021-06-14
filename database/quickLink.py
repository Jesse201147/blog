import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database.dbConfig import Config

app = Flask(__name__)

# 加载数据库配置对象
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


class Repo(db.Model):
    __tablename__ = "quickLink"

    id = db.Column(db.Integer, primary_key=True)  # 整型的主键，会默认设置为自增主键
    name = db.Column(db.String(128))
    position = db.Column(db.Integer, default=id)
    url = db.Column(db.String(512))

    def __repr__(self):
        return f"quickLink id-{self.id} name-{self.name} position-{self.position} url-{self.url}"


if __name__ == '__main__':
    pass
    # # 清除数据库里的所有数据
    # db.drop_all()
    # # 创建所有的表
    # db.create_all()
    #
    # update_project_list = [
    #     dict(name="crawler_Python",
    #          local="git@gitee.com:jesse201147/crawler_Python.git",
    #          remote="git@github.com:Jesse201147/crawler_Python.git"),
    #     dict(name="jusheng_wanhe",
    #          local="git@gitee.com:jesse201147/jusheng_wanhe.git",
    #          remote="git@github.com:Jesse201147/jusheng_wanhe.git"),
    # ]
    # for _r in update_project_list:
    #     _repo = Repo(
    #         name=_r.get("name"),
    #         local=_r.get("local"),
    #         remote=_r.get("remote"),
    #         project="test")
    #     db.session.add(_repo)
    # db.session.commit()
    # repos = Repo.query.all()
    # commits = LastCommit.query.all()
    # ids = [i for i in [ir.id for ir in repos] if i not in [ic for ic in commits]]
    # for _id in ids:
    #     _commit = LastCommit(
    #         repo_id=_id,
    #         ref="master",
    #         author_name="unknow",
    #         push_time="unknow",
    #         message="unknow",
    #         sha="unknow"
    #     )
    #     db.session.add(_commit)
    # db.session.commit()
