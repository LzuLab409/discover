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

# @bp.route('/getAlgorithm')
# def get_algorithm():
#     algorithm=['ICM算法','算法二','算法三','算法四']
#     return jsonify(algorithm)

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
    
    result={'staus':True,'msg':'文件上传成功'}
    if file and allowed_file(file.filename):
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return jsonify(result) 
    else:
        result['status']=False
        result['msg']='所上传文件类型不符合要求'
        return jsonify(result)

@bp.route('/submit',methods=['POST'])
def submit():
    result={'msg':'sucess','imgPath':''}
    try:
        algorithm=request.form['algorithm']
        filename=request.form['filename']
        print(algorithm)
        print(filename)
        #调用相应算法
        result['imgPath']='static/img/icon-01.png'
        return jsonify(result)
    except KeyError:
        result['msg']='get key error'
        return jsonify(result)








