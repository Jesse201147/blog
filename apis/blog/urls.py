#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jesse
# @Time    : 2021/6/15 15:49
from django.urls import path, include
from blog.views import get_article_list, get_article

app_name = "blog"

urlpatterns = [
    path('articles/', get_article_list, name="articles"),
    path('article/<int:article_id>', get_article, name="article")
]
