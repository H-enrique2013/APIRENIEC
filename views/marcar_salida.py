# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'marcar_salida_book_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MarcarSalidaForm(object):
    def setupUi(self, MarcarSalida):
        if not MarcarSalida.objectName():
            MarcarSalida.setObjectName(u"MarcarSalida")
        MarcarSalida.resize(1212, 573)
        MarcarSalida.setStyleSheet(u"QPushButton\n"
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
        self.label = QLabel(MarcarSalida)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 1171, 41))
        font = QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: red;")
        self.label.setFrameShape(QFrame.Box)
        self.label_autoriza = QLabel(MarcarSalida)
        self.label_autoriza.setObjectName(u"label_autoriza")
        self.label_autoriza.setGeometry(QRect(20, 70, 101, 16))
        self.titleLineEdit = QLineEdit(MarcarSalida)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(20, 90, 381, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.titleLineEdit.setFont(font1)
        self.categoryLineEdit = QLineEdit(MarcarSalida)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")
        self.categoryLineEdit.setGeometry(QRect(420, 90, 381, 31))
        self.categoryLineEdit.setFont(font1)
        self.descriptionTextedit = QTextEdit(MarcarSalida)
        self.descriptionTextedit.setObjectName(u"descriptionTextedit")
        self.descriptionTextedit.setGeometry(QRect(20, 320, 1141, 151))
        self.descriptionTextedit.setFont(font1)
        self.editButton = QPushButton(MarcarSalida)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(280, 500, 291, 41))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.editButton.setFont(font2)
        self.editButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.editButton.setStyleSheet(u"QPushButton\n"
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
        icon.addFile(u"./assets/icons/icon_black_clock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editButton.setIcon(icon)
        self.editButton.setIconSize(QSize(30, 60))
        self.editButton.setFlat(True)
        self.cancelButton = QPushButton(MarcarSalida)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(630, 500, 271, 41))
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
        self.cancelButton.setFlat(True)
        self.label_aquienvisita = QLabel(MarcarSalida)
        self.label_aquienvisita.setObjectName(u"label_aquienvisita")
        self.label_aquienvisita.setGeometry(QRect(420, 70, 191, 21))
        self.dateEditNuevo = QDateEdit(MarcarSalida)
        self.dateEditNuevo.setObjectName(u"dateEditNuevo")
        self.dateEditNuevo.setGeometry(QRect(20, 160, 121, 31))
        self.dateEditNuevo.setFont(font1)
        self.label_area = QLabel(MarcarSalida)
        self.label_area.setObjectName(u"label_area")
        self.label_area.setGeometry(QRect(820, 70, 191, 21))
        self.nombreVisitanteLineEdit = QLineEdit(MarcarSalida)
        self.nombreVisitanteLineEdit.setObjectName(u"nombreVisitanteLineEdit")
        self.nombreVisitanteLineEdit.setGeometry(QRect(310, 160, 451, 31))
        self.nombreVisitanteLineEdit.setFont(font1)
        self.label_fecha = QLabel(MarcarSalida)
        self.label_fecha.setObjectName(u"label_fecha")
        self.label_fecha.setGeometry(QRect(20, 140, 101, 16))
        self.label_visitante = QLabel(MarcarSalida)
        self.label_visitante.setObjectName(u"label_visitante")
        self.label_visitante.setGeometry(QRect(310, 140, 341, 21))
        self.label_observaciones = QLabel(MarcarSalida)
        self.label_observaciones.setObjectName(u"label_observaciones")
        self.label_observaciones.setGeometry(QRect(20, 290, 151, 21))
        self.categoryLineEditEntidadEmpresa = QLineEdit(MarcarSalida)
        self.categoryLineEditEntidadEmpresa.setObjectName(u"categoryLineEditEntidadEmpresa")
        self.categoryLineEditEntidadEmpresa.setGeometry(QRect(790, 160, 401, 31))
        self.categoryLineEditEntidadEmpresa.setFont(font1)
        self.label_entidad = QLabel(MarcarSalida)
        self.label_entidad.setObjectName(u"label_entidad")
        self.label_entidad.setGeometry(QRect(790, 140, 341, 21))
        self.label_horaIngreso = QLabel(MarcarSalida)
        self.label_horaIngreso.setObjectName(u"label_horaIngreso")
        self.label_horaIngreso.setGeometry(QRect(20, 210, 171, 16))
        self.label_horaSalida = QLabel(MarcarSalida)
        self.label_horaSalida.setObjectName(u"label_horaSalida")
        self.label_horaSalida.setGeometry(QRect(210, 210, 171, 16))
        self.label_motivoVisita = QLabel(MarcarSalida)
        self.label_motivoVisita.setObjectName(u"label_motivoVisita")
        self.label_motivoVisita.setGeometry(QRect(400, 210, 341, 21))
        self.dniLineEdit = QLineEdit(MarcarSalida)
        self.dniLineEdit.setObjectName(u"dniLineEdit")
        self.dniLineEdit.setGeometry(QRect(160, 160, 131, 31))
        self.dniLineEdit.setFont(font1)
        self.label_dni = QLabel(MarcarSalida)
        self.label_dni.setObjectName(u"label_dni")
        self.label_dni.setGeometry(QRect(160, 140, 91, 21))
        self.label_piso = QLabel(MarcarSalida)
        self.label_piso.setObjectName(u"label_piso")
        self.label_piso.setGeometry(QRect(880, 210, 61, 21))
        self.comboBoxPiso = QComboBox(MarcarSalida)
        self.comboBoxPiso.setObjectName(u"comboBoxPiso")
        self.comboBoxPiso.setGeometry(QRect(880, 230, 121, 31))
        self.comboBoxPiso.setFont(font1)
        self.comboBoxPiso.setEditable(False)
        self.label_estado = QLabel(MarcarSalida)
        self.label_estado.setObjectName(u"label_estado")
        self.label_estado.setGeometry(QRect(1020, 210, 91, 21))
        self.comboBoxEstado = QComboBox(MarcarSalida)
        self.comboBoxEstado.setObjectName(u"comboBoxEstado")
        self.comboBoxEstado.setGeometry(QRect(1020, 230, 171, 31))
        self.comboBoxEstado.setFont(font1)
        self.comboBoxEstado.setEditable(False)
        self.horaIngresoLineEdit = QLineEdit(MarcarSalida)
        self.horaIngresoLineEdit.setObjectName(u"horaIngresoLineEdit")
        self.horaIngresoLineEdit.setGeometry(QRect(20, 230, 161, 31))
        self.horaIngresoLineEdit.setFont(font1)
        self.horaSalidaLineEdit = QLineEdit(MarcarSalida)
        self.horaSalidaLineEdit.setObjectName(u"horaSalidaLineEdit")
        self.horaSalidaLineEdit.setGeometry(QRect(210, 230, 151, 31))
        self.horaSalidaLineEdit.setFont(font1)
        self.ast_motivo = QLabel(MarcarSalida)
        self.ast_motivo.setObjectName(u"ast_motivo")
        self.ast_motivo.setGeometry(QRect(590, 210, 16, 21))
        self.ast_visitante = QLabel(MarcarSalida)
        self.ast_visitante.setObjectName(u"ast_visitante")
        self.ast_visitante.setGeometry(QRect(640, 140, 16, 21))
        self.ast_horaingreso = QLabel(MarcarSalida)
        self.ast_horaingreso.setObjectName(u"ast_horaingreso")
        self.ast_horaingreso.setGeometry(QRect(180, 210, 16, 21))
        self.ast_fecha = QLabel(MarcarSalida)
        self.ast_fecha.setObjectName(u"ast_fecha")
        self.ast_fecha.setGeometry(QRect(80, 140, 16, 21))
        self.ast_dni = QLabel(MarcarSalida)
        self.ast_dni.setObjectName(u"ast_dni")
        self.ast_dni.setGeometry(QRect(200, 140, 16, 21))
        self.ast_autoriza = QLabel(MarcarSalida)
        self.ast_autoriza.setObjectName(u"ast_autoriza")
        self.ast_autoriza.setGeometry(QRect(120, 70, 16, 21))
        self.ast_aquienvisita = QLabel(MarcarSalida)
        self.ast_aquienvisita.setObjectName(u"ast_aquienvisita")
        self.ast_aquienvisita.setGeometry(QRect(560, 70, 16, 21))
        self.ast_area = QLabel(MarcarSalida)
        self.ast_area.setObjectName(u"ast_area")
        self.ast_area.setGeometry(QRect(960, 70, 16, 21))
        self.ast_entidadempresa = QLabel(MarcarSalida)
        self.ast_entidadempresa.setObjectName(u"ast_entidadempresa")
        self.ast_entidadempresa.setGeometry(QRect(970, 140, 16, 21))
        self.ast_piso = QLabel(MarcarSalida)
        self.ast_piso.setObjectName(u"ast_piso")
        self.ast_piso.setGeometry(QRect(930, 210, 16, 21))
        self.ast_estado = QLabel(MarcarSalida)
        self.ast_estado.setObjectName(u"ast_estado")
        self.ast_estado.setGeometry(QRect(1100, 210, 16, 21))
        self.label_nota_obligatoria = QLabel(MarcarSalida)
        self.label_nota_obligatoria.setObjectName(u"label_nota_obligatoria")
        self.label_nota_obligatoria.setGeometry(QRect(20, 480, 281, 21))
        self.motivoVisitaLineEdit = QLineEdit(MarcarSalida)
        self.motivoVisitaLineEdit.setObjectName(u"motivoVisitaLineEdit")
        self.motivoVisitaLineEdit.setGeometry(QRect(400, 230, 461, 31))
        self.motivoVisitaLineEdit.setFont(font1)
        self.ast_horaSalida = QLabel(MarcarSalida)
        self.ast_horaSalida.setObjectName(u"ast_horaSalida")
        self.ast_horaSalida.setGeometry(QRect(360, 210, 16, 21))
        self.label_advertencia_dni = QLabel(MarcarSalida)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(20, 480, 281, 21))
        self.areaVisitadaLineEdit = QLineEdit(MarcarSalida)
        self.areaVisitadaLineEdit.setObjectName(u"areaVisitadaLineEdit")
        self.areaVisitadaLineEdit.setGeometry(QRect(820, 90, 371, 31))
        self.areaVisitadaLineEdit.setFont(font1)
        QWidget.setTabOrder(self.titleLineEdit, self.categoryLineEdit)
        QWidget.setTabOrder(self.categoryLineEdit, self.dateEditNuevo)
        QWidget.setTabOrder(self.dateEditNuevo, self.dniLineEdit)
        QWidget.setTabOrder(self.dniLineEdit, self.nombreVisitanteLineEdit)
        QWidget.setTabOrder(self.nombreVisitanteLineEdit, self.categoryLineEditEntidadEmpresa)
        QWidget.setTabOrder(self.categoryLineEditEntidadEmpresa, self.horaIngresoLineEdit)
        QWidget.setTabOrder(self.horaIngresoLineEdit, self.horaSalidaLineEdit)
        QWidget.setTabOrder(self.horaSalidaLineEdit, self.motivoVisitaLineEdit)
        QWidget.setTabOrder(self.motivoVisitaLineEdit, self.comboBoxPiso)
        QWidget.setTabOrder(self.comboBoxPiso, self.comboBoxEstado)
        QWidget.setTabOrder(self.comboBoxEstado, self.descriptionTextedit)
        QWidget.setTabOrder(self.descriptionTextedit, self.editButton)
        QWidget.setTabOrder(self.editButton, self.cancelButton)

        self.retranslateUi(MarcarSalida)

        QMetaObject.connectSlotsByName(MarcarSalida)
    # setupUi

    def retranslateUi(self, MarcarSalida):
        MarcarSalida.setWindowTitle(QCoreApplication.translate("MarcarSalida", u"Marcar Salida", None))
        self.label.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">MARCAR SALIDA</span></p></body></html>", None))
        self.label_autoriza.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">AUTORIZA:</span></p></body></html>", None))
        self.titleLineEdit.setPlaceholderText("")
        self.editButton.setText(QCoreApplication.translate("MarcarSalida", u"MARCAR SALIDA", None))
        self.cancelButton.setText(QCoreApplication.translate("MarcarSalida", u"CANCELAR", None))
        self.label_aquienvisita.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">A QUIEN VISITA:</span></p></body></html>", None))
        self.label_area.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">\u00c1REA VISITADA:</span></p></body></html>", None))
        self.label_fecha.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">FECHA:</span></p></body></html>", None))
        self.label_visitante.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">APELLIDOS Y NOMBRES DEL VISITANTE:</span></p></body></html>", None))
        self.label_observaciones.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OBSERVACIONES:</span></p></body></html>", None))
        self.label_entidad.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ENTIDAD / EMPRESA:</span></p></body></html>", None))
        self.label_horaIngreso.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">HORA DE INGRESO:</span></p></body></html>", None))
        self.label_horaSalida.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">HORA DE SALIDA:</span></p></body></html>", None))
        self.label_motivoVisita.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">MOTIVO DE LA VISITA:</span></p></body></html>", None))
        self.label_dni.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">DNI:</span></p></body></html>", None))
        self.label_piso.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">PISO:</span></p></body></html>", None))
        self.label_estado.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ESTADO:</span></p></body></html>", None))
        self.ast_motivo.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_visitante.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_horaingreso.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_fecha.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_dni.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_autoriza.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_aquienvisita.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_area.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_entidadempresa.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_piso.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.ast_estado.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_nota_obligatoria.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) Estos campos son obligatorios</span></p></body></html>", None))
        self.ast_horaSalida.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("MarcarSalida", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">(*) El DNI debe tener 8 d\u00edgitos</span></p></body></html>", None))
    # retranslateUi

