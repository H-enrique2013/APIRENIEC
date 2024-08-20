# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_padron.ui'
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
        self.label_autoriza = QLabel(NewBook)
        self.label_autoriza.setObjectName(u"label_autoriza")
        self.label_autoriza.setGeometry(QRect(20, 60, 101, 21))
        self.inputRegion = QLineEdit(NewBook)
        self.inputRegion.setObjectName(u"inputRegion")
        self.inputRegion.setGeometry(QRect(20, 80, 151, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.inputRegion.setFont(font1)
        self.inputProvincia = QLineEdit(NewBook)
        self.inputProvincia.setObjectName(u"inputProvincia")
        self.inputProvincia.setGeometry(QRect(180, 80, 171, 31))
        self.inputProvincia.setFont(font1)
        self.label_aquienVisita = QLabel(NewBook)
        self.label_aquienVisita.setObjectName(u"label_aquienVisita")
        self.label_aquienVisita.setGeometry(QRect(180, 60, 181, 21))
        self.label_area = QLabel(NewBook)
        self.label_area.setObjectName(u"label_area")
        self.label_area.setGeometry(QRect(540, 60, 191, 21))
        self.label_fecha = QLabel(NewBook)
        self.label_fecha.setObjectName(u"label_fecha")
        self.label_fecha.setGeometry(QRect(20, 120, 251, 21))
        self.label_dni = QLabel(NewBook)
        self.label_dni.setObjectName(u"label_dni")
        self.label_dni.setGeometry(QRect(300, 120, 221, 21))
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(360, 60, 171, 21))
        self.label_area_3 = QLabel(NewBook)
        self.label_area_3.setObjectName(u"label_area_3")
        self.label_area_3.setGeometry(QRect(730, 60, 181, 21))
        self.inputDistrito = QLineEdit(NewBook)
        self.inputDistrito.setObjectName(u"inputDistrito")
        self.inputDistrito.setGeometry(QRect(360, 80, 171, 31))
        self.inputDistrito.setFont(font1)
        self.inputSector = QLineEdit(NewBook)
        self.inputSector.setObjectName(u"inputSector")
        self.inputSector.setGeometry(QRect(540, 80, 181, 31))
        self.inputSector.setFont(font1)
        self.inputCultivo = QLineEdit(NewBook)
        self.inputCultivo.setObjectName(u"inputCultivo")
        self.inputCultivo.setGeometry(QRect(730, 80, 191, 31))
        self.inputCultivo.setFont(font1)
        self.inputSuperficie = QLineEdit(NewBook)
        self.inputSuperficie.setObjectName(u"inputSuperficie")
        self.inputSuperficie.setGeometry(QRect(20, 140, 271, 31))
        self.inputSuperficie.setFont(font1)
        self.inputMonto = QLineEdit(NewBook)
        self.inputMonto.setObjectName(u"inputMonto")
        self.inputMonto.setGeometry(QRect(300, 140, 241, 31))
        self.inputMonto.setFont(font1)
        self.tableMasiva2 = QTableWidget(NewBook)
        self.tableMasiva2.setObjectName(u"tableMasiva2")
        self.tableMasiva2.setGeometry(QRect(20, 180, 1271, 441))
        self.tableMasiva2.setAutoFillBackground(True)
        self.tableMasiva2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableMasiva2.setTextElideMode(Qt.ElideLeft)
        self.tableMasiva2.horizontalHeader().setMinimumSectionSize(10)
        self.cancelButton = QPushButton(NewBook)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(770, 630, 191, 41))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.cancelButton.setFont(font2)
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
        self.addPdf = QPushButton(NewBook)
        self.addPdf.setObjectName(u"addPdf")
        self.addPdf.setGeometry(QRect(560, 630, 191, 41))
        self.addPdf.setFont(font2)
        self.addPdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.addPdf.setStyleSheet(u"QPushButton\n"
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
        icon1.addFile(u"./assets/icons/PDF_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addPdf.setIcon(icon1)
        self.addPdf.setIconSize(QSize(30, 30))
        self.addPdf.setAutoDefault(True)
        self.addPdf.setFlat(True)
        self.btnExcel = QPushButton(NewBook)
        self.btnExcel.setObjectName(u"btnExcel")
        self.btnExcel.setGeometry(QRect(350, 630, 191, 41))
        self.btnExcel.setFont(font2)
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
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/iconexcel.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnExcel.setIcon(icon2)
        self.btnExcel.setIconSize(QSize(35, 35))
        self.btnExcel.setAutoDefault(True)
        self.btnExcel.setFlat(True)
        self.line = QFrame(NewBook)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 110, 1271, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.btnGenerarPadron = QPushButton(NewBook)
        self.btnGenerarPadron.setObjectName(u"btnGenerarPadron")
        self.btnGenerarPadron.setGeometry(QRect(1080, 70, 211, 41))
        self.btnGenerarPadron.setFont(font2)
        self.btnGenerarPadron.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnGenerarPadron.setStyleSheet(u"QPushButton\n"
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
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnGenerarPadron.setIcon(icon3)
        self.btnGenerarPadron.setIconSize(QSize(35, 35))
        self.btnGenerarPadron.setAutoDefault(True)
        self.btnGenerarPadron.setFlat(True)
        self.inputFechaTermino = QDateEdit(NewBook)
        self.inputFechaTermino.setObjectName(u"inputFechaTermino")
        self.inputFechaTermino.setGeometry(QRect(930, 80, 141, 31))
        self.inputFechaTermino.setFont(font1)
        self.inputFechaTermino.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.label_area_4 = QLabel(NewBook)
        self.label_area_4.setObjectName(u"label_area_4")
        self.label_area_4.setGeometry(QRect(930, 60, 181, 21))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_area_4.setFont(font3)
        QWidget.setTabOrder(self.inputRegion, self.inputProvincia)

        self.retranslateUi(NewBook)

        self.cancelButton.setDefault(True)
        self.addPdf.setDefault(True)
        self.btnExcel.setDefault(True)
        self.btnGenerarPadron.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">GENERACI\u00d3N DE PADRON</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Regi\u00f3n:</span></p></body></html>", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Provincia:</span></p></body></html>", None))
        self.label_area.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Sector Estad\u00edstico:</span></p></body></html>", None))
        self.label_fecha.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Superficie Indemnizable (ha):</span></p></body></html>", None))
        self.label_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Monto Indemnizable (S/.):</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Distrito:</span></p></body></html>", None))
        self.label_area_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Cultivo Indemnizable:</span></p></body></html>", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.addPdf.setText(QCoreApplication.translate("NewBook", u"Generar PDF", None))
        self.btnExcel.setText(QCoreApplication.translate("NewBook", u"Generar Excel", None))
        self.btnGenerarPadron.setText(QCoreApplication.translate("NewBook", u"Generar Padr\u00f3n", None))
        self.label_area_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p>Fecha Termino:</p></body></html>", None))
    # retranslateUi

