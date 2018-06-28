# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\AllPrj\PyQt5prj\Layout_test\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LayoutDemo(object):
    def setupUi(self, LayoutDemo):
        LayoutDemo.setObjectName("LayoutDemo")
        LayoutDemo.resize(748, 594)
        self.centralwidget = QtWidgets.QWidget(LayoutDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 130, 471, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox_returns_min = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_returns_min.setObjectName("doubleSpinBox_returns_min")
        self.gridLayout.addWidget(self.doubleSpinBox_returns_min, 0, 1, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout.addWidget(self.doubleSpinBox_4, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout.addWidget(self.doubleSpinBox_6, 2, 2, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout.addWidget(self.doubleSpinBox_5, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.doubleSpinBox_returns_max = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_returns_max.setObjectName("doubleSpinBox_returns_max")
        self.gridLayout.addWidget(self.doubleSpinBox_returns_max, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 80, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(510, 80, 54, 12))
        self.label_5.setObjectName("label_5")
        self.Start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Button.setGeometry(QtCore.QRect(650, 280, 75, 23))
        self.Start_Button.setObjectName("Start_Button")
        LayoutDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LayoutDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 23))
        self.menubar.setObjectName("menubar")
        LayoutDemo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LayoutDemo)
        self.statusbar.setObjectName("statusbar")
        LayoutDemo.setStatusBar(self.statusbar)
        self.label_3.setBuddy(self.doubleSpinBox_5)

        self.retranslateUi(LayoutDemo)
        QtCore.QMetaObject.connectSlotsByName(LayoutDemo)
        LayoutDemo.setTabOrder(self.doubleSpinBox_returns_min, self.doubleSpinBox_returns_max)
        LayoutDemo.setTabOrder(self.doubleSpinBox_returns_max, self.doubleSpinBox_3)
        LayoutDemo.setTabOrder(self.doubleSpinBox_3, self.doubleSpinBox_4)
        LayoutDemo.setTabOrder(self.doubleSpinBox_4, self.doubleSpinBox_5)
        LayoutDemo.setTabOrder(self.doubleSpinBox_5, self.doubleSpinBox_6)

    def retranslateUi(self, LayoutDemo):
        _translate = QtCore.QCoreApplication.translate
        LayoutDemo.setWindowTitle(_translate("LayoutDemo", "MainWindow"))
        self.label.setText(_translate("LayoutDemo", "收益"))
        self.label_3.setText(_translate("LayoutDemo", "&sharp 比"))
        self.label_2.setText(_translate("LayoutDemo", "最大回撤"))
        self.label_4.setText(_translate("LayoutDemo", "最小值"))
        self.label_5.setText(_translate("LayoutDemo", "最大值"))
        self.Start_Button.setText(_translate("LayoutDemo", "开始"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LayoutDemo = QtWidgets.QMainWindow()
    ui = Ui_LayoutDemo()
    ui.setupUi(LayoutDemo)
    LayoutDemo.show()
    sys.exit(app.exec_())

