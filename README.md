## 环境准备
- python3.6
- pip install -r requirements 
- pygexf模块需手动安装，过程如下：
  - 下载[gexf安装文件压缩包](https://github.com/paulgirard/pygexf)
  - 进入解压后的文件夹根目录，执行**python setup.py install**命令，期间可能会出现报错信息，手动解决错误完成安装。
## 运行方式
- 方式一：直接运行入口函数**discover/app/main.py**
- 方式二：命令行下运行
  - 切换到 /discover 目录下**
    ```
    set FLASK_APP=app
    set FLASK_ENV=development
    flask run
    ```

