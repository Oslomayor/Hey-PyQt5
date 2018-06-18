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
