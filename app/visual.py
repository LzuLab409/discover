#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   visual.py
@Time    :   2020/06/10 18:45:33
@Author  :   Du ShiKang 
@Version :   1.0
@Contact :   1103146395@qq.com
@Desc    :   可视化模块
'''

# here put the import lib
import os
import functools
from flask import(
    Blueprint,flash,g,redirect,render_template,request,session,url_for,jsonify,current_app as app
)
from werkzeug.utils import secure_filename

bp=Blueprint('visual',__name__)

@bp.route('/')
def data_visual():
    return render_template('index.html')

@bp.route('/getAlgorithm')
def get_algorithm():
    algorithm=['ICM算法','算法二','算法三','算法四']
    return jsonify(algorithm)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@bp.route('/uploadData',methods=['POST'])
def upload_data():
    print('load data')
    if 'file' not in request.files:
        flash('no file part')
        return redirect(request.url)
    file=request.files['file']

    if file.filename=='':
        flash('no selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        result={'staus':True,'msg':'保存成功'}
        return jsonify(result) 

@bp.route('/submit',methods=['POST'])
def submit():
    try:
        algorithm=request.form['algorithm']
    except KeyError:
        return 'get key error'
    # file_path=
    print(algorithm)
    return '此处return算法运行生成图片的path，在前端ajax方法内实现局部刷新可视化'







