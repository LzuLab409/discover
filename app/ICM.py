#encoding:utf-8
import random
import copy
import math
import networkx as nx
#ICM传播模型
#已经被激活的当前时刻的节点列表：  nowActivedNodes = noAN
#已经被激活的当前时刻的节点 的单个非激活邻居节点: nodeN
#已经被选定为种子节点：A
#传播概率：p
def ICM(G,A,p) :
    noAN = copy.deepcopy(A)
    for node in noAN:
        for nodeN in list(G[node]):
            if nodeN not in noAN:
                num = random.random()
                edgeCount = G.number_of_edges(node,nodeN)
                pp = 1-math.pow((1-p),edgeCount)
                if num < pp:
                    noAN.append(nodeN)
    return list(noAN)


