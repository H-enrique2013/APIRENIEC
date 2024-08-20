# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class LoginRegistroForm(object):
    def setupUi(self, LoginRegistro):
        if not LoginRegistro.objectName():
            LoginRegistro.setObjectName(u"LoginRegistro")
        LoginRegistro.resize(480, 327)
        LoginRegistro.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}")
        LoginRegistro.setInputMethodHints(Qt.ImhNone)
        self.label = QLabel(LoginRegistro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(45, 20, 390, 41))
        font = QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: red;")
        self.label.setFrameShape(QFrame.Box)
        self.passwordLineEdit = QLineEdit(LoginRegistro)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(130, 180, 271, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.passwordLineEdit.setFont(font1)
        self.usuarioLineEdit = QLineEdit(LoginRegistro)
        self.usuarioLineEdit.setObjectName(u"usuarioLineEdit")
        self.usuarioLineEdit.setGeometry(QRect(130, 100, 271, 41))
        self.usuarioLineEdit.setFont(font1)
        self.ingresarButton = QPushButton(LoginRegistro)
        self.ingresarButton.setObjectName(u"ingresarButton")
        self.ingresarButton.setGeometry(QRect(80, 260, 321, 41))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.ingresarButton.setFont(font2)
        self.ingresarButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ingresarButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        icon = QIcon()
        icon.addFile(u"./assets/icons/exitoso.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ingresarButton.setIcon(icon)
        self.ingresarButton.setIconSize(QSize(30, 30))
        self.ingresarButton.setFlat(True)
        self.label_validacion_usuario = QLabel(LoginRegistro)
        self.label_validacion_usuario.setObjectName(u"label_validacion_usuario")
        self.label_validacion_usuario.setGeometry(QRect(80, 140, 281, 21))
        self.label_validacion_password = QLabel(LoginRegistro)
        self.label_validacion_password.setObjectName(u"label_validacion_password")
        self.label_validacion_password.setGeometry(QRect(90, 220, 261, 21))
        self.progressBar = QProgressBar(LoginRegistro)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 310, 481, 16))
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)
        self.pushButton = QPushButton(LoginRegistro)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(80, 180, 51, 41))
        self.pushButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	font-weight: bold;\n"
"	background-color:grey;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/pass_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton_2 = QPushButton(LoginRegistro)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QRect(80, 100, 51, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	font-weight: bold;\n"
"	background-color:grey;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/icon_user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(30, 30))
        QWidget.setTabOrder(self.usuarioLineEdit, self.passwordLineEdit)
        QWidget.setTabOrder(self.passwordLineEdit, self.ingresarButton)

        self.retranslateUi(LoginRegistro)

        self.ingresarButton.setDefault(True)
        

        QMetaObject.connectSlotsByName(LoginRegistro)
    # setupUi

    def retranslateUi(self, LoginRegistro):
        LoginRegistro.setWindowTitle(QCoreApplication.translate("LoginRegistro", u"Inicio de Sesi\u00f3n", None))
        self.label.setText(QCoreApplication.translate("LoginRegistro", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">INICIO DE SESI\u00d3N</span></p></body></html>", None))
        self.ingresarButton.setText(QCoreApplication.translate("LoginRegistro", u"Ingresar", None))
        self.label_validacion_usuario.setText(QCoreApplication.translate("LoginRegistro", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">- El nombre de usuario es incorrecto</span></p></body></html>", None))
        self.label_validacion_password.setText(QCoreApplication.translate("LoginRegistro", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">- La contrase\u00f1a es incorrecta</span></p></body></html>", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
    # retranslateUi

