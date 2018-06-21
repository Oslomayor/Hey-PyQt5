# 调用 UI 测试
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_mainWindow import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,  parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
