# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Design/register.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class RegisterWindowUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1435, 1051)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(760, 160, 402, 270))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.log_in = QtWidgets.QLabel(self.layoutWidget)
        self.log_in.setStyleSheet("font-family: Red Hat Text;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 48px;\n"
"line-height: 154.8%;")
        self.log_in.setAlignment(QtCore.Qt.AlignCenter)
        self.log_in.setObjectName("log_in")
        self.verticalLayout.addWidget(self.log_in)
        self.Login_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.Login_le.setStyleSheet("font-family: Red Hat Text;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 24px;\n"
"line-height: 0%;\n"
"/* or 0px */\n"
"\n"
"letter-spacing: -0.05em;\n"
"color: #00000;\n"
"position: absolute;\n"
"width: 344px;\n"
"height: 51px;\n"
"left: 548px;\n"
"top: 299px;\n"
"\n"
"background: #FFFFFF;\n"
"border-radius: 10px;")
        self.Login_le.setInputMask("")
        self.Login_le.setText("")
        self.Login_le.setObjectName("Login_le")
        self.verticalLayout.addWidget(self.Login_le)
        self.Password_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.Password_le.setStyleSheet("position: absolute;\n"
"width: 150px;\n"
"height: 25px;\n"
"left: 570px;\n"
"top: 392px;\n"
"\n"
"font-family: Red Hat Text;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 24px;\n"
"line-height: 0%;\n"
"/* or 0px */\n"
"\n"
"letter-spacing: -0.05em;\n"
"\n"
"color: #000000;\n"
"position: absolute;\n"
"width: 344px;\n"
"height: 51px;\n"
"left: 548px;\n"
"top: 299px;\n"
"\n"
"background: #FFFFFF;\n"
"border-radius: 10px;")
        self.Password_le.setInputMask("")
        self.Password_le.setText("")
        self.Password_le.setObjectName("Password_le")
        self.verticalLayout.addWidget(self.Password_le)
        self.sign_up = QtWidgets.QPushButton(self.layoutWidget)
        self.sign_up.setStyleSheet("font-family: Red Hat Text;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 24px;\n"
"line-height: 0%;\n"
"\n"
"position: absolute;\n"
"width: 400px;\n"
"height: 40px;\n"
"left: 520px;\n"
"top: 464px;\n"
"\n"
"background: #CFEBF9;\n"
"border-radius: 10px;")
        self.sign_up.setObjectName("sign_up")
        self.verticalLayout.addWidget(self.sign_up)
        self.back = QtWidgets.QPushButton(self.layoutWidget)
        self.back.setStyleSheet("font-family: Red Hat Text;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 24px;\n"
"line-height: 0%;\n"
"\n"
"position: absolute;\n"
"width: 400px;\n"
"height: 40px;\n"
"left: 520px;\n"
"top: 511px;\n"
"\n"
"background: #CFEBF9;\n"
"border-radius: 10px;")
        self.back.setObjectName("back")
        self.verticalLayout.addWidget(self.back)
        self.Message = QtWidgets.QLabel(self.centralwidget)
        self.Message.setGeometry(QtCore.QRect(710, 430, 501, 71))
        self.Message.setStyleSheet("font-family: Red Hat Text;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 24px;")
        self.Message.setText("")
        self.Message.setAlignment(QtCore.Qt.AlignCenter)
        self.Message.setObjectName("Message")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????????"))
        self.log_in.setText(_translate("MainWindow", "??????????????????????"))
        self.Login_le.setPlaceholderText(_translate("MainWindow", "??????????"))
        self.Password_le.setPlaceholderText(_translate("MainWindow", "????????????"))
        self.sign_up.setText(_translate("MainWindow", "????????????????????????????????????"))
        self.back.setText(_translate("MainWindow", "??????????"))
