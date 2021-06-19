# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Directions_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from recognition import main_app
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.verticalLayout.addWidget(self.button_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.defects = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.defects.setFont(font)
        self.defects.setObjectName("defects")
        self.horizontalLayout.addWidget(self.defects)
        self.d_reading = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.d_reading.setFont(font)
        self.d_reading.setText("")
        self.d_reading.setObjectName("d_reading")
        self.horizontalLayout.addWidget(self.d_reading)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.angle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.angle.setFont(font)
        self.angle.setObjectName("angle")
        self.horizontalLayout_3.addWidget(self.angle)
        self.a_reading = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.a_reading.setFont(font)
        self.a_reading.setText("")
        self.a_reading.setObjectName("a_reading")
        self.horizontalLayout_3.addWidget(self.a_reading)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.horizontalLayout_2.addWidget(self.button)
        self.b_reading = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b_reading.setFont(font)
        self.b_reading.setText("")
        self.b_reading.setObjectName("b_reading")
        self.horizontalLayout_2.addWidget(self.b_reading)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.started = False

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Readings"))
        self.button_2.setText(_translate("MainWindow", "Waiting for Reading"))
        self.defects.setText(_translate("MainWindow", "Number of Defects (Fingers):"))
        self.angle.setText(_translate("MainWindow", "Angle (Degrees):"))
        self.button.setText(_translate("MainWindow", "Button Pressed:"))
        
    def reading(self, window, text):
        _translate = QtCore.QCoreApplication.translate
        if not self.started:
            self.button_2.setText(_translate("MainWindow", "Readings Started"))
            self.started = True
        if window=='defects':
            self.d_reading.setText(_translate("MainWindow", text))
        elif window=='angle':
            self.a_reading.setText(_translate("MainWindow", text))
        elif window=='button':
            self.b_reading.setText(_translate("MainWindow", text))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main_app(ui)
    app.exec_()
