# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ListBookForm(object):
    def setupUi(self, ListBookForm):
        if not ListBookForm.objectName():
            ListBookForm.setObjectName(u"ListBookForm")
        ListBookForm.resize(1309, 689)
        ListBookForm.setToolTipDuration(1)
        self.consultaMasiva = QTabWidget(ListBookForm)
        self.consultaMasiva.setObjectName(u"consultaMasiva")
        self.consultaMasiva.setGeometry(QRect(10, 0, 1341, 681))
        self.consultaMasiva.setToolTipDuration(-2)
        self.consultaMasiva.setAutoFillBackground(True)
        self.consultaMasiva.setStyleSheet(u"QTabWidget::pane { \n"
"   border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  background: #D7D0D0;\n"
"  color: black;\n"
"  padding: 5px;\n"
" }\n"
"QTabBar::tab:selected {\n"
"  background: red;\n"
"  color: white;\n"
" }\n"
"\n"
"QTabWidget::tab-bar {\n"
"   border: 1px solid black;\n"
"}")
        self.consultaMasiva.setTabPosition(QTabWidget.South)
        self.consultaMasiva.setTabShape(QTabWidget.Rounded)
        self.consultaMasiva.setElideMode(Qt.ElideNone)
        self.consultaMasiva.setUsesScrollButtons(True)
        self.consultaMasiva.setDocumentMode(True)
        self.consultaMasiva.setTabsClosable(False)
        self.consultaMasiva.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 630, 141, 16))
        font = QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.buttonsFrame = QFrame(self.tab)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setGeometry(QRect(0, 0, 1291, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonsFrame.sizePolicy().hasHeightForWidth())
        self.buttonsFrame.setSizePolicy(sizePolicy)
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.buttonsFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 10, 1281, 41))
        self.label_7.setStyleSheet(u"background-color: red;")
        self.tableGeneral = QTableWidget(self.tab)
        self.tableGeneral.setObjectName(u"tableGeneral")
        self.tableGeneral.setGeometry(QRect(0, 140, 1281, 491))
        self.tableGeneral.setAutoFillBackground(True)
        self.tableGeneral.setLineWidth(5)
        self.tableGeneral.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableGeneral.setTextElideMode(Qt.ElideLeft)
        self.tableGeneral.horizontalHeader().setMinimumSectionSize(10)
        self.labelNumeroRegistros = QLabel(self.tab)
        self.labelNumeroRegistros.setObjectName(u"labelNumeroRegistros")
        self.labelNumeroRegistros.setGeometry(QRect(150, 630, 47, 16))
        self.labelNumeroRegistros.setFont(font)
        self.btnBuscar = QPushButton(self.tab)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(1120, 70, 41, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.btnBuscar.setFont(font1)
        self.btnBuscar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBuscar.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #00AAFF;\n"
"	background-color:#00AAFF;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"./assets/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBuscar.setIcon(icon)
        self.btnBuscar.setIconSize(QSize(25, 25))
        self.btnActualizar = QPushButton(self.tab)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setGeometry(QRect(1170, 70, 41, 41))
        self.btnActualizar.setFont(font1)
        self.btnActualizar.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #1D6F42;\n"
"	background-color:#26914A;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#1D6F42;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualizar.setIcon(icon1)
        self.btnActualizar.setIconSize(QSize(25, 25))
        self.label_32 = QLabel(self.tab)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(390, 100, 221, 21))
        font2 = QFont()
        font2.setPointSize(11)
        self.label_32.setFont(font2)
        self.label_33 = QLabel(self.tab)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(640, 100, 111, 21))
        self.label_33.setFont(font2)
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(200, 100, 101, 21))
        self.label_9.setFont(font2)
        self.inputNombres = QLineEdit(self.tab)
        self.inputNombres.setObjectName(u"inputNombres")
        self.inputNombres.setGeometry(QRect(200, 70, 181, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.inputNombres.setFont(font3)
        self.inputApellidoPaterno = QLineEdit(self.tab)
        self.inputApellidoPaterno.setObjectName(u"inputApellidoPaterno")
        self.inputApellidoPaterno.setGeometry(QRect(390, 70, 241, 31))
        self.inputApellidoPaterno.setFont(font3)
        self.btnDescargaExcel = QPushButton(self.tab)
        self.btnDescargaExcel.setObjectName(u"btnDescargaExcel")
        self.btnDescargaExcel.setGeometry(QRect(1220, 70, 61, 41))
        self.btnDescargaExcel.setFont(font1)
        self.btnDescargaExcel.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	background-color:white;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/icon_excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDescargaExcel.setIcon(icon2)
        self.btnDescargaExcel.setIconSize(QSize(50, 50))
        self.inputApellidoMaterno = QLineEdit(self.tab)
        self.inputApellidoMaterno.setObjectName(u"inputApellidoMaterno")
        self.inputApellidoMaterno.setGeometry(QRect(640, 70, 231, 31))
        self.inputApellidoMaterno.setFont(font3)
        self.inputDNI = QLineEdit(self.tab)
        self.inputDNI.setObjectName(u"inputDNI")
        self.inputDNI.setGeometry(QRect(0, 70, 181, 31))
        self.inputDNI.setFont(font3)
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 100, 101, 21))
        self.label_10.setFont(font2)
        self.consultaMasiva.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.buttonsFrame_2 = QFrame(self.tab_2)
        self.buttonsFrame_2.setObjectName(u"buttonsFrame_2")
        self.buttonsFrame_2.setGeometry(QRect(0, 0, 1291, 61))
        sizePolicy.setHeightForWidth(self.buttonsFrame_2.sizePolicy().hasHeightForWidth())
        self.buttonsFrame_2.setSizePolicy(sizePolicy)
        self.buttonsFrame_2.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame_2.setFrameShadow(QFrame.Raised)
        self.btnActualizarPreventivo = QPushButton(self.buttonsFrame_2)
        self.btnActualizarPreventivo.setObjectName(u"btnActualizarPreventivo")
        self.btnActualizarPreventivo.setGeometry(QRect(1170, 100, 151, 41))
        self.btnActualizarPreventivo.setFont(font1)
        self.btnActualizarPreventivo.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #1D6F42;\n"
"	background-color:#26914A;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#1D6F42;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"")
        self.btnActualizarPreventivo.setIcon(icon1)
        self.btnActualizarPreventivo.setIconSize(QSize(25, 25))
        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 10, 1281, 41))
        self.label_18.setStyleSheet(u"background-color: green;")
        self.tableMasiva1 = QTableWidget(self.tab_2)
        self.tableMasiva1.setObjectName(u"tableMasiva1")
        self.tableMasiva1.setGeometry(QRect(0, 110, 1281, 521))
        self.tableMasiva1.setAutoFillBackground(True)
        self.tableMasiva1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableMasiva1.setTextElideMode(Qt.ElideLeft)
        self.tableMasiva1.horizontalHeader().setMinimumSectionSize(10)
        self.label_20 = QLabel(self.tab_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 630, 141, 16))
        self.label_20.setFont(font)
        self.labelNumeroRegistroMasiva1 = QLabel(self.tab_2)
        self.labelNumeroRegistroMasiva1.setObjectName(u"labelNumeroRegistroMasiva1")
        self.labelNumeroRegistroMasiva1.setGeometry(QRect(150, 630, 47, 16))
        self.labelNumeroRegistroMasiva1.setFont(font)
        self.btnConsultaMasiva = QPushButton(self.tab_2)
        self.btnConsultaMasiva.setObjectName(u"btnConsultaMasiva")
        self.btnConsultaMasiva.setGeometry(QRect(830, 60, 211, 41))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setWeight(75)
        self.btnConsultaMasiva.setFont(font4)
        self.btnConsultaMasiva.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnConsultaMasiva.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #00AAFF;\n"
"	background-color:#000000;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/uploadv2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnConsultaMasiva.setIcon(icon3)
        self.btnConsultaMasiva.setIconSize(QSize(30, 30))
        self.btnDescargaExcel_2 = QPushButton(self.tab_2)
        self.btnDescargaExcel_2.setObjectName(u"btnDescargaExcel_2")
        self.btnDescargaExcel_2.setGeometry(QRect(1050, 60, 231, 41))
        self.btnDescargaExcel_2.setFont(font4)
        self.btnDescargaExcel_2.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	background-color:white;\n"
"	font-weight: bold;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"")
        self.btnDescargaExcel_2.setIcon(icon2)
        self.btnDescargaExcel_2.setIconSize(QSize(50, 50))
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 70, 821, 21))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_11.setFont(font5)
        self.consultaMasiva.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2 = QTabWidget(self.tab_4)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 1341, 681))
        self.tabWidget_2.setToolTipDuration(-2)
        self.tabWidget_2.setAutoFillBackground(True)
        self.tabWidget_2.setStyleSheet(u"QTabWidget::pane { \n"
"   border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  background: #D7D0D0;\n"
"  color: black;\n"
"  padding: 5px;\n"
" }\n"
"QTabBar::tab:selected {\n"
"  background: red;\n"
"  color: white;\n"
" }\n"
"\n"
"QTabWidget::tab-bar {\n"
"   border: 1px solid black;\n"
"}")
        self.tabWidget_2.setTabPosition(QTabWidget.South)
        self.tabWidget_2.setTabShape(QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(Qt.ElideNone)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setDocumentMode(True)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(True)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.label_29 = QLabel(self.tab_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(0, 630, 141, 16))
        self.label_29.setFont(font)
        self.buttonsFrame_4 = QFrame(self.tab_5)
        self.buttonsFrame_4.setObjectName(u"buttonsFrame_4")
        self.buttonsFrame_4.setGeometry(QRect(0, 0, 1291, 61))
        sizePolicy.setHeightForWidth(self.buttonsFrame_4.sizePolicy().hasHeightForWidth())
        self.buttonsFrame_4.setSizePolicy(sizePolicy)
        self.buttonsFrame_4.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame_4.setFrameShadow(QFrame.Raised)
        self.label_30 = QLabel(self.buttonsFrame_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(-40, 10, 1321, 41))
        self.label_30.setStyleSheet(u"background-color: black;")
        self.booksQtyLabel_4 = QLabel(self.tab_5)
        self.booksQtyLabel_4.setObjectName(u"booksQtyLabel_4")
        self.booksQtyLabel_4.setGeometry(QRect(150, 630, 47, 16))
        self.booksQtyLabel_4.setFont(font)
        self.tableMasiva2 = QTableWidget(self.tab_5)
        self.tableMasiva2.setObjectName(u"tableMasiva2")
        self.tableMasiva2.setGeometry(QRect(-30, 110, 1311, 521))
        self.tableMasiva2.setAutoFillBackground(True)
        self.tableMasiva2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableMasiva2.setTextElideMode(Qt.ElideLeft)
        self.tableMasiva2.horizontalHeader().setMinimumSectionSize(10)
        self.btnConsultaMasiva_3 = QPushButton(self.tab_5)
        self.btnConsultaMasiva_3.setObjectName(u"btnConsultaMasiva_3")
        self.btnConsultaMasiva_3.setGeometry(QRect(530, 60, 181, 41))
        self.btnConsultaMasiva_3.setFont(font4)
        self.btnConsultaMasiva_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnConsultaMasiva_3.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #00AAFF;\n"
"	background-color:#000000;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"")
        self.btnConsultaMasiva_3.setIcon(icon3)
        self.btnConsultaMasiva_3.setIconSize(QSize(30, 30))
        self.label_12 = QLabel(self.tab_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 70, 491, 21))
        self.label_12.setFont(font5)
        self.btnDescargaExcel_3 = QPushButton(self.tab_5)
        self.btnDescargaExcel_3.setObjectName(u"btnDescargaExcel_3")
        self.btnDescargaExcel_3.setGeometry(QRect(720, 60, 181, 41))
        self.btnDescargaExcel_3.setFont(font4)
        self.btnDescargaExcel_3.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	background-color:white;\n"
"	font-weight: bold;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"")
        self.btnDescargaExcel_3.setIcon(icon2)
        self.btnDescargaExcel_3.setIconSize(QSize(50, 50))
        self.btnGenerarPadron = QPushButton(self.tab_5)
        self.btnGenerarPadron.setObjectName(u"btnGenerarPadron")
        self.btnGenerarPadron.setGeometry(QRect(910, 60, 181, 41))
        self.btnGenerarPadron.setFont(font4)
        self.btnGenerarPadron.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: BLACK;\n"
"	background-color:WHITE;\n"
"	font-weight: bold;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/add-book-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnGenerarPadron.setIcon(icon4)
        self.btnGenerarPadron.setIconSize(QSize(40, 50))
        self.btnGenerarBanco = QPushButton(self.tab_5)
        self.btnGenerarBanco.setObjectName(u"btnGenerarBanco")
        self.btnGenerarBanco.setGeometry(QRect(1100, 60, 181, 41))
        self.btnGenerarBanco.setFont(font4)
        self.btnGenerarBanco.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: BLACK;\n"
"	background-color:WHITE;\n"
"	font-weight: bold;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"./assets/icons/generatebanck.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnGenerarBanco.setIcon(icon5)
        self.btnGenerarBanco.setIconSize(QSize(35, 35))
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.searchButton_9 = QPushButton(self.tab_6)
        self.searchButton_9.setObjectName(u"searchButton_9")
        self.searchButton_9.setGeometry(QRect(1170, 150, 151, 41))
        self.searchButton_9.setFont(font1)
        self.searchButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton_9.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #00AAFF;\n"
"	background-color:#00AAFF;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"")
        self.searchButton_9.setIcon(icon)
        self.searchButton_9.setIconSize(QSize(25, 25))
        self.parameterLineEditMotivo_5 = QLineEdit(self.tab_6)
        self.parameterLineEditMotivo_5.setObjectName(u"parameterLineEditMotivo_5")
        self.parameterLineEditMotivo_5.setGeometry(QRect(700, 160, 301, 31))
        self.parameterLineEditMotivo_5.setFont(font3)
        self.parameterLineEditDNI_5 = QLineEdit(self.tab_6)
        self.parameterLineEditDNI_5.setObjectName(u"parameterLineEditDNI_5")
        self.parameterLineEditDNI_5.setGeometry(QRect(0, 160, 101, 31))
        self.parameterLineEditDNI_5.setFont(font3)
        self.label_37 = QLabel(self.tab_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(0, 190, 31, 21))
        self.label_37.setFont(font2)
        self.parameterLineEditFecha_5 = QLineEdit(self.tab_6)
        self.parameterLineEditFecha_5.setObjectName(u"parameterLineEditFecha_5")
        self.parameterLineEditFecha_5.setGeometry(QRect(200, 160, 111, 31))
        self.parameterLineEditFecha_5.setFont(font3)
        self.parameterLineEditVisitante_5 = QLineEdit(self.tab_6)
        self.parameterLineEditVisitante_5.setObjectName(u"parameterLineEditVisitante_5")
        self.parameterLineEditVisitante_5.setGeometry(QRect(320, 160, 371, 31))
        self.parameterLineEditVisitante_5.setFont(font3)
        self.label_38 = QLabel(self.tab_6)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(700, 190, 191, 21))
        self.label_38.setFont(font2)
        self.label_39 = QLabel(self.tab_6)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(1010, 190, 101, 21))
        self.label_39.setFont(font2)
        self.ast_dni_5 = QLabel(self.tab_6)
        self.ast_dni_5.setObjectName(u"ast_dni_5")
        self.ast_dni_5.setGeometry(QRect(30, 190, 21, 21))
        self.ast_dni_5.setFont(font)
        self.label_40 = QLabel(self.tab_6)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(200, 190, 81, 21))
        self.label_40.setFont(font2)
        self.searchByPiso_5 = QComboBox(self.tab_6)
        self.searchByPiso_5.setObjectName(u"searchByPiso_5")
        self.searchByPiso_5.setGeometry(QRect(110, 160, 81, 31))
        self.searchByPiso_5.setFont(font3)
        self.label_41 = QLabel(self.tab_6)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(320, 190, 191, 21))
        self.label_41.setFont(font2)
        self.searchByEstado_5 = QComboBox(self.tab_6)
        self.searchByEstado_5.setObjectName(u"searchByEstado_5")
        self.searchByEstado_5.setGeometry(QRect(1010, 160, 141, 31))
        self.searchByEstado_5.setFont(font3)
        self.buttonsFrame_5 = QFrame(self.tab_6)
        self.buttonsFrame_5.setObjectName(u"buttonsFrame_5")
        self.buttonsFrame_5.setGeometry(QRect(0, 0, 1331, 151))
        sizePolicy.setHeightForWidth(self.buttonsFrame_5.sizePolicy().hasHeightForWidth())
        self.buttonsFrame_5.setSizePolicy(sizePolicy)
        self.buttonsFrame_5.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame_5.setFrameShadow(QFrame.Raised)
        self.open_new_button_9 = QPushButton(self.buttonsFrame_5)
        self.open_new_button_9.setObjectName(u"open_new_button_9")
        self.open_new_button_9.setGeometry(QRect(20, 50, 201, 91))
        self.open_new_button_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_9.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"./assets/icons/icon_nuevo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_new_button_9.setIcon(icon6)
        self.open_new_button_9.setIconSize(QSize(200, 200))
        self.open_new_button_9.setFlat(True)
        self.open_new_button_10 = QPushButton(self.buttonsFrame_5)
        self.open_new_button_10.setObjectName(u"open_new_button_10")
        self.open_new_button_10.setGeometry(QRect(230, 50, 201, 91))
        self.open_new_button_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_10.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"./assets/icons/icon_mod.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_new_button_10.setIcon(icon7)
        self.open_new_button_10.setIconSize(QSize(200, 200))
        self.open_new_button_10.setFlat(True)
        self.delete_book_button_5 = QPushButton(self.buttonsFrame_5)
        self.delete_book_button_5.setObjectName(u"delete_book_button_5")
        self.delete_book_button_5.setGeometry(QRect(440, 50, 201, 91))
        self.delete_book_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_book_button_5.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"./assets/icons/icon_del.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_book_button_5.setIcon(icon8)
        self.delete_book_button_5.setIconSize(QSize(200, 200))
        self.delete_book_button_5.setFlat(True)
        self.excel_generate_button_5 = QPushButton(self.buttonsFrame_5)
        self.excel_generate_button_5.setObjectName(u"excel_generate_button_5")
        self.excel_generate_button_5.setGeometry(QRect(850, 50, 201, 91))
        self.excel_generate_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.excel_generate_button_5.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"./assets/icons/icon_gen_reporte.png", QSize(), QIcon.Normal, QIcon.Off)
        self.excel_generate_button_5.setIcon(icon9)
        self.excel_generate_button_5.setIconSize(QSize(200, 200))
        self.excel_generate_button_5.setFlat(True)
        self.marcar_salida_button_5 = QPushButton(self.buttonsFrame_5)
        self.marcar_salida_button_5.setObjectName(u"marcar_salida_button_5")
        self.marcar_salida_button_5.setGeometry(QRect(650, 50, 201, 91))
        self.marcar_salida_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.marcar_salida_button_5.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"./assets/icons/icon_marcar_exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marcar_salida_button_5.setIcon(icon10)
        self.marcar_salida_button_5.setIconSize(QSize(200, 200))
        self.marcar_salida_button_5.setFlat(True)
        self.searchButton_10 = QPushButton(self.buttonsFrame_5)
        self.searchButton_10.setObjectName(u"searchButton_10")
        self.searchButton_10.setGeometry(QRect(1170, 100, 151, 41))
        self.searchButton_10.setFont(font1)
        self.searchButton_10.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #1D6F42;\n"
"	background-color:#26914A;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#1D6F42;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"")
        self.searchButton_10.setIcon(icon1)
        self.searchButton_10.setIconSize(QSize(25, 25))
        self.label_42 = QLabel(self.tab_6)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(110, 190, 81, 21))
        self.label_42.setFont(font2)
        self.label_43 = QLabel(self.tab_6)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(0, 10, 1321, 41))
        self.label_43.setStyleSheet(u"background-color: green;")
        self.listBooksTable_5 = QTableWidget(self.tab_6)
        self.listBooksTable_5.setObjectName(u"listBooksTable_5")
        self.listBooksTable_5.setGeometry(QRect(0, 220, 1321, 411))
        self.listBooksTable_5.setAutoFillBackground(True)
        self.listBooksTable_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listBooksTable_5.setTextElideMode(Qt.ElideLeft)
        self.listBooksTable_5.horizontalHeader().setMinimumSectionSize(10)
        self.label_advertencia_sin_resultados_5 = QLabel(self.tab_6)
        self.label_advertencia_sin_resultados_5.setObjectName(u"label_advertencia_sin_resultados_5")
        self.label_advertencia_sin_resultados_5.setGeometry(QRect(790, 140, 351, 21))
        self.label_advertencia_sin_resultados_5.setFont(font)
        self.label_44 = QLabel(self.tab_6)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(0, 630, 141, 16))
        self.label_44.setFont(font)
        self.booksQtyLabel_5 = QLabel(self.tab_6)
        self.booksQtyLabel_5.setObjectName(u"booksQtyLabel_5")
        self.booksQtyLabel_5.setGeometry(QRect(150, 630, 47, 16))
        self.booksQtyLabel_5.setFont(font)
        self.label_advertencia_filtros_5 = QLabel(self.tab_6)
        self.label_advertencia_filtros_5.setObjectName(u"label_advertencia_filtros_5")
        self.label_advertencia_filtros_5.setGeometry(QRect(730, 140, 431, 21))
        self.label_advertencia_filtros_5.setFont(font)
        self.label_advertencia_dni_5 = QLabel(self.tab_6)
        self.label_advertencia_dni_5.setObjectName(u"label_advertencia_dni_5")
        self.label_advertencia_dni_5.setGeometry(QRect(800, 140, 351, 21))
        self.label_advertencia_dni_5.setFont(font)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.buttonsFrame_6 = QFrame(self.tab_8)
        self.buttonsFrame_6.setObjectName(u"buttonsFrame_6")
        self.buttonsFrame_6.setGeometry(QRect(0, 0, 1331, 151))
        sizePolicy.setHeightForWidth(self.buttonsFrame_6.sizePolicy().hasHeightForWidth())
        self.buttonsFrame_6.setSizePolicy(sizePolicy)
        self.buttonsFrame_6.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame_6.setFrameShadow(QFrame.Raised)
        self.open_new_button_11 = QPushButton(self.buttonsFrame_6)
        self.open_new_button_11.setObjectName(u"open_new_button_11")
        self.open_new_button_11.setGeometry(QRect(20, 50, 201, 91))
        self.open_new_button_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_11.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.open_new_button_11.setIcon(icon6)
        self.open_new_button_11.setIconSize(QSize(200, 200))
        self.open_new_button_11.setFlat(True)
        self.open_new_button_12 = QPushButton(self.buttonsFrame_6)
        self.open_new_button_12.setObjectName(u"open_new_button_12")
        self.open_new_button_12.setGeometry(QRect(230, 50, 201, 91))
        self.open_new_button_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_12.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.open_new_button_12.setIcon(icon7)
        self.open_new_button_12.setIconSize(QSize(200, 200))
        self.open_new_button_12.setFlat(True)
        self.delete_book_button_6 = QPushButton(self.buttonsFrame_6)
        self.delete_book_button_6.setObjectName(u"delete_book_button_6")
        self.delete_book_button_6.setGeometry(QRect(440, 50, 201, 91))
        self.delete_book_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_book_button_6.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.delete_book_button_6.setIcon(icon8)
        self.delete_book_button_6.setIconSize(QSize(200, 200))
        self.delete_book_button_6.setFlat(True)
        self.excel_generate_button_6 = QPushButton(self.buttonsFrame_6)
        self.excel_generate_button_6.setObjectName(u"excel_generate_button_6")
        self.excel_generate_button_6.setGeometry(QRect(850, 50, 201, 91))
        self.excel_generate_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.excel_generate_button_6.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.excel_generate_button_6.setIcon(icon9)
        self.excel_generate_button_6.setIconSize(QSize(200, 200))
        self.excel_generate_button_6.setFlat(True)
        self.marcar_salida_button_6 = QPushButton(self.buttonsFrame_6)
        self.marcar_salida_button_6.setObjectName(u"marcar_salida_button_6")
        self.marcar_salida_button_6.setGeometry(QRect(650, 50, 201, 91))
        self.marcar_salida_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.marcar_salida_button_6.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.marcar_salida_button_6.setIcon(icon10)
        self.marcar_salida_button_6.setIconSize(QSize(200, 200))
        self.marcar_salida_button_6.setFlat(True)
        self.searchButton_11 = QPushButton(self.buttonsFrame_6)
        self.searchButton_11.setObjectName(u"searchButton_11")
        self.searchButton_11.setGeometry(QRect(1170, 110, 151, 41))
        self.searchButton_11.setFont(font1)
        self.searchButton_11.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #1D6F42;\n"
"	background-color:#26914A;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#1D6F42;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"")
        self.searchButton_11.setIcon(icon1)
        self.searchButton_11.setIconSize(QSize(25, 25))
        self.label_45 = QLabel(self.buttonsFrame_6)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(0, 10, 1321, 41))
        self.label_45.setStyleSheet(u"background-color: BLUE;")
        self.label_advertencia_filtros_6 = QLabel(self.tab_8)
        self.label_advertencia_filtros_6.setObjectName(u"label_advertencia_filtros_6")
        self.label_advertencia_filtros_6.setGeometry(QRect(740, 140, 431, 21))
        self.label_advertencia_filtros_6.setFont(font)
        self.label_46 = QLabel(self.tab_8)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(110, 190, 81, 21))
        self.label_46.setFont(font2)
        self.searchByPiso_6 = QComboBox(self.tab_8)
        self.searchByPiso_6.setObjectName(u"searchByPiso_6")
        self.searchByPiso_6.setGeometry(QRect(110, 160, 81, 31))
        self.searchByPiso_6.setFont(font3)
        self.label_47 = QLabel(self.tab_8)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(200, 190, 81, 21))
        self.label_47.setFont(font2)
        self.searchByEstado_6 = QComboBox(self.tab_8)
        self.searchByEstado_6.setObjectName(u"searchByEstado_6")
        self.searchByEstado_6.setGeometry(QRect(1010, 160, 141, 31))
        self.searchByEstado_6.setFont(font3)
        self.label_48 = QLabel(self.tab_8)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(700, 190, 191, 21))
        self.label_48.setFont(font2)
        self.parameterLineEditDNI_6 = QLineEdit(self.tab_8)
        self.parameterLineEditDNI_6.setObjectName(u"parameterLineEditDNI_6")
        self.parameterLineEditDNI_6.setGeometry(QRect(0, 160, 101, 31))
        self.parameterLineEditDNI_6.setFont(font3)
        self.parameterLineEditFecha_6 = QLineEdit(self.tab_8)
        self.parameterLineEditFecha_6.setObjectName(u"parameterLineEditFecha_6")
        self.parameterLineEditFecha_6.setGeometry(QRect(200, 160, 111, 31))
        self.parameterLineEditFecha_6.setFont(font3)
        self.parameterLineEditMotivo_6 = QLineEdit(self.tab_8)
        self.parameterLineEditMotivo_6.setObjectName(u"parameterLineEditMotivo_6")
        self.parameterLineEditMotivo_6.setGeometry(QRect(700, 160, 301, 31))
        self.parameterLineEditMotivo_6.setFont(font3)
        self.label_49 = QLabel(self.tab_8)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(0, 190, 81, 21))
        self.label_49.setFont(font2)
        self.parameterLineEditVisitante_6 = QLineEdit(self.tab_8)
        self.parameterLineEditVisitante_6.setObjectName(u"parameterLineEditVisitante_6")
        self.parameterLineEditVisitante_6.setGeometry(QRect(320, 160, 371, 31))
        self.parameterLineEditVisitante_6.setFont(font3)
        self.label_advertencia_sin_resultados_6 = QLabel(self.tab_8)
        self.label_advertencia_sin_resultados_6.setObjectName(u"label_advertencia_sin_resultados_6")
        self.label_advertencia_sin_resultados_6.setGeometry(QRect(790, 140, 351, 21))
        self.label_advertencia_sin_resultados_6.setFont(font)
        self.searchButton_12 = QPushButton(self.tab_8)
        self.searchButton_12.setObjectName(u"searchButton_12")
        self.searchButton_12.setGeometry(QRect(1170, 160, 151, 41))
        self.searchButton_12.setFont(font1)
        self.searchButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton_12.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #00AAFF;\n"
"	background-color:#00AAFF;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"")
        self.searchButton_12.setIcon(icon)
        self.searchButton_12.setIconSize(QSize(25, 25))
        self.ast_dni_6 = QLabel(self.tab_8)
        self.ast_dni_6.setObjectName(u"ast_dni_6")
        self.ast_dni_6.setGeometry(QRect(30, 190, 21, 21))
        self.ast_dni_6.setFont(font)
        self.label_50 = QLabel(self.tab_8)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(320, 190, 191, 21))
        self.label_50.setFont(font2)
        self.label_51 = QLabel(self.tab_8)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(1010, 190, 101, 21))
        self.label_51.setFont(font2)
        self.listBooksTable_6 = QTableWidget(self.tab_8)
        self.listBooksTable_6.setObjectName(u"listBooksTable_6")
        self.listBooksTable_6.setGeometry(QRect(0, 220, 1321, 411))
        self.listBooksTable_6.setToolTipDuration(-1)
        self.listBooksTable_6.setAutoFillBackground(True)
        self.listBooksTable_6.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listBooksTable_6.setTextElideMode(Qt.ElideLeft)
        self.listBooksTable_6.horizontalHeader().setMinimumSectionSize(10)
        self.label_52 = QLabel(self.tab_8)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(0, 630, 141, 16))
        self.label_52.setFont(font)
        self.booksQtyLabel_6 = QLabel(self.tab_8)
        self.booksQtyLabel_6.setObjectName(u"booksQtyLabel_6")
        self.booksQtyLabel_6.setGeometry(QRect(150, 630, 47, 16))
        self.booksQtyLabel_6.setFont(font)
        self.label_advertencia_dni_6 = QLabel(self.tab_8)
        self.label_advertencia_dni_6.setObjectName(u"label_advertencia_dni_6")
        self.label_advertencia_dni_6.setGeometry(QRect(810, 140, 351, 21))
        self.label_advertencia_dni_6.setFont(font)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.consultaMasiva.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.buttonsFrame_3 = QFrame(self.tab_3)
        self.buttonsFrame_3.setObjectName(u"buttonsFrame_3")
        self.buttonsFrame_3.setGeometry(QRect(0, 0, 1331, 151))
        sizePolicy.setHeightForWidth(self.buttonsFrame_3.sizePolicy().hasHeightForWidth())
        self.buttonsFrame_3.setSizePolicy(sizePolicy)
        self.buttonsFrame_3.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame_3.setFrameShadow(QFrame.Raised)
        self.open_new_button_5 = QPushButton(self.buttonsFrame_3)
        self.open_new_button_5.setObjectName(u"open_new_button_5")
        self.open_new_button_5.setGeometry(QRect(20, 50, 201, 91))
        self.open_new_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_5.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        self.open_new_button_5.setIcon(icon6)
        self.open_new_button_5.setIconSize(QSize(200, 200))
        self.open_new_button_5.setFlat(True)
        self.label_21 = QLabel(self.buttonsFrame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 10, 1321, 41))
        self.label_21.setStyleSheet(u"background-color: BLUE;")
        self.label_28 = QLabel(self.tab_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(0, 630, 141, 16))
        self.label_28.setFont(font)
        self.booksQtyLabel_3 = QLabel(self.tab_3)
        self.booksQtyLabel_3.setObjectName(u"booksQtyLabel_3")
        self.booksQtyLabel_3.setGeometry(QRect(150, 630, 47, 16))
        self.booksQtyLabel_3.setFont(font)
        self.consultaMasiva.addTab(self.tab_3, "")
        QWidget.setTabOrder(self.inputDNI, self.inputNombres)
        QWidget.setTabOrder(self.inputNombres, self.inputApellidoPaterno)
        QWidget.setTabOrder(self.inputApellidoPaterno, self.inputApellidoMaterno)
        QWidget.setTabOrder(self.inputApellidoMaterno, self.btnBuscar)
        QWidget.setTabOrder(self.btnBuscar, self.btnActualizar)
        QWidget.setTabOrder(self.btnActualizar, self.btnDescargaExcel)
        QWidget.setTabOrder(self.btnDescargaExcel, self.btnActualizarPreventivo)
        QWidget.setTabOrder(self.btnActualizarPreventivo, self.tableMasiva1)
        QWidget.setTabOrder(self.tableMasiva1, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.searchButton_9)
        QWidget.setTabOrder(self.searchButton_9, self.parameterLineEditMotivo_5)
        QWidget.setTabOrder(self.parameterLineEditMotivo_5, self.parameterLineEditDNI_5)
        QWidget.setTabOrder(self.parameterLineEditDNI_5, self.parameterLineEditFecha_5)
        QWidget.setTabOrder(self.parameterLineEditFecha_5, self.parameterLineEditVisitante_5)
        QWidget.setTabOrder(self.parameterLineEditVisitante_5, self.searchByPiso_5)
        QWidget.setTabOrder(self.searchByPiso_5, self.searchByEstado_5)
        QWidget.setTabOrder(self.searchByEstado_5, self.open_new_button_9)
        QWidget.setTabOrder(self.open_new_button_9, self.open_new_button_10)
        QWidget.setTabOrder(self.open_new_button_10, self.delete_book_button_5)
        QWidget.setTabOrder(self.delete_book_button_5, self.excel_generate_button_5)
        QWidget.setTabOrder(self.excel_generate_button_5, self.marcar_salida_button_5)
        QWidget.setTabOrder(self.marcar_salida_button_5, self.searchButton_10)
        QWidget.setTabOrder(self.searchButton_10, self.listBooksTable_5)
        QWidget.setTabOrder(self.listBooksTable_5, self.open_new_button_11)
        QWidget.setTabOrder(self.open_new_button_11, self.open_new_button_12)
        QWidget.setTabOrder(self.open_new_button_12, self.delete_book_button_6)
        QWidget.setTabOrder(self.delete_book_button_6, self.excel_generate_button_6)
        QWidget.setTabOrder(self.excel_generate_button_6, self.marcar_salida_button_6)
        QWidget.setTabOrder(self.marcar_salida_button_6, self.searchButton_11)
        QWidget.setTabOrder(self.searchButton_11, self.searchByPiso_6)
        QWidget.setTabOrder(self.searchByPiso_6, self.searchByEstado_6)
        QWidget.setTabOrder(self.searchByEstado_6, self.parameterLineEditDNI_6)
        QWidget.setTabOrder(self.parameterLineEditDNI_6, self.parameterLineEditFecha_6)
        QWidget.setTabOrder(self.parameterLineEditFecha_6, self.parameterLineEditMotivo_6)
        QWidget.setTabOrder(self.parameterLineEditMotivo_6, self.parameterLineEditVisitante_6)
        QWidget.setTabOrder(self.parameterLineEditVisitante_6, self.searchButton_12)
        QWidget.setTabOrder(self.searchButton_12, self.listBooksTable_6)
        QWidget.setTabOrder(self.listBooksTable_6, self.open_new_button_5)
        QWidget.setTabOrder(self.open_new_button_5, self.consultaMasiva)
        QWidget.setTabOrder(self.consultaMasiva, self.tableGeneral)

        self.retranslateUi(ListBookForm)

        self.consultaMasiva.setCurrentIndex(2)
        self.btnBuscar.setDefault(True)
        self.btnActualizar.setDefault(True)
        self.btnDescargaExcel.setDefault(True)
        self.btnActualizarPreventivo.setDefault(True)
        self.btnConsultaMasiva.setDefault(True)
        self.btnDescargaExcel_2.setDefault(True)
        self.tabWidget_2.setCurrentIndex(0)
        self.btnConsultaMasiva_3.setDefault(True)
        self.btnDescargaExcel_3.setDefault(True)
        self.btnGenerarPadron.setDefault(True)
        self.btnGenerarBanco.setDefault(True)
        self.searchButton_9.setDefault(True)
        self.open_new_button_9.setDefault(True)
        self.open_new_button_10.setDefault(True)
        self.delete_book_button_5.setDefault(True)
        self.excel_generate_button_5.setDefault(True)
        self.marcar_salida_button_5.setDefault(True)
        self.searchButton_10.setDefault(True)
        self.open_new_button_11.setDefault(True)
        self.open_new_button_12.setDefault(True)
        self.delete_book_button_6.setDefault(True)
        self.excel_generate_button_6.setDefault(True)
        self.marcar_salida_button_6.setDefault(True)
        self.searchButton_11.setDefault(True)
        self.searchButton_12.setDefault(True)
        self.open_new_button_5.setDefault(True)


        QMetaObject.connectSlotsByName(ListBookForm)
    # setupUi

    def retranslateUi(self, ListBookForm):
        ListBookForm.setWindowTitle(QCoreApplication.translate("ListBookForm", u"Sistema de Busqueda Reniec", None))
        self.label_6.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">BUSQUEDA DNI</span></p></body></html>", None))
        self.labelNumeroRegistros.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.btnBuscar.setText("")
        self.btnActualizar.setText("")
        self.label_32.setText(QCoreApplication.translate("ListBookForm", u"Apellido Paterno", None))
        self.label_33.setText(QCoreApplication.translate("ListBookForm", u"Apellido Materno", None))
        self.label_9.setText(QCoreApplication.translate("ListBookForm", u"Nombres", None))
        self.btnDescargaExcel.setText("")
        self.label_10.setText(QCoreApplication.translate("ListBookForm", u"DNI", None))
        self.consultaMasiva.setTabText(self.consultaMasiva.indexOf(self.tab), QCoreApplication.translate("ListBookForm", u"CONSULTA INDIVIDUAL", None))
        self.btnActualizarPreventivo.setText(QCoreApplication.translate("ListBookForm", u" ACTUALIZAR", None))
        self.label_18.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">BUSQUEDA MASIVA</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.labelNumeroRegistroMasiva1.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.btnConsultaMasiva.setText(QCoreApplication.translate("ListBookForm", u"CONSULTA MASIVA", None))
        self.btnDescargaExcel_2.setText(QCoreApplication.translate("ListBookForm", u"DESCARGAR EXCEL", None))
        self.label_11.setText(QCoreApplication.translate("ListBookForm", u"SELECCIONE UN ARCHICO EXCEL CON UNA SOLA COLUMNA DENOMINADA \"DNI\"", None))
        self.consultaMasiva.setTabText(self.consultaMasiva.indexOf(self.tab_2), QCoreApplication.translate("ListBookForm", u"CONSULTA MASIVA", None))
        self.label_29.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">CONSULTA MASIVA TIPO 2</span></p></body></html>", None))
        self.booksQtyLabel_4.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.btnConsultaMasiva_3.setText(QCoreApplication.translate("ListBookForm", u"CONSULTA MASIVA", None))
        self.label_12.setText(QCoreApplication.translate("ListBookForm", u"SELECCIONE UN ARCHICO EXCEL CON EL FORMATO N\u00b01", None))
        self.btnDescargaExcel_3.setText(QCoreApplication.translate("ListBookForm", u"DESCARGAR EXCEL", None))
        self.btnGenerarPadron.setText(QCoreApplication.translate("ListBookForm", u"GENERAR PADR\u00d3N", None))
        self.btnGenerarBanco.setText(QCoreApplication.translate("ListBookForm", u"FORMATO BANCO", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("ListBookForm", u"VISITAS", None))
        self.searchButton_9.setText(QCoreApplication.translate("ListBookForm", u" BUSCAR", None))
        self.label_37.setText(QCoreApplication.translate("ListBookForm", u"DNI", None))
        self.label_38.setText(QCoreApplication.translate("ListBookForm", u"MOTIVO", None))
        self.label_39.setText(QCoreApplication.translate("ListBookForm", u"ESTADO", None))
        self.ast_dni_5.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ff0000;\">*</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("ListBookForm", u"FECHA", None))
        self.label_41.setText(QCoreApplication.translate("ListBookForm", u"NOMBRE DEL LOCADOR", None))
        self.open_new_button_9.setText("")
        self.open_new_button_10.setText("")
        self.delete_book_button_5.setText("")
        self.excel_generate_button_5.setText("")
        self.marcar_salida_button_5.setText("")
        self.searchButton_10.setText(QCoreApplication.translate("ListBookForm", u" ACTUALIZAR", None))
        self.label_42.setText(QCoreApplication.translate("ListBookForm", u"PISO", None))
        self.label_43.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">REGISTRO DE LOCADORES - FEBAN</span></p></body></html>", None))
        self.label_advertencia_sin_resultados_5.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">No existen registros con los par\u00e1metros brindados...</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.booksQtyLabel_5.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.label_advertencia_filtros_5.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-style:italic; color:#ff0000;\">\u00a1Ingrese datos en al menos uno de los campos para realizar la b\u00fasqueda!</span></p></body></html>", None))
        self.label_advertencia_dni_5.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">El DNI debe contener 8 d\u00edgitos!</span></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("ListBookForm", u"LOCADORES", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("ListBookForm", u"PERSONAL FEBAN", None))
        self.open_new_button_11.setText("")
        self.open_new_button_12.setText("")
        self.delete_book_button_6.setText("")
        self.excel_generate_button_6.setText("")
        self.marcar_salida_button_6.setText("")
        self.searchButton_11.setText(QCoreApplication.translate("ListBookForm", u" ACTUALIZAR", None))
        self.label_45.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">REGISTRO DE PERSONAL DE MANTENIMIENTO - FEBAN</span></p></body></html>", None))
        self.label_advertencia_filtros_6.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-style:italic; color:#ff0000;\">\u00a1Ingrese datos en al menos uno de los campos para realizar la b\u00fasqueda!</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("ListBookForm", u"PISO", None))
        self.label_47.setText(QCoreApplication.translate("ListBookForm", u"FECHA", None))
        self.label_48.setText(QCoreApplication.translate("ListBookForm", u"MOTIVO", None))
        self.label_49.setText(QCoreApplication.translate("ListBookForm", u"DNI", None))
        self.label_advertencia_sin_resultados_6.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">No existen registros con los par\u00e1metros brindados...</span></p></body></html>", None))
        self.searchButton_12.setText(QCoreApplication.translate("ListBookForm", u" BUSCAR", None))
        self.ast_dni_6.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ff0000;\">*</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("ListBookForm", u"NOMBRE DEL PERSONAL", None))
        self.label_51.setText(QCoreApplication.translate("ListBookForm", u"ESTADO", None))
        self.label_52.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.booksQtyLabel_6.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.label_advertencia_dni_6.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">El DNI debe contener 8 d\u00edgitos!</span></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("ListBookForm", u"MANTENIMIENTO", None))
        self.consultaMasiva.setTabText(self.consultaMasiva.indexOf(self.tab_4), QCoreApplication.translate("ListBookForm", u"CONSULTA MASIVA CON FORMATO", None))
        self.open_new_button_5.setText("")
        self.label_21.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">BUSQUEDA 3</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.booksQtyLabel_3.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.consultaMasiva.setTabText(self.consultaMasiva.indexOf(self.tab_3), QCoreApplication.translate("ListBookForm", u"Pag4", None))
    # retranslateUi

