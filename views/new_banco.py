# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_banco.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewBook(object):
    def setupUi(self, NewBook):
        if not NewBook.objectName():
            NewBook.setObjectName(u"NewBook")
        NewBook.resize(1304, 691)
        NewBook.setStyleSheet(u"QPushButton\n"
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
        self.label = QLabel(NewBook)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 1271, 41))
        font = QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setFocusPolicy(Qt.ClickFocus)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: black;")
        self.label.setFrameShape(QFrame.Box)
        self.tableMasiva2 = QTableWidget(NewBook)
        self.tableMasiva2.setObjectName(u"tableMasiva2")
        self.tableMasiva2.setGeometry(QRect(20, 70, 1271, 551))
        self.tableMasiva2.setAutoFillBackground(True)
        self.tableMasiva2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableMasiva2.setTextElideMode(Qt.ElideLeft)
        self.tableMasiva2.horizontalHeader().setMinimumSectionSize(10)
        self.cancelButton = QPushButton(NewBook)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(660, 630, 221, 41))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.cancelButton.setFont(font1)
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: black;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}")
        icon = QIcon()
        icon.addFile(u"./assets/icons/cancel-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon)
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setAutoDefault(True)
        self.cancelButton.setFlat(True)
        self.btnExcel = QPushButton(NewBook)
        self.btnExcel.setObjectName(u"btnExcel")
        self.btnExcel.setGeometry(QRect(430, 630, 221, 41))
        self.btnExcel.setFont(font1)
        self.btnExcel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnExcel.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: black;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/iconexcel.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnExcel.setIcon(icon1)
        self.btnExcel.setIconSize(QSize(35, 35))
        self.btnExcel.setAutoDefault(True)
        self.btnExcel.setFlat(True)

        self.retranslateUi(NewBook)

        self.cancelButton.setDefault(True)
        self.btnExcel.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">GENERACI\u00d3N DE PADRON BANCO</span></p></body></html>", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.btnExcel.setText(QCoreApplication.translate("NewBook", u"Generar Excel", None))
    # retranslateUi

