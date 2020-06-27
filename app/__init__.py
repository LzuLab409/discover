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
from flask import Flask,jsonify,render_template
import sys

def create_app():
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        UPLOAD_FOLDER=os.getcwd()+os.sep+'app'+os.sep+'static'+os.sep+'data'+os.sep+'file',
        ALLOWED_EXTENSIONS={'txt'},
    )

    # @app.route('/test')
    # def hello():
    #     print(app.config['UPLOAD_FOLDER'])
    #     return '舆情检测系统！！'
    
    app.debug=True

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'),404

    import visual
    app.register_blueprint(visual.bp)

    return app