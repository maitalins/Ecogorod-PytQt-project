# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Design/help_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class HelpingMessageUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.agree = QtWidgets.QPushButton(self.centralwidget)
        self.agree.setGeometry(QtCore.QRect(840, 940, 240, 51))
        self.agree.setStyleSheet("position: absolute;\n"
"width: 340px;\n"
"height: 60px;\n"
"\n"
"background: #3C9897;\n"
"border-radius: 10px;\n"
"font-family: Red Hat Text;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 24px;\n"
"line-height: 32px;\n"
"\n"
"color: #FFFFFF;")
        self.agree.setObjectName("agree")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.agree.setText(_translate("MainWindow", "OK"))
