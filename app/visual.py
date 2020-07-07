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
import logging
from nose.tools import *
from networkx import *
from linear_threshold import *
from ICM import *
import time
import numpy as np
import copy

bp=Blueprint('visual',__name__)

@bp.route('/')
def data_visual():
    return render_template('index.html')

def allowed_file(filename):
    '''check the type of upload file
    '''
    return '.' in filename and filename.rsplit('.',1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def excuteLT(sweed,file):
    '''the function used for running LT model
    :param sweed: 影响力传播种子节点
    :param file: 网络节点文件
    :return G: graph
    :return layers:激活的节点
    '''
    if ',' in sweed:
        sweed=sweed.split(',')
    else:
        sweed=sweed.split('，')
    sweed=list(map(int,sweed))

    start=time.clock()
    G = nx.read_edgelist(file, nodetype=int)
    # datasets=[]
    # f=open(file,"r")        #读取文件数据（边的数据）
    # data=f.read()
    # rows=data.split('\n')
    # for row in rows:
    #   split_row=row.split('\t')
    #   name=(int(split_row[0]),int(split_row[1]))
    #   datasets.append(name)            #将边的数据以元组的形式存放到列表中

    # G=networkx.DiGraph()               #建立一个空的有向图G
    # G.add_edges_from(datasets)         #向有向图G中添加边的数据列表
    layers=linear_threshold(G,sweed,5)     #调用LT线性阈值算法，返回子节点集和该子节点集的最大激活节点集
    del layers[-1]
    length=0
    for i in range(len(layers)):
        length =length+len(layers[i])
    lengths=length-len(layers[0])       #获得子节点的激活节点的个数（长度）
    end=time.clock()
    #测试数据输出结果
    print(layers)  #[[25], [33, 3, 6, 8, 55, 80, 50, 19, 54, 23, 75, 28, 29, 30, 35]]
    print(lengths) #15
    print('Running time: %s Seconds'%(end-start))  #输出代码运行时间
    return G,layers

def excuteIC(sweed,filePath):
    if ',' in sweed:
        sweed=sweed.split(',')
    else:
        sweed=sweed.split('，')
    sweed=list(map(int,sweed))    
    G = nx.read_edgelist(filePath, nodetype=int)
    layers=ICM(G,sweed,p=0.7)
    print('layers:{}'.format(layers))
    return G,layers

def generateXml(G,layers):
    '''generat the relation of the graph 弃用该方法
    :param G: graph
    :param layers: 激活的节点
    '''
    file=os.getcwd()+os.sep+'app'+os.sep+'static'+os.sep+'data'+os.sep+'xml'+os.sep+'data.xml'
    print(layers)
    attrs={}
    for i in range(len(layers)):
        for j in range(len(layers[i])):
            attrs['modularity_class'][layers[i][j]]={'Modularity Class':i}
    print(attrs)
    networkx.set_node_attributes(G,)
    networkx.set_node_attributes(G,attrs)
    networkx.write_gexf(G,file)
    pass

@bp.route('/uploadData',methods=['POST'])
def upload_data():
    '''file upload
    :param request: request里应包含所上传的文件流
    '''
    result={'staus':True,'msg':'文件上传成功'}
    if 'file' not in request.files:
        flash('no file part')
        return redirect(request.url)
    file=request.files['file']
    if file.filename=='':
        flash('no selected file')
        return redirect(request.url)
    # file=request.files.get('file')
    # print(file.name)
    if file and allowed_file(file.filename):
        filename=secure_filename(file.filename)
        try:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return jsonify(result) 
        except IOError as e:
            result['status']=False
            result['msg']='保存文件出错'
            return jsonify(result)
    else:
        result['status']=False
        result['msg']='所上传文件类型不符合要求'
        return jsonify(result)
    return jsonify(result)

@bp.route('/submit',methods=['POST'])
def submit():
    '''execute the selected algorithm
    :param algorithm: 算法
    :param seedNode: 种子节点集
    '''
    result={'status':'True','msg':'sucess'}
    try:
        algorithm=request.form['algorithm']
        filename=request.form['filename']
        nodes=request.form['nodes']
        if not bool(algorithm) or not bool(filename) or not bool(nodes):
            result['status']=False
            result['msg']='缺少必要参数'
        else:
            filePath=os.path.join(app.config['UPLOAD_FOLDER'],filename)
            filePath=r'%s'%filePath
            if algorithm =='LT':
                logging.info('LT Model starting...')
                G,layers=excuteLT(nodes,filePath)
                result['layers']=layers
                result['type']=len(layers)
                if len(layers)==1:
                    result['msg']='选择的种子节点未激活网络中任何其他节点'
                else:
                    try:
                        import toXml as toXml
                        toXml.generateXml(G,layers)
                        result['msg']='选择的种子节点所激活网络中的其他节点已用不同类别标识'
                    except IOError as e:
                        result['status']=False
                        result['msg']=e
            elif algorithm == 'IC':
                G,layers=excuteIC(nodes,filePath)
                if ',' in nodes:
                    nodes=nodes.split(',')
                else:
                    nodes=nodes.split('，')
                nodes=list(map(int,nodes)) 
                ly=[]
                temp=copy.deepcopy(layers)
                for i in range(len(layers)):
                    if layers[i] in nodes:
                        del temp[i]
                ly.append(nodes) 
                ly.append(temp)
                result['layers']=ly
                result['type']=len(ly)
                if len(ly)==1:
                    result['msg']='选择的种子节点未激活网络中任何其他节点'
                else:
                    try:
                        import toXml as toXml
                        toXml.generateXml(G,ly)
                        result['msg']='选择的种子节点所激活网络中的其他节点已用不同类别标识'
                    except IOError as e:
                        result['status']=False
                        result['msg']=e
            else:
                result['msg']='error: 算法开发中，暂不支持所选择的算法'
        return jsonify(result)
    except KeyError:
        result['msg']='get key error'
        return jsonify(result)








