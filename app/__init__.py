#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2020/06/10 17:45:26
@Author  :   Du ShiKang 
@Version :   1.0
@Contact :   1103146395@qq.com
@Desc    :   None
'''

# here put the import lib
import os
from flask import Flask

def create_app(test_config=None):
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def hello():
        return 'hello world!'
    return app
