# Hey-PyQt5
Learning awesome PyQt5

## What is PyQT
PyQt 是一个用于创建 GUI 应用程序的跨平台的工具包，它将最强大的 GUI 库 Qt, 和 Python 编程语言融合在一起。PyQt 可以运行在所有主流的操作系统上，包括 Windows, Mac OS, Linux, UNIX

## How to install

#### 1. install Python 3.6  
目前 Python3.6 应该是最成熟稳定的版本，Python [官网](https://www.python.org/downloads/)下载安装  
#### 2. install PyQt5
选择 PyQt5 而不选择 PyQt4 的道理，与安装 Python3 而不选择 Python2 的道理一样，官方逐渐停止对老版本 PyQt4 的维护  
命令行输入
> pip install PyQt5

在国内可以使用以下命令代替，采用豆瓣镜像源加快下载安装速度  

> pip install PyQt5 -i https://pypi.douban.com/simple  
#### 3. install PyQt5 tools
为了使用图形界面开发工具 Qt Designer 等，还需要安装常用的 QT 工具
> pip install PyQt5-tools  

在国内可以使用以下命令代替，采用豆瓣镜像源加快下载安装速度  

> pip install PyQt5-tools -i https://pypi.douban.com/simple  
#### 4. add system PATH
pip 命令执行完成后，PyQt5 工具安装在 X:\XXX\Python3_6_4\Lib\site-packages\pyqt5-tools 下，添加到系统环境变量中  

#### 5. install QScintilla
> pip install QScintilla -i https://pypi.douban.com/simple  

在安装 Eric6 前先安装 QScintilla, 否则会报错 ‘cannot import 那么‘Qsci’’  

#### 6. install Eric6
Eric6 是 Python 写的编辑器, 与开发 PyQt5 程序据说是绝配  
访问 Eric [官网](https://sourceforge.net/projects/eric-ide/files/eric6/stable/), 下载安装包和汉化包， 解压后用汉化包中的文件覆盖原安装包的相应文件, 然后运行安装包中的 install.py 开始安装. 安装完成后, 进入相应目录找到 eric6.pyw 文件, 双击打开 Eric6  
