#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jesse
# @Time    : 2021/6/15 13:48
from flask import Blueprint, jsonify

from database.article import Article

blueprint_blog = Blueprint('blueprint_blog', __name__)


@blueprint_blog.route('/bloglist', methods=['GET', 'POST'])
def blog_list():
    data = Article.query.all().order_by('id')
    return jsonify([i.to_dict() for i in data])
