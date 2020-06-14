#encoding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
from numpy import zeros,ones, empty
import numpy as np
import os
from numpy import *

def func(filepath):
    '''
        :params filepath:默认不对路径字符串进行转义
        :return: 返回生成的图片数
    '''
    path = filepath
    G = nx.read_edgelist(path, nodetype=int)
# nodeNum1 = len(G.nodes())
# if min(G.node())!=0:
#     for i in range(1,nodeNum1+1):
#         G.node[i] = i-1
# print G.node()
    nodeNum = len(G.nodes())
    print (nodeNum)
    colors = zeros((nodeNum))
    plt.ion()
    for i in range(nodeNum):
        G.node[i]['label'] = i
    resultTable=zeros([nodeNum,5])

    for i in range(resultTable.shape[0]):
        resultTable[i,0] =  G.node[i]['label']
    k = 5

    nodeDegIdsMat = zeros((nodeNum,2))#matrix of nodes ids and relative degree values
    for i in range(nodeDegIdsMat.shape[0]):
        nodeDegIdsMat[i,0] = i       # the first column is node ids
        nodeDegIdsMat[i,1] = nx.degree(G,i)     #the second column is nodes degree

    orderDegree=nodeDegIdsMat[np.lexsort(-nodeDegIdsMat.T)]

    tempInput =0
    tempInput = orderDegree[0:k,0]
# print tempInput

    threshold = 0.2
    activeOrderIndex = np.repeat(None, nodeNum, axis=0) #保存激活节点的内部ID
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
    #index=1
    z = -1
    count=0
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
        # plt.show()
        #name="demo{}.jps".format(index)
        
        #plt.savefig("static/img/%d.jpg"%(i+1))
        #current_path=os.path.join("static/img/demo{}.png".format(index))
        #print(str(current_path))
        #plt.savefig(current_path)
        
        if z != -2:
            z += 1 
            #plt.pause(1)
            #plt.close()
        #plt.savefig("app/static/img/k.jpg")
        plt.savefig("app/static/img/%d.jpg"%(z+1))
        if i+1 <=orderLength:
            print (activeOrderLabel[i])
            print (activeOrderLabel[i+1:orderLength])
        i = i+1
        count+=1
        #return demo,
    print ('Label State activeNode Weight time')
    print (resultTable)
    print (threshold)
    print (orderLength,nodeNum)
    Activerate=float(orderLength)/float(nodeNum)
    print ('The actived vertex number is:',orderLength,',actived rate is :',format(Activerate*100,'.2f'),'%\n')
    print ('The actived node sequence in order is:',activeOrderLabel[0:orderLength])
    return count
# if __name__ =='__main__':
    # func('X://develope//coding//iwhale//discover//app//network//karate-int.txt')
#nx.draw_networkx(G, node_color=colors)
#plt.show()
    # file='X:\develope\coding\iwhale\data\karate-int.txt'
    # filePath=r'%s'%file
    # print(filePath)