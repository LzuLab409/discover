#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   2xml.py
@Time    :   2020/06/27 21:30:51
@Author  :   Du ShiKang 
@Version :   1.0
@Contact :   1103146395@qq.com
@Desc    :   None
'''

# here put the import lib
import sys,pprint,os
from gexf import Gexf
import faker

def generateXml(G,layers):
    gexf = Gexf("lzu.edu","network based on IPv6")
    graph=gexf.addGraph("undirected","static","network based on IPv6")
    
    # atr1 = graph.addNodeAttribute('ip address',type='string',defaultValue='true')
    atr1=graph.addNodeAttribute(force_id='modularity_class',title='Modularity Class',type='integer')
    
    f=faker.Faker(locale='zh-CN')
    print('ipv6:{}'.format(f.ipv6()))

    nodes=list(G.nodes)
    edges=list(G.edges)
    print('nodes:{}'.format(nodes))
    print('edges:{}'.format(edges))

    activate_nodes=[]
    for i in range(len(layers)):
        for j in range(len(layers[i])):
            activate_nodes.append(layers[i][j])

    for i in range(len(nodes)):
        tmp=graph.addNode(nodes[i],f.ipv6())
        attribute_flag=0
        for j in range(len(layers)):
            if nodes[i] in layers[j]:
                attribute_flag=j+1
                break
        tmp.addAttribute(atr1,str(attribute_flag))
    for i in range(len(edges)):
        graph.addEdge(str(i),str(edges[i][0]),str(edges[i][1]))
    # tmp = graph.addNode("0","Gephi")
    # tmp.addAttribute(atr1,"http://gephi.org")
    # tmp = graph.addNode("1","Webatlas")
    # tmp.addAttribute(atr1,"http://webatlas.fr")
    # tmp = graph.addNode("2","RTGI")
    # tmp.addAttribute(atr1,"http://rtgi.fr")
    # tmp = graph.addNode("3","BarabasiLab")
    # tmp.addAttribute(atr1,"http://barabasilab.com")
    
    # graph.addEdge("0","0","1",weight='1')
    # graph.addEdge("1","0","2",weight='1')
    # graph.addEdge("2","1","0",weight='1')
    # graph.addEdge("3","2","1",weight='1')
    # graph.addEdge("4","0","3",weight='1')
    
    xml_file=os.getcwd()+os.sep+'app'+os.sep+'static'+os.sep+'data'+os.sep+'xml'+os.sep+'data.xml'
    output_file=open(xml_file,"wb")
    gexf.write(output_file)
