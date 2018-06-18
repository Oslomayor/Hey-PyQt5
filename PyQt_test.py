# 10:20, 2018-06-18 @ home
# PyQt5 环境测试
import sys
from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360,360)
widget.setWindowTitle('Hello, PyQt5')
widget.show()
sys.exit(app.exec())
