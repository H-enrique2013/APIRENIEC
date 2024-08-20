# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_excel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConfirmExcel(object):
    def setupUi(self, ConfirmExcel):
        if not ConfirmExcel.objectName():
            ConfirmExcel.setObjectName(u"ConfirmExcel")
        ConfirmExcel.resize(509, 306)
        ConfirmExcel.setStyleSheet(u"QPushButton\n"
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
        self.label = QLabel(ConfirmExcel)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 461, 41))
        font = QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: red;")
        self.label.setFrameShape(QFrame.Box)
        self.cancelButton = QPushButton(ConfirmExcel)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(120, 250, 271, 41))
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
" 	border-color: grey;\n"
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
        self.cancelButton.setFlat(True)
        self.label_horaIngreso = QLabel(ConfirmExcel)
        self.label_horaIngreso.setObjectName(u"label_horaIngreso")
        self.label_horaIngreso.setGeometry(QRect(80, 110, 171, 16))
        self.label_horaSalida = QLabel(ConfirmExcel)
        self.label_horaSalida.setObjectName(u"label_horaSalida")
        self.label_horaSalida.setGeometry(QRect(290, 110, 171, 16))
        self.groupBox = QGroupBox(ConfirmExcel)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 70, 441, 171))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.groupBox.setFont(font2)
        self.groupBox.setStyleSheet(u"height: 2em;\n"
" border-style: solid;\n"
"border-width: 1px;\n"
" border-color: black;\n"
"background-color:#D9D9D9;\n"
"font-weight: bold;\n"
"")
        self.groupBox.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.inputFechaInicio = QDateEdit(self.groupBox)
        self.inputFechaInicio.setObjectName(u"inputFechaInicio")
        self.inputFechaInicio.setGeometry(QRect(50, 60, 131, 31))
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.inputFechaInicio.setFont(font3)
        self.inputFechaInicio.setDateTime(QDateTime(QDate(2023, 11, 1), QTime(0, 0, 0)))
        self.inputFechaInicio_2 = QDateEdit(self.groupBox)
        self.inputFechaInicio_2.setObjectName(u"inputFechaInicio_2")
        self.inputFechaInicio_2.setGeometry(QRect(260, 60, 131, 31))
        self.inputFechaInicio_2.setFont(font3)
        self.inputFechaInicio_2.setDateTime(QDateTime(QDate(2023, 11, 1), QTime(0, 0, 0)))
        self.generarExcelFechasButton = QPushButton(ConfirmExcel)
        self.generarExcelFechasButton.setObjectName(u"generarExcelFechasButton")
        self.generarExcelFechasButton.setGeometry(QRect(110, 190, 291, 41))
        self.generarExcelFechasButton.setFont(font1)
        self.generarExcelFechasButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.generarExcelFechasButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #1D6F42;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#1D6F42;\n"
"	color:white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.generarExcelFechasButton.setIcon(icon1)
        self.generarExcelFechasButton.setIconSize(QSize(30, 30))
        self.generarExcelFechasButton.setFlat(True)
        self.groupBox.raise_()
        self.label.raise_()
        self.cancelButton.raise_()
        self.label_horaIngreso.raise_()
        self.label_horaSalida.raise_()
        self.generarExcelFechasButton.raise_()
        QWidget.setTabOrder(self.generarExcelFechasButton, self.cancelButton)

        self.retranslateUi(ConfirmExcel)

        QMetaObject.connectSlotsByName(ConfirmExcel)
    # setupUi

    def retranslateUi(self, ConfirmExcel):
        ConfirmExcel.setWindowTitle(QCoreApplication.translate("ConfirmExcel", u"Generar Reporte", None))
        self.label.setText(QCoreApplication.translate("ConfirmExcel", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">GENERAR REPORTE</span></p></body></html>", None))
        self.cancelButton.setText(QCoreApplication.translate("ConfirmExcel", u"CANCELAR", None))
        self.label_horaIngreso.setText(QCoreApplication.translate("ConfirmExcel", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">FECHA INICIAL:</span></p></body></html>", None))
        self.label_horaSalida.setText(QCoreApplication.translate("ConfirmExcel", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">FECHA FINAL:</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("ConfirmExcel", u"REPORTE POR PERIODO", None))
        self.generarExcelFechasButton.setText(QCoreApplication.translate("ConfirmExcel", u"GENERAR EXCEL", None))
    # retranslateUi

