# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_preventivo.ui'
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
        NewBook.resize(1011, 447)
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
        self.label.setGeometry(QRect(20, 10, 981, 41))
        font = QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: green;")
        self.label.setFrameShape(QFrame.Box)
        self.label_autoriza = QLabel(NewBook)
        self.label_autoriza.setObjectName(u"label_autoriza")
        self.label_autoriza.setGeometry(QRect(20, 70, 101, 21))
        self.inputCodigo = QLineEdit(NewBook)
        self.inputCodigo.setObjectName(u"inputCodigo")
        self.inputCodigo.setGeometry(QRect(20, 90, 111, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.inputCodigo.setFont(font1)
        self.inputInmueble = QLineEdit(NewBook)
        self.inputInmueble.setObjectName(u"inputInmueble")
        self.inputInmueble.setGeometry(QRect(140, 90, 221, 31))
        self.inputInmueble.setFont(font1)
        self.addButton = QPushButton(NewBook)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(200, 390, 291, 41))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.addButton.setFont(font2)
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton\n"
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
        icon.addFile(u"./assets/icons/add-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setIconSize(QSize(30, 30))
        self.addButton.setAutoDefault(True)
        self.addButton.setFlat(True)
        self.cancelButton = QPushButton(NewBook)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(530, 390, 271, 41))
        self.cancelButton.setFont(font2)
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
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/cancel-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setAutoDefault(True)
        self.cancelButton.setFlat(True)
        self.label_aquienVisita = QLabel(NewBook)
        self.label_aquienVisita.setObjectName(u"label_aquienVisita")
        self.label_aquienVisita.setGeometry(QRect(140, 70, 191, 21))
        self.label_area = QLabel(NewBook)
        self.label_area.setObjectName(u"label_area")
        self.label_area.setGeometry(QRect(500, 70, 191, 21))
        self.inputDias = QLineEdit(NewBook)
        self.inputDias.setObjectName(u"inputDias")
        self.inputDias.setEnabled(False)
        self.inputDias.setGeometry(QRect(320, 160, 71, 31))
        self.inputDias.setFont(font1)
        self.label_fecha = QLabel(NewBook)
        self.label_fecha.setObjectName(u"label_fecha")
        self.label_fecha.setGeometry(QRect(20, 140, 111, 16))
        self.label_visitante = QLabel(NewBook)
        self.label_visitante.setObjectName(u"label_visitante")
        self.label_visitante.setGeometry(QRect(320, 140, 141, 21))
        self.inputMonto = QLineEdit(NewBook)
        self.inputMonto.setObjectName(u"inputMonto")
        self.inputMonto.setEnabled(False)
        self.inputMonto.setGeometry(QRect(410, 160, 151, 31))
        self.inputMonto.setFont(font1)
        self.label_entidad = QLabel(NewBook)
        self.label_entidad.setObjectName(u"label_entidad")
        self.label_entidad.setGeometry(QRect(410, 140, 151, 21))
        self.label_dni = QLabel(NewBook)
        self.label_dni.setObjectName(u"label_dni")
        self.label_dni.setGeometry(QRect(170, 140, 91, 21))
        self.label_nota_obligatoria = QLabel(NewBook)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 360, 281, 21))
        self.ast_aquienvisita = QLabel(NewBook)
        self.ast_aquienvisita.setObjectName(u"ast_aquienvisita")
        self.ast_aquienvisita.setGeometry(QRect(220, 70, 21, 21))
        self.ast_dni = QLabel(NewBook)
        self.ast_dni.setObjectName(u"ast_dni")
        self.ast_dni.setGeometry(QRect(250, 140, 21, 21))
        self.ast_horaingreso = QLabel(NewBook)
        self.ast_horaingreso.setObjectName(u"ast_horaingreso")
        self.ast_horaingreso.setGeometry(QRect(710, 140, 21, 21))
        self.ast_fecha = QLabel(NewBook)
        self.ast_fecha.setObjectName(u"ast_fecha")
        self.ast_fecha.setGeometry(QRect(120, 140, 21, 21))
        self.label_area_2 = QLabel(NewBook)
        self.label_area_2.setObjectName(u"label_area_2")
        self.label_area_2.setGeometry(QRect(370, 70, 61, 21))
        self.label_area_3 = QLabel(NewBook)
        self.label_area_3.setObjectName(u"label_area_3")
        self.label_area_3.setGeometry(QRect(710, 70, 91, 21))
        self.label_entidad_2 = QLabel(NewBook)
        self.label_entidad_2.setObjectName(u"label_entidad_2")
        self.label_entidad_2.setGeometry(QRect(580, 140, 151, 21))
        self.inputFechaFin = QDateEdit(NewBook)
        self.inputFechaFin.setObjectName(u"inputFechaFin")
        self.inputFechaFin.setGeometry(QRect(170, 160, 131, 31))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.inputFechaFin.setFont(font3)
        self.inputFechaFin.setDateTime(QDateTime(QDate(2024, 12, 31), QTime(0, 0, 0)))
        self.inputDepartamento = QLineEdit(NewBook)
        self.inputDepartamento.setObjectName(u"inputDepartamento")
        self.inputDepartamento.setEnabled(False)
        self.inputDepartamento.setGeometry(QRect(500, 90, 201, 31))
        self.inputDepartamento.setFont(font1)
        self.inputTipo = QLineEdit(NewBook)
        self.inputTipo.setObjectName(u"inputTipo")
        self.inputTipo.setEnabled(False)
        self.inputTipo.setGeometry(QRect(370, 90, 121, 31))
        self.inputTipo.setFont(font1)
        self.inputDireccion = QLineEdit(NewBook)
        self.inputDireccion.setObjectName(u"inputDireccion")
        self.inputDireccion.setEnabled(False)
        self.inputDireccion.setGeometry(QRect(710, 90, 291, 31))
        self.inputDireccion.setFont(font1)
        self.inputFechaInicio = QDateEdit(NewBook)
        self.inputFechaInicio.setObjectName(u"inputFechaInicio")
        self.inputFechaInicio.setGeometry(QRect(20, 160, 131, 31))
        self.inputFechaInicio.setFont(font3)
        self.inputFechaInicio.setDateTime(QDateTime(QDate(2023, 11, 1), QTime(0, 0, 0)))
        self.cbReqCorrectivo = QComboBox(NewBook)
        self.cbReqCorrectivo.setObjectName(u"cbReqCorrectivo")
        self.cbReqCorrectivo.setEnabled(True)
        self.cbReqCorrectivo.setGeometry(QRect(580, 160, 141, 31))
        self.cbReqCorrectivo.setFont(font1)
        self.cbReqCorrectivo.setEditable(False)
        self.plainTextObservaciones = QPlainTextEdit(NewBook)
        self.plainTextObservaciones.setObjectName(u"plainTextObservaciones")
        self.plainTextObservaciones.setGeometry(QRect(20, 230, 981, 131))
        self.label_fecha_2 = QLabel(NewBook)
        self.label_fecha_2.setObjectName(u"label_fecha_2")
        self.label_fecha_2.setGeometry(QRect(20, 210, 161, 16))
        QWidget.setTabOrder(self.inputCodigo, self.inputInmueble)
        QWidget.setTabOrder(self.inputInmueble, self.inputDias)
        QWidget.setTabOrder(self.inputDias, self.inputMonto)
        QWidget.setTabOrder(self.inputMonto, self.addButton)
        QWidget.setTabOrder(self.addButton, self.cancelButton)

        self.retranslateUi(NewBook)

        self.addButton.setDefault(True)
        self.cancelButton.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">NUEVO MANTENIMIENTO PREVENTIVO</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Codigo:</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewBook", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Inmueble:</span></p></body></html>", None))
        self.label_area.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Departamento:</span></p></body></html>", None))
        self.label_fecha.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Fecha Inicio:</span></p></body></html>", None))
        self.label_visitante.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">D\u00edas:</span></p></body></html>", None))
        self.label_entidad.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Monto:</span></p></body></html>", None))
        self.label_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Fecha Fin:</span></p></body></html>", None))
        self.label_nota_obligatoria.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) Estos campos son obligatorios</span></p></body></html>", None))
        self.ast_aquienvisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_horaingreso.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_fecha.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_area_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Tipo:</span></p></body></html>", None))
        self.label_area_3.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Direcci\u00f3n:</span></p></body></html>", None))
        self.label_entidad_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Req. Correctivo:</span></p></body></html>", None))
        self.label_fecha_2.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Observaciones:</span></p></body></html>", None))
    # retranslateUi

