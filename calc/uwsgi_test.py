#!/usr/bin/python
# -*- coding=UTF-8 -*-
# trickysky
# 2016/11/3


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["Hello World"]
