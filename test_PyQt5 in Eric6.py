# 23:34, June 20th, 2018 @ Dorm
# test PyQt5 in Eric6 
import sys
from PyQt5.QtWidgets import QWidget,  QApplication
if __name__ == '__main__':
    app = QApplication(sys.argv)
    q = QWidget()
    q.show()
    sys.exit(app.exec_())
