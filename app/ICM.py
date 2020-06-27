#encoding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
from numpy import zeros,ones, empty
import numpy as np
import os
from numpy import *
def func(filePath):
    '''
        :param: filePath: 固定参数，算法数据集文件路径
        :return: count: 生成图片的个数
    '''
    # path = r'X:\develope\coding\iwhale\discover\app\network\karate-int.txt'
    path=filePath
    G = nx.read_edgelist(path, nodetype=int)

    nodeNum = len(G.nodes())
    print (nodeNum)
    colors = zeros((nodeNum)) #值为0，大小为节点数的一维数组

    # plt.ion()
    for i in range(nodeNum):
        G.node[i]['label'] = i #G的标签值为节点值 
    resultTable=zeros([nodeNum,5]) #值为0，大小为node*5的五维数组

    for i in range(resultTable.shape[0]):
        resultTable[i,0] =  G.node[i]['label']
    k = 5
    print('G.node:{}'.format(G.node))
    #此处可以优化
    nodeDegIdsMat = zeros((nodeNum,2))#matrix of nodes ids and relative degree values 值为0，大小为node*2的二维数组
    for i in range(nodeDegIdsMat.shape[0]):
        nodeDegIdsMat[i,0] = i       # the first column is node ids
        nodeDegIdsMat[i,1] = nx.degree(G,i)     #the second column is nodes degree

    print('nodeDegIdsMat:{}'.format(nodeDegIdsMat))
    orderDegree=nodeDegIdsMat[np.lexsort(-nodeDegIdsMat.T)] #此操作看不懂，但操作后还是个node*2的二维数组，里面值的顺序按照度的大小进行了降序排列
    print('orderDegree:{}'.format(orderDegree))

    tempInput = orderDegree[0:k,0]  #取前5个度最大的节点，值为节点编号
    print(tempInput)

    threshold = 0.2
    activeOrderIndex = np.repeat(None, nodeNum, axis=0) #保存激活节点的内部ID 长度为node，值为None的一维数组
    activeOrderLabel = np.repeat(None, nodeNum, axis=0) #保存激活节点的label

    for i in range(k):
        temp=tempInput[i]
        for j in range(nodeNum):
            if temp == G.node[j]['label']:
                activeOrderIndex[i] = j
                activeOrderLabel[i] = temp
                colors[j] = 1
                resultTable[j,1] = 1
                resultTable[j,4] = 0

    i =0
    orderLength = k
    count=1
    colorList=[]

    while activeOrderIndex[i] !=None:
        nodeID = activeOrderIndex[i]
        for j in range(nodeNum):
            if j in G.neighbors(nodeID) and resultTable[j,1]==0:
                temp = random.random()
                if temp <= threshold:
                    orderLength = orderLength+1
                    activeOrderIndex[orderLength-1] = j
                    activeOrderLabel[orderLength-1] = G.node[j]['label']
                    colors[j] = 2
                    resultTable[j,1] = 1
                    resultTable[j,2] = G.node[nodeID]['label']
                #resultTable[j,3] = temp
                    resT4=resultTable[nodeID,4]
                    resultTable[j,4]=resT4+1.0
        nx.draw_networkx(G, pos= nx.kamada_kawai_layout(G), node_color=colors)
        colorList.append(colors)
        # plt.show()
        save_path=os.getcwd()+os.sep+'app'+os.sep+'static'+os.sep+'data'+os.sep+'img'+os.sep+'%d.jpg'%(count)
        plt.savefig(save_path)
        count+=1

        if i+1 <=orderLength:
            print (activeOrderLabel[i])
            print (activeOrderLabel[i+1:orderLength])
        i = i+1
    print ('Label State activeNode Weight time')
    print (resultTable)
    print (threshold)
    print (orderLength,nodeNum)
    Activerate=float(orderLength)/float(nodeNum)
    print ('The actived vertex number is:',orderLength,',actived rate is :',format(Activerate*100,'.2f'),'%\n')
    print ('The actived node sequence in order is:',activeOrderLabel[0:orderLength])
    print(colorList)
    return count,colorList,G
if __name__ =='__main__':
    path = r'X:\develope\coding\iwhale\discover\app\network\karate-int.txt'
    count,colorList,G=func(path)

    for i in range(len(colorList)):
        nx.draw_networkx(G, pos= nx.kamada_kawai_layout(G), node_color=colorList[i])
        plt.show()