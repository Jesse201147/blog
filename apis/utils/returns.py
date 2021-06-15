#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Jesse
# @Time    : 2021/6/15 16:58
from django.http import JsonResponse
import json


def return_succeed(msg="", data=""):
    return JsonResponse(dict(code=1, msg=msg, data=data))


def return_fail(msg="", data=""):
    return JsonResponse(dict(code=-1, msg=msg, data=data),)
