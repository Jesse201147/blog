#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jesse
# @Time    : 2021/6/15 13:23

from flask import jsonify

from blueprint import blueprint_blog
from database import app, db, Article

# db = SQLAlchemy(app)
app.register_blueprint(blueprint_blog)
db.drop_all()
db.create_all()


# migrate = Migrate(app, db)
@app.route('/bloglist', methods=['GET', 'POST'])
def blog_list():
    data = Article.query.all().order_by('id')
    return jsonify([i.to_dict() for i in data])


if __name__ == '__main__':
    app.run()
    """
    set FLASK_APP=startup.py && flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    """
