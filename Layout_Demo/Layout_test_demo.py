# PyQt5 Layout test

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_untitled import Ui_LayoutDemo

class LayoutDemo(QMainWindow, Ui_LayoutDemo):
    
    def __init__(self, parent=None):
        super(LayoutDemo, self).__init__(parent)
        self.setupUi(self)
        
    # @pyqtSlot
    # pyqtSlot 不知道什么情况不能用
    
    # 当 Start_Button  按下
    def on_Start_Button_clicked(self):
        print('收益_min:', self.doubleSpinBox_returns_min.text())
        print('收益_max:', self.doubleSpinBox_returns_min.text())
        print('最大回撤_min:', self.doubleSpinBox_3.text())
        print('最大回撤_max:', self.doubleSpinBox_4.text())
        print('sharp比_min:', self.doubleSpinBox_5.text())
        print('sharp比_max:', self.doubleSpinBox_6.text())
        
if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec_())
