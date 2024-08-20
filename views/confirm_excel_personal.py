# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_excel_personal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ConfirmExcelPersonal(object):
    def setupUi(self, ConfirmExcel):
        if not ConfirmExcel.objectName():
            ConfirmExcel.setObjectName(u"ConfirmExcel")
        ConfirmExcel.resize(902, 408)
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
        self.label.setGeometry(QRect(20, 10, 861, 41))
        font = QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: #8a36d2;")
        self.label.setFrameShape(QFrame.Box)
        self.cancelButton = QPushButton(ConfirmExcel)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(310, 350, 271, 41))
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
        self.label_horaIngreso.setGeometry(QRect(80, 150, 171, 16))
        self.label_horaSalida = QLabel(ConfirmExcel)
        self.label_horaSalida.setObjectName(u"label_horaSalida")
        self.label_horaSalida.setGeometry(QRect(290, 150, 171, 16))
        self.horaSalidaLineEdit = QLineEdit(ConfirmExcel)
        self.horaSalidaLineEdit.setObjectName(u"horaSalidaLineEdit")
        self.horaSalidaLineEdit.setGeometry(QRect(290, 170, 161, 31))
        font2 = QFont()
        font2.setPointSize(14)
        self.horaSalidaLineEdit.setFont(font2)
        self.groupBox = QGroupBox(ConfirmExcel)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(50, 100, 431, 221))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.groupBox.setFont(font3)
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
        self.label_horaIngreso_4 = QLabel(self.groupBox)
        self.label_horaIngreso_4.setObjectName(u"label_horaIngreso_4")
        self.label_horaIngreso_4.setGeometry(QRect(30, 110, 331, 31))
        self.label_horaIngreso_4.setStyleSheet(u"border-color: #0000ffff;")
        self.horaIngresoLineEdit = QLineEdit(ConfirmExcel)
        self.horaIngresoLineEdit.setObjectName(u"horaIngresoLineEdit")
        self.horaIngresoLineEdit.setGeometry(QRect(80, 170, 161, 31))
        self.horaIngresoLineEdit.setFont(font2)
        self.groupBox_2 = QGroupBox(ConfirmExcel)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(530, 100, 341, 221))
        self.groupBox_2.setFont(font3)
        self.groupBox_2.setStyleSheet(u"height: 2em;\n"
" border-style: solid;\n"
"border-width: 1px;\n"
" border-color: black;\n"
"background-color:#D9D9D9;\n"
"font-weight: bold;\n"
"")
        self.groupBox_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.generarExcelHoyButton = QPushButton(self.groupBox_2)
        self.generarExcelHoyButton.setObjectName(u"generarExcelHoyButton")
        self.generarExcelHoyButton.setGeometry(QRect(30, 150, 291, 41))
        self.generarExcelHoyButton.setFont(font1)
        self.generarExcelHoyButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.generarExcelHoyButton.setStyleSheet(u"QPushButton\n"
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
        self.generarExcelHoyButton.setIcon(icon1)
        self.generarExcelHoyButton.setIconSize(QSize(30, 30))
        self.generarExcelHoyButton.setFlat(True)
        self.generarExcelFechasButton = QPushButton(ConfirmExcel)
        self.generarExcelFechasButton.setObjectName(u"generarExcelFechasButton")
        self.generarExcelFechasButton.setGeometry(QRect(110, 250, 291, 41))
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
        self.generarExcelFechasButton.setIcon(icon1)
        self.generarExcelFechasButton.setIconSize(QSize(30, 30))
        self.generarExcelFechasButton.setFlat(True)
        self.fechaHoyLineEdit = QLineEdit(ConfirmExcel)
        self.fechaHoyLineEdit.setObjectName(u"fechaHoyLineEdit")
        self.fechaHoyLineEdit.setGeometry(QRect(590, 170, 161, 31))
        self.fechaHoyLineEdit.setFont(font2)
        self.label_horaIngreso_2 = QLabel(ConfirmExcel)
        self.label_horaIngreso_2.setObjectName(u"label_horaIngreso_2")
        self.label_horaIngreso_2.setGeometry(QRect(590, 150, 171, 16))
        self.label_horaIngreso_3 = QLabel(ConfirmExcel)
        self.label_horaIngreso_3.setObjectName(u"label_horaIngreso_3")
        self.label_horaIngreso_3.setGeometry(QRect(590, 210, 241, 31))
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.cancelButton.raise_()
        self.label_horaIngreso.raise_()
        self.label_horaSalida.raise_()
        self.horaSalidaLineEdit.raise_()
        self.horaIngresoLineEdit.raise_()
        self.generarExcelFechasButton.raise_()
        self.fechaHoyLineEdit.raise_()
        self.label_horaIngreso_2.raise_()
        self.label_horaIngreso_3.raise_()
        QWidget.setTabOrder(self.horaIngresoLineEdit, self.horaSalidaLineEdit)
        QWidget.setTabOrder(self.horaSalidaLineEdit, self.generarExcelFechasButton)
        QWidget.setTabOrder(self.generarExcelFechasButton, self.fechaHoyLineEdit)
        QWidget.setTabOrder(self.fechaHoyLineEdit, self.generarExcelHoyButton)
        QWidget.setTabOrder(self.generarExcelHoyButton, self.cancelButton)

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
        self.label_horaIngreso_4.setText(QCoreApplication.translate("ConfirmExcel", u"<html><head/><body><p><span style=\" font-weight:400; color:#ff0000;\">*Importante: El formato de fecha es d/mm/aaaa.<br/>Por ejemplo 8/05/2021</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ConfirmExcel", u"REPORTE DIARIO", None))
        self.generarExcelHoyButton.setText(QCoreApplication.translate("ConfirmExcel", u"GENERAR EXCEL", None))
        self.generarExcelFechasButton.setText(QCoreApplication.translate("ConfirmExcel", u"GENERAR EXCEL", None))
        self.label_horaIngreso_2.setText(QCoreApplication.translate("ConfirmExcel", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">FECHA:</span></p></body></html>", None))
        self.label_horaIngreso_3.setText(QCoreApplication.translate("ConfirmExcel", u"<html><head/><body><p><span style=\" color:#ff0000;\">*Importante: El formato de fecha es d/mm/aaaa.<br/>Por ejemplo 8/05/2021</span></p></body></html>", None))
    # retranslateUi

