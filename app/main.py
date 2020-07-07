#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2020/06/10 18:56:08
@Author  :   Du ShiKang 
@Version :   1.0
@Contact :   1103146395@qq.com
@Desc    :   None
'''

# here put the import lib
from __init__ import create_app

if __name__=='__main__':
    app=create_app()
    # app.run()
    app.run(host='0.0.0.0',port=80)
    
    

