# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Design/wrong.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class WrongDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(416, 229)
        Dialog.setStyleSheet("background: #FFFFFF;")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 391, 29))
        self.label.setStyleSheet("font-family: Red Hat Text;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 24px;\n"
"line-height: 48px;")
        self.label.setObjectName("label")
        self.ok = QtWidgets.QPushButton(Dialog)
        self.ok.setGeometry(QtCore.QRect(120, 150, 171, 43))
        self.ok.setStyleSheet("font-family: Red Hat Text;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 36px;\n"
"line-height: 48px;\n"
"\n"
"color: #FDFDFD;\n"
"background: #3C9897;\n"
"border-radius: 10px;")
        self.ok.setObjectName("ok")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Error", "Error"))
        self.label.setText(_translate("Dialog", "Данные введены некорректно"))
        self.ok.setText(_translate("Dialog", "OK"))
