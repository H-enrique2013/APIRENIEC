# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_book_window_mantenimiento.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class NewBookFormMantenimiento(object):
    def setupUi(self, NewBook):
        if not NewBook.objectName():
            NewBook.setObjectName(u"NewBook")
        NewBook.resize(1212, 567)
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
        self.label.setGeometry(QRect(20, 10, 1171, 41))
        font = QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: blue;")
        self.label.setFrameShape(QFrame.Box)
        self.label_autoriza = QLabel(NewBook)
        self.label_autoriza.setObjectName(u"label_autoriza")
        self.label_autoriza.setGeometry(QRect(20, 140, 101, 16))
        self.titleLineEdit = QLineEdit(NewBook)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(20, 160, 381, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.titleLineEdit.setFont(font1)
        self.categoryLineEdit = QLineEdit(NewBook)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")
        self.categoryLineEdit.setGeometry(QRect(420, 160, 381, 31))
        self.categoryLineEdit.setFont(font1)
        self.descriptionTextedit = QTextEdit(NewBook)
        self.descriptionTextedit.setObjectName(u"descriptionTextedit")
        self.descriptionTextedit.setGeometry(QRect(20, 320, 1171, 151))
        self.descriptionTextedit.setFont(font1)
        self.addButton = QPushButton(NewBook)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(280, 500, 291, 41))
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
        self.cancelButton.setGeometry(QRect(640, 500, 271, 41))
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
        self.label_aquienVisita.setGeometry(QRect(420, 140, 191, 21))
        self.dateEditNuevo = QDateEdit(NewBook)
        self.dateEditNuevo.setObjectName(u"dateEditNuevo")
        self.dateEditNuevo.setGeometry(QRect(20, 90, 121, 31))
        self.dateEditNuevo.setFont(font1)
        self.label_area = QLabel(NewBook)
        self.label_area.setObjectName(u"label_area")
        self.label_area.setGeometry(QRect(820, 140, 191, 21))
        self.nombreVisitanteLineEdit = QLineEdit(NewBook)
        self.nombreVisitanteLineEdit.setObjectName(u"nombreVisitanteLineEdit")
        self.nombreVisitanteLineEdit.setGeometry(QRect(310, 90, 451, 31))
        self.nombreVisitanteLineEdit.setFont(font1)
        self.label_fecha = QLabel(NewBook)
        self.label_fecha.setObjectName(u"label_fecha")
        self.label_fecha.setGeometry(QRect(20, 70, 101, 16))
        self.label_visitante = QLabel(NewBook)
        self.label_visitante.setObjectName(u"label_visitante")
        self.label_visitante.setGeometry(QRect(310, 70, 341, 21))
        self.label_4 = QLabel(NewBook)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 290, 151, 21))
        self.categoryLineEditEntidadEmpresa = QLineEdit(NewBook)
        self.categoryLineEditEntidadEmpresa.setObjectName(u"categoryLineEditEntidadEmpresa")
        self.categoryLineEditEntidadEmpresa.setGeometry(QRect(790, 90, 401, 31))
        self.categoryLineEditEntidadEmpresa.setFont(font1)
        self.label_entidad = QLabel(NewBook)
        self.label_entidad.setObjectName(u"label_entidad")
        self.label_entidad.setGeometry(QRect(790, 70, 341, 21))
        self.label_horaIngreso = QLabel(NewBook)
        self.label_horaIngreso.setObjectName(u"label_horaIngreso")
        self.label_horaIngreso.setGeometry(QRect(20, 210, 171, 16))
        self.label_horaSalida = QLabel(NewBook)
        self.label_horaSalida.setObjectName(u"label_horaSalida")
        self.label_horaSalida.setGeometry(QRect(210, 210, 171, 16))
        self.label_motivoVisita = QLabel(NewBook)
        self.label_motivoVisita.setObjectName(u"label_motivoVisita")
        self.label_motivoVisita.setGeometry(QRect(400, 210, 341, 21))
        self.dniLineEdit = QLineEdit(NewBook)
        self.dniLineEdit.setObjectName(u"dniLineEdit")
        self.dniLineEdit.setGeometry(QRect(160, 90, 131, 31))
        self.dniLineEdit.setFont(font1)
        self.label_dni = QLabel(NewBook)
        self.label_dni.setObjectName(u"label_dni")
        self.label_dni.setGeometry(QRect(160, 70, 91, 21))
        self.label_piso = QLabel(NewBook)
        self.label_piso.setObjectName(u"label_piso")
        self.label_piso.setGeometry(QRect(870, 210, 51, 21))
        self.comboBoxPiso = QComboBox(NewBook)
        self.comboBoxPiso.setObjectName(u"comboBoxPiso")
        self.comboBoxPiso.setGeometry(QRect(870, 230, 121, 31))
        self.comboBoxPiso.setFont(font1)
        self.comboBoxPiso.setEditable(False)
        self.label_estado = QLabel(NewBook)
        self.label_estado.setObjectName(u"label_estado")
        self.label_estado.setGeometry(QRect(1010, 210, 71, 21))
        self.horaIngresoLineEdit = QLineEdit(NewBook)
        self.horaIngresoLineEdit.setObjectName(u"horaIngresoLineEdit")
        self.horaIngresoLineEdit.setGeometry(QRect(20, 230, 161, 31))
        self.horaIngresoLineEdit.setFont(font1)
        self.horaSalidaLineEdit = QLineEdit(NewBook)
        self.horaSalidaLineEdit.setObjectName(u"horaSalidaLineEdit")
        self.horaSalidaLineEdit.setGeometry(QRect(210, 230, 151, 31))
        self.horaSalidaLineEdit.setFont(font1)
        self.label_nota_obligatoria = QLabel(NewBook)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 480, 281, 21))
        self.ast_autoriza = QLabel(NewBook)
        self.ast_autoriza.setObjectName(u"ast_autoriza")
        self.ast_autoriza.setGeometry(QRect(120, 140, 21, 21))
        self.ast_aquienvisita = QLabel(NewBook)
        self.ast_aquienvisita.setObjectName(u"ast_aquienvisita")
        self.ast_aquienvisita.setGeometry(QRect(570, 140, 21, 21))
        self.ast_area = QLabel(NewBook)
        self.ast_area.setObjectName(u"ast_area")
        self.ast_area.setGeometry(QRect(960, 140, 21, 21))
        self.ast_entidadempresa = QLabel(NewBook)
        self.ast_entidadempresa.setObjectName(u"ast_entidadempresa")
        self.ast_entidadempresa.setGeometry(QRect(970, 70, 21, 21))
        self.ast_piso = QLabel(NewBook)
        self.ast_piso.setObjectName(u"ast_piso")
        self.ast_piso.setGeometry(QRect(920, 210, 21, 21))
        self.ast_estado = QLabel(NewBook)
        self.ast_estado.setObjectName(u"ast_estado")
        self.ast_estado.setGeometry(QRect(1090, 210, 21, 21))
        self.ast_motivo = QLabel(NewBook)
        self.ast_motivo.setObjectName(u"ast_motivo")
        self.ast_motivo.setGeometry(QRect(590, 210, 21, 21))
        self.ast_dni = QLabel(NewBook)
        self.ast_dni.setObjectName(u"ast_dni")
        self.ast_dni.setGeometry(QRect(200, 70, 21, 21))
        self.ast_horaingreso = QLabel(NewBook)
        self.ast_horaingreso.setObjectName(u"ast_horaingreso")
        self.ast_horaingreso.setGeometry(QRect(180, 210, 21, 21))
        self.ast_fecha = QLabel(NewBook)
        self.ast_fecha.setObjectName(u"ast_fecha")
        self.ast_fecha.setGeometry(QRect(80, 70, 21, 21))
        self.ast_visitante = QLabel(NewBook)
        self.ast_visitante.setObjectName(u"ast_visitante")
        self.ast_visitante.setGeometry(QRect(640, 70, 21, 21))
        self.comboBoxEstado = QComboBox(NewBook)
        self.comboBoxEstado.setObjectName(u"comboBoxEstado")
        self.comboBoxEstado.setGeometry(QRect(1010, 230, 171, 31))
        self.comboBoxEstado.setFont(font1)
        self.comboBoxEstado.setEditable(False)
        self.motivoVisitaLineEdit = QLineEdit(NewBook)
        self.motivoVisitaLineEdit.setObjectName(u"motivoVisitaLineEdit")
        self.motivoVisitaLineEdit.setGeometry(QRect(400, 230, 451, 31))
        self.motivoVisitaLineEdit.setFont(font1)
        self.label_advertencia_dni = QLabel(NewBook)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 480, 251, 21))
        self.areaVisitadaLineEdit = QLineEdit(NewBook)
        self.areaVisitadaLineEdit.setObjectName(u"areaVisitadaLineEdit")
        self.areaVisitadaLineEdit.setGeometry(QRect(820, 160, 371, 31))
        self.areaVisitadaLineEdit.setFont(font1)
        QWidget.setTabOrder(self.dniLineEdit, self.nombreVisitanteLineEdit)
        QWidget.setTabOrder(self.nombreVisitanteLineEdit, self.categoryLineEditEntidadEmpresa)
        QWidget.setTabOrder(self.categoryLineEditEntidadEmpresa, self.titleLineEdit)
        QWidget.setTabOrder(self.titleLineEdit, self.categoryLineEdit)
        QWidget.setTabOrder(self.categoryLineEdit, self.areaVisitadaLineEdit)
        QWidget.setTabOrder(self.areaVisitadaLineEdit, self.horaIngresoLineEdit)
        QWidget.setTabOrder(self.horaIngresoLineEdit, self.horaSalidaLineEdit)
        QWidget.setTabOrder(self.horaSalidaLineEdit, self.motivoVisitaLineEdit)
        QWidget.setTabOrder(self.motivoVisitaLineEdit, self.comboBoxPiso)
        QWidget.setTabOrder(self.comboBoxPiso, self.comboBoxEstado)
        QWidget.setTabOrder(self.comboBoxEstado, self.descriptionTextedit)
        QWidget.setTabOrder(self.descriptionTextedit, self.addButton)
        QWidget.setTabOrder(self.addButton, self.cancelButton)
        QWidget.setTabOrder(self.cancelButton, self.dateEditNuevo)

        self.retranslateUi(NewBook)

        self.addButton.setDefault(True)
        self.cancelButton.setDefault(True)


        QMetaObject.connectSlotsByName(NewBook)
    # setupUi

    def retranslateUi(self, NewBook):
        NewBook.setWindowTitle(QCoreApplication.translate("NewBook", u"Nuevo Registro", None))
        self.label.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">NUEVO REGISTRO</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">AUTORIZA:</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewBook", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBook", u"CANCELAR", None))
        self.label_aquienVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">A QUIEN VISITA:</span></p></body></html>", None))
        self.label_area.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">\u00c1REA VISITADA:</span></p></body></html>", None))
        self.label_fecha.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">FECHA:</span></p></body></html>", None))
        self.label_visitante.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">APELLIDOS Y NOMBRES DEL VISITANTE:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OBSERVACIONES:</span></p></body></html>", None))
        self.label_entidad.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ENTIDAD / EMPRESA:</span></p></body></html>", None))
        self.label_horaIngreso.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">HORA DE INGRESO:</span></p></body></html>", None))
        self.label_horaSalida.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">HORA DE SALIDA:</span></p></body></html>", None))
        self.label_motivoVisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">MOTIVO DE LA VISITA:</span></p></body></html>", None))
        self.label_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">DNI:</span></p></body></html>", None))
        self.label_piso.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">PISO:</span></p></body></html>", None))
        self.label_estado.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ESTADO:</span></p></body></html>", None))
        self.label_nota_obligatoria.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) Estos campos son obligatorios</span></p></body></html>", None))
        self.ast_autoriza.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_aquienvisita.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_area.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_entidadempresa.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_piso.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_estado.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_motivo.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_horaingreso.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_fecha.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_visitante.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("NewBook", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El DNI debe tener 8 d\u00edgitos</span></p></body></html>", None))
    # retranslateUi

