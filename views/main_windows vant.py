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


class ListBookForm(object):
    def setupUi(self, ListBookForm):
        if not ListBookForm.objectName():
            ListBookForm.setObjectName(u"ListBookForm")
        ListBookForm.resize(1354, 690)
        ListBookForm.setToolTipDuration(1)
        self.tabWidget = QTabWidget(ListBookForm)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 1341, 681))
        self.tabWidget.setToolTipDuration(-2)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { \n"
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
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_advertencia_dni = QLabel(self.tab)
        self.label_advertencia_dni.setObjectName(u"label_advertencia_dni")
        self.label_advertencia_dni.setGeometry(QRect(800, 140, 351, 21))
        font = QFont()
        font.setPointSize(10)
        self.label_advertencia_dni.setFont(font)
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 630, 141, 16))
        self.label_6.setFont(font)
        self.buttonsFrame = QFrame(self.tab)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setGeometry(QRect(0, 0, 1331, 151))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonsFrame.sizePolicy().hasHeightForWidth())
        self.buttonsFrame.setSizePolicy(sizePolicy)
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.open_new_button = QPushButton(self.buttonsFrame)
        self.open_new_button.setObjectName(u"open_new_button")
        self.open_new_button.setGeometry(QRect(20, 50, 201, 91))
        self.open_new_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button.setStyleSheet(u"QPushButton:hover\n"
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
        icon = QIcon()
        icon.addFile(u"./assets/icons/icon_nuevo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_new_button.setIcon(icon)
        self.open_new_button.setIconSize(QSize(200, 200))
        self.open_new_button.setFlat(True)
        self.open_new_button_2 = QPushButton(self.buttonsFrame)
        self.open_new_button_2.setObjectName(u"open_new_button_2")
        self.open_new_button_2.setGeometry(QRect(230, 50, 201, 91))
        self.open_new_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_2.setStyleSheet(u"QPushButton:hover\n"
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
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/icon_mod.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_new_button_2.setIcon(icon1)
        self.open_new_button_2.setIconSize(QSize(200, 200))
        self.open_new_button_2.setFlat(True)
        self.delete_book_button = QPushButton(self.buttonsFrame)
        self.delete_book_button.setObjectName(u"delete_book_button")
        self.delete_book_button.setGeometry(QRect(440, 50, 201, 91))
        self.delete_book_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_book_button.setStyleSheet(u"QPushButton:hover\n"
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
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/icon_del.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_book_button.setIcon(icon2)
        self.delete_book_button.setIconSize(QSize(200, 200))
        self.delete_book_button.setFlat(True)
        self.label_7 = QLabel(self.buttonsFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 10, 1321, 41))
        self.label_7.setStyleSheet(u"background-color: red;")
        self.searchButton_2 = QPushButton(self.buttonsFrame)
        self.searchButton_2.setObjectName(u"searchButton_2")
        self.searchButton_2.setGeometry(QRect(1170, 100, 151, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.searchButton_2.setFont(font1)
        self.searchButton_2.setStyleSheet(u"QPushButton\n"
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
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton_2.setIcon(icon3)
        self.searchButton_2.setIconSize(QSize(25, 25))
        self.excel_generate_button = QPushButton(self.buttonsFrame)
        self.excel_generate_button.setObjectName(u"excel_generate_button")
        self.excel_generate_button.setGeometry(QRect(850, 50, 201, 91))
        self.excel_generate_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.excel_generate_button.setStyleSheet(u"QPushButton:hover\n"
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
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/icon_gen_reporte.png", QSize(), QIcon.Normal, QIcon.Off)
        self.excel_generate_button.setIcon(icon4)
        self.excel_generate_button.setIconSize(QSize(200, 200))
        self.excel_generate_button.setFlat(True)
        self.marcar_salida_button = QPushButton(self.buttonsFrame)
        self.marcar_salida_button.setObjectName(u"marcar_salida_button")
        self.marcar_salida_button.setGeometry(QRect(650, 50, 201, 91))
        self.marcar_salida_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.marcar_salida_button.setStyleSheet(u"QPushButton:hover\n"
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
        icon5 = QIcon()
        icon5.addFile(u"./assets/icons/icon_marcar_exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.marcar_salida_button.setIcon(icon5)
        self.marcar_salida_button.setIconSize(QSize(200, 200))
        self.marcar_salida_button.setFlat(True)
        self.open_new_button_2.raise_()
        self.open_new_button.raise_()
        self.delete_book_button.raise_()
        self.label_7.raise_()
        self.searchButton_2.raise_()
        self.excel_generate_button.raise_()
        self.marcar_salida_button.raise_()
        self.listBooksTable = QTableWidget(self.tab)
        self.listBooksTable.setObjectName(u"listBooksTable")
        self.listBooksTable.setGeometry(QRect(0, 220, 1321, 411))
        self.listBooksTable.setAutoFillBackground(True)
        self.listBooksTable.setLineWidth(5)
        self.listBooksTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listBooksTable.setTextElideMode(Qt.ElideLeft)
        self.listBooksTable.horizontalHeader().setMinimumSectionSize(10)
        self.booksQtyLabel = QLabel(self.tab)
        self.booksQtyLabel.setObjectName(u"booksQtyLabel")
        self.booksQtyLabel.setGeometry(QRect(150, 630, 47, 16))
        self.booksQtyLabel.setFont(font)
        self.parameterLineEditDNI = QLineEdit(self.tab)
        self.parameterLineEditDNI.setObjectName(u"parameterLineEditDNI")
        self.parameterLineEditDNI.setGeometry(QRect(0, 160, 101, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.parameterLineEditDNI.setFont(font2)
        self.searchByPiso = QComboBox(self.tab)
        self.searchByPiso.setObjectName(u"searchByPiso")
        self.searchByPiso.setGeometry(QRect(110, 160, 131, 31))
        self.searchByPiso.setFont(font2)
        self.parameterLineEditFecha = QLineEdit(self.tab)
        self.parameterLineEditFecha.setObjectName(u"parameterLineEditFecha")
        self.parameterLineEditFecha.setGeometry(QRect(250, 160, 111, 31))
        self.parameterLineEditFecha.setFont(font2)
        self.parameterLineEditVisitante = QLineEdit(self.tab)
        self.parameterLineEditVisitante.setObjectName(u"parameterLineEditVisitante")
        self.parameterLineEditVisitante.setGeometry(QRect(370, 160, 341, 31))
        self.parameterLineEditVisitante.setFont(font2)
        self.parameterLineEditMotivo = QLineEdit(self.tab)
        self.parameterLineEditMotivo.setObjectName(u"parameterLineEditMotivo")
        self.parameterLineEditMotivo.setGeometry(QRect(720, 160, 281, 31))
        self.parameterLineEditMotivo.setFont(font2)
        self.label_advertencia_filtros = QLabel(self.tab)
        self.label_advertencia_filtros.setObjectName(u"label_advertencia_filtros")
        self.label_advertencia_filtros.setGeometry(QRect(730, 140, 421, 21))
        self.label_advertencia_filtros.setFont(font)
        self.label_advertencia_sin_resultados = QLabel(self.tab)
        self.label_advertencia_sin_resultados.setObjectName(u"label_advertencia_sin_resultados")
        self.label_advertencia_sin_resultados.setGeometry(QRect(800, 140, 351, 21))
        self.label_advertencia_sin_resultados.setFont(font)
        self.searchByEstado = QComboBox(self.tab)
        self.searchByEstado.setObjectName(u"searchByEstado")
        self.searchByEstado.setGeometry(QRect(1010, 160, 141, 31))
        self.searchByEstado.setFont(font2)
        self.searchButton = QPushButton(self.tab)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(1170, 150, 151, 41))
        self.searchButton.setFont(font1)
        self.searchButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton.setStyleSheet(u"QPushButton\n"
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
        icon6 = QIcon()
        icon6.addFile(u"./assets/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon6)
        self.searchButton.setIconSize(QSize(25, 25))
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1010, 190, 101, 21))
        font3 = QFont()
        font3.setPointSize(11)
        self.label_13.setFont(font3)
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 190, 81, 21))
        self.label_5.setFont(font3)
        self.ast_dni = QLabel(self.tab)
        self.ast_dni.setObjectName(u"ast_dni")
        self.ast_dni.setGeometry(QRect(30, 190, 21, 21))
        self.ast_dni.setFont(font)
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(110, 190, 81, 21))
        self.label_9.setFont(font3)
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(250, 190, 81, 21))
        self.label_10.setFont(font3)
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(370, 190, 191, 21))
        self.label_11.setFont(font3)
        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(720, 190, 191, 21))
        self.label_12.setFont(font3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.searchButton_3 = QPushButton(self.tab_2)
        self.searchButton_3.setObjectName(u"searchButton_3")
        self.searchButton_3.setGeometry(QRect(1170, 150, 151, 41))
        self.searchButton_3.setFont(font1)
        self.searchButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton_3.setStyleSheet(u"QPushButton\n"
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
        self.searchButton_3.setIcon(icon6)
        self.searchButton_3.setIconSize(QSize(25, 25))
        self.parameterLineEditMotivo_2 = QLineEdit(self.tab_2)
        self.parameterLineEditMotivo_2.setObjectName(u"parameterLineEditMotivo_2")
        self.parameterLineEditMotivo_2.setGeometry(QRect(720, 160, 281, 31))
        self.parameterLineEditMotivo_2.setFont(font2)
        self.parameterLineEditDNI_2 = QLineEdit(self.tab_2)
        self.parameterLineEditDNI_2.setObjectName(u"parameterLineEditDNI_2")
        self.parameterLineEditDNI_2.setGeometry(QRect(0, 160, 101, 31))
        self.parameterLineEditDNI_2.setFont(font2)
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 190, 31, 21))
        self.label_8.setFont(font3)
        self.parameterLineEditFecha_2 = QLineEdit(self.tab_2)
        self.parameterLineEditFecha_2.setObjectName(u"parameterLineEditFecha_2")
        self.parameterLineEditFecha_2.setGeometry(QRect(250, 160, 111, 31))
        self.parameterLineEditFecha_2.setFont(font2)
        self.parameterLineEditVisitante_2 = QLineEdit(self.tab_2)
        self.parameterLineEditVisitante_2.setObjectName(u"parameterLineEditVisitante_2")
        self.parameterLineEditVisitante_2.setGeometry(QRect(370, 160, 341, 31))
        self.parameterLineEditVisitante_2.setFont(font2)
        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(720, 190, 191, 21))
        self.label_14.setFont(font3)
        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(1010, 190, 101, 21))
        self.label_15.setFont(font3)
        self.ast_dni_2 = QLabel(self.tab_2)
        self.ast_dni_2.setObjectName(u"ast_dni_2")
        self.ast_dni_2.setGeometry(QRect(30, 190, 21, 21))
        self.ast_dni_2.setFont(font)
        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(250, 190, 81, 21))
        self.label_16.setFont(font3)
        self.searchByPiso_2 = QComboBox(self.tab_2)
        self.searchByPiso_2.setObjectName(u"searchByPiso_2")
        self.searchByPiso_2.setGeometry(QRect(110, 160, 131, 31))
        self.searchByPiso_2.setFont(font2)
        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(370, 190, 191, 21))
        self.label_17.setFont(font3)
        self.searchByEstado_2 = QComboBox(self.tab_2)
        self.searchByEstado_2.setObjectName(u"searchByEstado_2")
        self.searchByEstado_2.setGeometry(QRect(1010, 160, 141, 31))
        self.searchByEstado_2.setFont(font2)
        self.buttonsFrame_2 = QFrame(self.tab_2)
        self.buttonsFrame_2.setObjectName(u"buttonsFrame_2")
        self.buttonsFrame_2.setGeometry(QRect(0, 0, 1331, 151))
        sizePolicy.setHeightForWidth(self.buttonsFrame_2.sizePolicy().hasHeightForWidth())
        self.buttonsFrame_2.setSizePolicy(sizePolicy)
        self.buttonsFrame_2.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame_2.setFrameShadow(QFrame.Raised)
        self.open_new_button_3 = QPushButton(self.buttonsFrame_2)
        self.open_new_button_3.setObjectName(u"open_new_button_3")
        self.open_new_button_3.setGeometry(QRect(20, 50, 201, 91))
        self.open_new_button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_3.setStyleSheet(u"QPushButton:hover\n"
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
        self.open_new_button_3.setIcon(icon)
        self.open_new_button_3.setIconSize(QSize(200, 200))
        self.open_new_button_3.setFlat(True)
        self.open_new_button_4 = QPushButton(self.buttonsFrame_2)
        self.open_new_button_4.setObjectName(u"open_new_button_4")
        self.open_new_button_4.setGeometry(QRect(230, 50, 201, 91))
        self.open_new_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_4.setStyleSheet(u"QPushButton:hover\n"
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
        self.open_new_button_4.setIcon(icon1)
        self.open_new_button_4.setIconSize(QSize(200, 200))
        self.open_new_button_4.setFlat(True)
        self.delete_book_button_2 = QPushButton(self.buttonsFrame_2)
        self.delete_book_button_2.setObjectName(u"delete_book_button_2")
        self.delete_book_button_2.setGeometry(QRect(440, 50, 201, 91))
        self.delete_book_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_book_button_2.setStyleSheet(u"QPushButton:hover\n"
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
        self.delete_book_button_2.setIcon(icon2)
        self.delete_book_button_2.setIconSize(QSize(200, 200))
        self.delete_book_button_2.setFlat(True)
        self.excel_generate_button_2 = QPushButton(self.buttonsFrame_2)
        self.excel_generate_button_2.setObjectName(u"excel_generate_button_2")
        self.excel_generate_button_2.setGeometry(QRect(850, 50, 201, 91))
        self.excel_generate_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.excel_generate_button_2.setStyleSheet(u"QPushButton:hover\n"
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
        self.excel_generate_button_2.setIcon(icon4)
        self.excel_generate_button_2.setIconSize(QSize(200, 200))
        self.excel_generate_button_2.setFlat(True)
        self.marcar_salida_button_2 = QPushButton(self.buttonsFrame_2)
        self.marcar_salida_button_2.setObjectName(u"marcar_salida_button_2")
        self.marcar_salida_button_2.setGeometry(QRect(650, 50, 201, 91))
        self.marcar_salida_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.marcar_salida_button_2.setStyleSheet(u"QPushButton:hover\n"
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
        self.marcar_salida_button_2.setIcon(icon5)
        self.marcar_salida_button_2.setIconSize(QSize(200, 200))
        self.marcar_salida_button_2.setFlat(True)
        self.searchButton_4 = QPushButton(self.buttonsFrame_2)
        self.searchButton_4.setObjectName(u"searchButton_4")
        self.searchButton_4.setGeometry(QRect(1170, 100, 151, 41))
        self.searchButton_4.setFont(font1)
        self.searchButton_4.setStyleSheet(u"QPushButton\n"
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
        self.searchButton_4.setIcon(icon3)
        self.searchButton_4.setIconSize(QSize(25, 25))
        self.label_19 = QLabel(self.tab_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(110, 190, 81, 21))
        self.label_19.setFont(font3)
        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 10, 1321, 41))
        self.label_18.setStyleSheet(u"background-color: green;")
        self.listBooksTable_2 = QTableWidget(self.tab_2)
        self.listBooksTable_2.setObjectName(u"listBooksTable_2")
        self.listBooksTable_2.setGeometry(QRect(0, 220, 1321, 411))
        self.listBooksTable_2.setAutoFillBackground(True)
        self.listBooksTable_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listBooksTable_2.setTextElideMode(Qt.ElideLeft)
        self.listBooksTable_2.horizontalHeader().setMinimumSectionSize(10)
        self.label_advertencia_sin_resultados_2 = QLabel(self.tab_2)
        self.label_advertencia_sin_resultados_2.setObjectName(u"label_advertencia_sin_resultados_2")
        self.label_advertencia_sin_resultados_2.setGeometry(QRect(790, 140, 351, 21))
        self.label_advertencia_sin_resultados_2.setFont(font)
        self.label_20 = QLabel(self.tab_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 630, 141, 16))
        self.label_20.setFont(font)
        self.booksQtyLabel_2 = QLabel(self.tab_2)
        self.booksQtyLabel_2.setObjectName(u"booksQtyLabel_2")
        self.booksQtyLabel_2.setGeometry(QRect(150, 630, 47, 16))
        self.booksQtyLabel_2.setFont(font)
        self.label_advertencia_filtros_2 = QLabel(self.tab_2)
        self.label_advertencia_filtros_2.setObjectName(u"label_advertencia_filtros_2")
        self.label_advertencia_filtros_2.setGeometry(QRect(730, 140, 431, 21))
        self.label_advertencia_filtros_2.setFont(font)
        self.label_advertencia_dni_2 = QLabel(self.tab_2)
        self.label_advertencia_dni_2.setObjectName(u"label_advertencia_dni_2")
        self.label_advertencia_dni_2.setGeometry(QRect(800, 140, 351, 21))
        self.label_advertencia_dni_2.setFont(font)
        self.tabWidget.addTab(self.tab_2, "")
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
        self.label_advertencia_dni_4 = QLabel(self.tab_5)
        self.label_advertencia_dni_4.setObjectName(u"label_advertencia_dni_4")
        self.label_advertencia_dni_4.setGeometry(QRect(800, 140, 351, 21))
        self.label_advertencia_dni_4.setFont(font)
        self.label_29 = QLabel(self.tab_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(0, 630, 141, 16))
        self.label_29.setFont(font)
        self.buttonsFrame_4 = QFrame(self.tab_5)
        self.buttonsFrame_4.setObjectName(u"buttonsFrame_4")
        self.buttonsFrame_4.setGeometry(QRect(0, 0, 1331, 151))
        sizePolicy.setHeightForWidth(self.buttonsFrame_4.sizePolicy().hasHeightForWidth())
        self.buttonsFrame_4.setSizePolicy(sizePolicy)
        self.buttonsFrame_4.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame_4.setFrameShadow(QFrame.Raised)
        self.open_new_button_7 = QPushButton(self.buttonsFrame_4)
        self.open_new_button_7.setObjectName(u"open_new_button_7")
        self.open_new_button_7.setGeometry(QRect(20, 50, 201, 91))
        self.open_new_button_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_7.setStyleSheet(u"QPushButton:hover\n"
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
        self.open_new_button_7.setIcon(icon)
        self.open_new_button_7.setIconSize(QSize(200, 200))
        self.open_new_button_7.setFlat(True)
        self.open_new_button_8 = QPushButton(self.buttonsFrame_4)
        self.open_new_button_8.setObjectName(u"open_new_button_8")
        self.open_new_button_8.setGeometry(QRect(230, 50, 201, 91))
        self.open_new_button_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_8.setStyleSheet(u"QPushButton:hover\n"
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
        self.open_new_button_8.setIcon(icon1)
        self.open_new_button_8.setIconSize(QSize(200, 200))
        self.open_new_button_8.setFlat(True)
        self.delete_book_button_4 = QPushButton(self.buttonsFrame_4)
        self.delete_book_button_4.setObjectName(u"delete_book_button_4")
        self.delete_book_button_4.setGeometry(QRect(440, 50, 201, 91))
        self.delete_book_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_book_button_4.setStyleSheet(u"QPushButton:hover\n"
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
        self.delete_book_button_4.setIcon(icon2)
        self.delete_book_button_4.setIconSize(QSize(200, 200))
        self.delete_book_button_4.setFlat(True)
        self.label_30 = QLabel(self.buttonsFrame_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(0, 10, 1321, 41))
        self.label_30.setStyleSheet(u"background-color: #8a36d2;")
        self.searchButton_7 = QPushButton(self.buttonsFrame_4)
        self.searchButton_7.setObjectName(u"searchButton_7")
        self.searchButton_7.setGeometry(QRect(1170, 100, 151, 41))
        self.searchButton_7.setFont(font1)
        self.searchButton_7.setStyleSheet(u"QPushButton\n"
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
        self.searchButton_7.setIcon(icon3)
        self.searchButton_7.setIconSize(QSize(25, 25))
        self.excel_generate_button_4 = QPushButton(self.buttonsFrame_4)
        self.excel_generate_button_4.setObjectName(u"excel_generate_button_4")
        self.excel_generate_button_4.setGeometry(QRect(850, 50, 201, 91))
        self.excel_generate_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.excel_generate_button_4.setStyleSheet(u"QPushButton:hover\n"
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
        self.excel_generate_button_4.setIcon(icon4)
        self.excel_generate_button_4.setIconSize(QSize(200, 200))
        self.excel_generate_button_4.setFlat(True)
        self.marcar_salida_button_4 = QPushButton(self.buttonsFrame_4)
        self.marcar_salida_button_4.setObjectName(u"marcar_salida_button_4")
        self.marcar_salida_button_4.setGeometry(QRect(650, 50, 201, 91))
        self.marcar_salida_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.marcar_salida_button_4.setStyleSheet(u"QPushButton:hover\n"
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
        self.marcar_salida_button_4.setIcon(icon5)
        self.marcar_salida_button_4.setIconSize(QSize(200, 200))
        self.marcar_salida_button_4.setFlat(True)
        self.listBooksTable_4 = QTableWidget(self.tab_5)
        self.listBooksTable_4.setObjectName(u"listBooksTable_4")
        self.listBooksTable_4.setGeometry(QRect(0, 220, 1321, 411))
        self.listBooksTable_4.setAutoFillBackground(True)
        self.listBooksTable_4.setLineWidth(5)
        self.listBooksTable_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listBooksTable_4.setTextElideMode(Qt.ElideLeft)
        self.listBooksTable_4.horizontalHeader().setMinimumSectionSize(10)
        self.booksQtyLabel_4 = QLabel(self.tab_5)
        self.booksQtyLabel_4.setObjectName(u"booksQtyLabel_4")
        self.booksQtyLabel_4.setGeometry(QRect(150, 630, 47, 16))
        self.booksQtyLabel_4.setFont(font)
        self.parameterLineEditDNI_4 = QLineEdit(self.tab_5)
        self.parameterLineEditDNI_4.setObjectName(u"parameterLineEditDNI_4")
        self.parameterLineEditDNI_4.setGeometry(QRect(0, 160, 101, 31))
        self.parameterLineEditDNI_4.setFont(font2)
        self.searchByPiso_4 = QComboBox(self.tab_5)
        self.searchByPiso_4.setObjectName(u"searchByPiso_4")
        self.searchByPiso_4.setGeometry(QRect(110, 160, 131, 31))
        self.searchByPiso_4.setFont(font2)
        self.parameterLineEditFecha_4 = QLineEdit(self.tab_5)
        self.parameterLineEditFecha_4.setObjectName(u"parameterLineEditFecha_4")
        self.parameterLineEditFecha_4.setGeometry(QRect(250, 160, 111, 31))
        self.parameterLineEditFecha_4.setFont(font2)
        self.parameterLineEditVisitante_4 = QLineEdit(self.tab_5)
        self.parameterLineEditVisitante_4.setObjectName(u"parameterLineEditVisitante_4")
        self.parameterLineEditVisitante_4.setGeometry(QRect(370, 160, 341, 31))
        self.parameterLineEditVisitante_4.setFont(font2)
        self.parameterLineEditMotivo_4 = QLineEdit(self.tab_5)
        self.parameterLineEditMotivo_4.setObjectName(u"parameterLineEditMotivo_4")
        self.parameterLineEditMotivo_4.setGeometry(QRect(720, 160, 281, 31))
        self.parameterLineEditMotivo_4.setFont(font2)
        self.label_advertencia_filtros_4 = QLabel(self.tab_5)
        self.label_advertencia_filtros_4.setObjectName(u"label_advertencia_filtros_4")
        self.label_advertencia_filtros_4.setGeometry(QRect(730, 140, 421, 21))
        self.label_advertencia_filtros_4.setFont(font)
        self.label_advertencia_sin_resultados_4 = QLabel(self.tab_5)
        self.label_advertencia_sin_resultados_4.setObjectName(u"label_advertencia_sin_resultados_4")
        self.label_advertencia_sin_resultados_4.setGeometry(QRect(800, 140, 351, 21))
        self.label_advertencia_sin_resultados_4.setFont(font)
        self.searchByEstado_4 = QComboBox(self.tab_5)
        self.searchByEstado_4.setObjectName(u"searchByEstado_4")
        self.searchByEstado_4.setGeometry(QRect(1010, 160, 141, 31))
        self.searchByEstado_4.setFont(font2)
        self.searchButton_8 = QPushButton(self.tab_5)
        self.searchButton_8.setObjectName(u"searchButton_8")
        self.searchButton_8.setGeometry(QRect(1170, 150, 151, 41))
        self.searchButton_8.setFont(font1)
        self.searchButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton_8.setStyleSheet(u"QPushButton\n"
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
        self.searchButton_8.setIcon(icon6)
        self.searchButton_8.setIconSize(QSize(25, 25))
        self.label_31 = QLabel(self.tab_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(1010, 190, 101, 21))
        self.label_31.setFont(font3)
        self.label_32 = QLabel(self.tab_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(0, 190, 81, 21))
        self.label_32.setFont(font3)
        self.ast_dni_4 = QLabel(self.tab_5)
        self.ast_dni_4.setObjectName(u"ast_dni_4")
        self.ast_dni_4.setGeometry(QRect(30, 190, 21, 21))
        self.ast_dni_4.setFont(font)
        self.label_33 = QLabel(self.tab_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(110, 190, 81, 21))
        self.label_33.setFont(font3)
        self.label_34 = QLabel(self.tab_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(250, 190, 81, 21))
        self.label_34.setFont(font3)
        self.label_35 = QLabel(self.tab_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(370, 190, 191, 21))
        self.label_35.setFont(font3)
        self.label_36 = QLabel(self.tab_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(720, 190, 191, 21))
        self.label_36.setFont(font3)
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
        self.searchButton_9.setIcon(icon6)
        self.searchButton_9.setIconSize(QSize(25, 25))
        self.parameterLineEditMotivo_5 = QLineEdit(self.tab_6)
        self.parameterLineEditMotivo_5.setObjectName(u"parameterLineEditMotivo_5")
        self.parameterLineEditMotivo_5.setGeometry(QRect(700, 160, 301, 31))
        self.parameterLineEditMotivo_5.setFont(font2)
        self.parameterLineEditDNI_5 = QLineEdit(self.tab_6)
        self.parameterLineEditDNI_5.setObjectName(u"parameterLineEditDNI_5")
        self.parameterLineEditDNI_5.setGeometry(QRect(0, 160, 101, 31))
        self.parameterLineEditDNI_5.setFont(font2)
        self.label_37 = QLabel(self.tab_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(0, 190, 31, 21))
        self.label_37.setFont(font3)
        self.parameterLineEditFecha_5 = QLineEdit(self.tab_6)
        self.parameterLineEditFecha_5.setObjectName(u"parameterLineEditFecha_5")
        self.parameterLineEditFecha_5.setGeometry(QRect(200, 160, 111, 31))
        self.parameterLineEditFecha_5.setFont(font2)
        self.parameterLineEditVisitante_5 = QLineEdit(self.tab_6)
        self.parameterLineEditVisitante_5.setObjectName(u"parameterLineEditVisitante_5")
        self.parameterLineEditVisitante_5.setGeometry(QRect(320, 160, 371, 31))
        self.parameterLineEditVisitante_5.setFont(font2)
        self.label_38 = QLabel(self.tab_6)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(700, 190, 191, 21))
        self.label_38.setFont(font3)
        self.label_39 = QLabel(self.tab_6)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(1010, 190, 101, 21))
        self.label_39.setFont(font3)
        self.ast_dni_5 = QLabel(self.tab_6)
        self.ast_dni_5.setObjectName(u"ast_dni_5")
        self.ast_dni_5.setGeometry(QRect(30, 190, 21, 21))
        self.ast_dni_5.setFont(font)
        self.label_40 = QLabel(self.tab_6)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(200, 190, 81, 21))
        self.label_40.setFont(font3)
        self.searchByPiso_5 = QComboBox(self.tab_6)
        self.searchByPiso_5.setObjectName(u"searchByPiso_5")
        self.searchByPiso_5.setGeometry(QRect(110, 160, 81, 31))
        self.searchByPiso_5.setFont(font2)
        self.label_41 = QLabel(self.tab_6)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(320, 190, 191, 21))
        self.label_41.setFont(font3)
        self.searchByEstado_5 = QComboBox(self.tab_6)
        self.searchByEstado_5.setObjectName(u"searchByEstado_5")
        self.searchByEstado_5.setGeometry(QRect(1010, 160, 141, 31))
        self.searchByEstado_5.setFont(font2)
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
        self.open_new_button_9.setIcon(icon)
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
        self.open_new_button_10.setIcon(icon1)
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
        self.delete_book_button_5.setIcon(icon2)
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
        self.excel_generate_button_5.setIcon(icon4)
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
        self.marcar_salida_button_5.setIcon(icon5)
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
        self.searchButton_10.setIcon(icon3)
        self.searchButton_10.setIconSize(QSize(25, 25))
        self.label_42 = QLabel(self.tab_6)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(110, 190, 81, 21))
        self.label_42.setFont(font3)
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
        self.open_new_button_11.setIcon(icon)
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
        self.open_new_button_12.setIcon(icon1)
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
        self.delete_book_button_6.setIcon(icon2)
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
        self.excel_generate_button_6.setIcon(icon4)
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
        self.marcar_salida_button_6.setIcon(icon5)
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
        self.searchButton_11.setIcon(icon3)
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
        self.label_46.setFont(font3)
        self.searchByPiso_6 = QComboBox(self.tab_8)
        self.searchByPiso_6.setObjectName(u"searchByPiso_6")
        self.searchByPiso_6.setGeometry(QRect(110, 160, 81, 31))
        self.searchByPiso_6.setFont(font2)
        self.label_47 = QLabel(self.tab_8)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(200, 190, 81, 21))
        self.label_47.setFont(font3)
        self.searchByEstado_6 = QComboBox(self.tab_8)
        self.searchByEstado_6.setObjectName(u"searchByEstado_6")
        self.searchByEstado_6.setGeometry(QRect(1010, 160, 141, 31))
        self.searchByEstado_6.setFont(font2)
        self.label_48 = QLabel(self.tab_8)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(700, 190, 191, 21))
        self.label_48.setFont(font3)
        self.parameterLineEditDNI_6 = QLineEdit(self.tab_8)
        self.parameterLineEditDNI_6.setObjectName(u"parameterLineEditDNI_6")
        self.parameterLineEditDNI_6.setGeometry(QRect(0, 160, 101, 31))
        self.parameterLineEditDNI_6.setFont(font2)
        self.parameterLineEditFecha_6 = QLineEdit(self.tab_8)
        self.parameterLineEditFecha_6.setObjectName(u"parameterLineEditFecha_6")
        self.parameterLineEditFecha_6.setGeometry(QRect(200, 160, 111, 31))
        self.parameterLineEditFecha_6.setFont(font2)
        self.parameterLineEditMotivo_6 = QLineEdit(self.tab_8)
        self.parameterLineEditMotivo_6.setObjectName(u"parameterLineEditMotivo_6")
        self.parameterLineEditMotivo_6.setGeometry(QRect(700, 160, 301, 31))
        self.parameterLineEditMotivo_6.setFont(font2)
        self.label_49 = QLabel(self.tab_8)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(0, 190, 81, 21))
        self.label_49.setFont(font3)
        self.parameterLineEditVisitante_6 = QLineEdit(self.tab_8)
        self.parameterLineEditVisitante_6.setObjectName(u"parameterLineEditVisitante_6")
        self.parameterLineEditVisitante_6.setGeometry(QRect(320, 160, 371, 31))
        self.parameterLineEditVisitante_6.setFont(font2)
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
        self.searchButton_12.setIcon(icon6)
        self.searchButton_12.setIconSize(QSize(25, 25))
        self.ast_dni_6 = QLabel(self.tab_8)
        self.ast_dni_6.setObjectName(u"ast_dni_6")
        self.ast_dni_6.setGeometry(QRect(30, 190, 21, 21))
        self.ast_dni_6.setFont(font)
        self.label_50 = QLabel(self.tab_8)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(320, 190, 191, 21))
        self.label_50.setFont(font3)
        self.label_51 = QLabel(self.tab_8)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(1010, 190, 101, 21))
        self.label_51.setFont(font3)
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
        self.tabWidget.addTab(self.tab_4, "")
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
        self.open_new_button_5.setIcon(icon)
        self.open_new_button_5.setIconSize(QSize(200, 200))
        self.open_new_button_5.setFlat(True)
        self.open_new_button_6 = QPushButton(self.buttonsFrame_3)
        self.open_new_button_6.setObjectName(u"open_new_button_6")
        self.open_new_button_6.setGeometry(QRect(230, 50, 201, 91))
        self.open_new_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button_6.setStyleSheet(u"QPushButton:hover\n"
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
        self.open_new_button_6.setIcon(icon1)
        self.open_new_button_6.setIconSize(QSize(200, 200))
        self.open_new_button_6.setFlat(True)
        self.delete_book_button_3 = QPushButton(self.buttonsFrame_3)
        self.delete_book_button_3.setObjectName(u"delete_book_button_3")
        self.delete_book_button_3.setGeometry(QRect(440, 50, 201, 91))
        self.delete_book_button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_book_button_3.setStyleSheet(u"QPushButton:hover\n"
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
        self.delete_book_button_3.setIcon(icon2)
        self.delete_book_button_3.setIconSize(QSize(200, 200))
        self.delete_book_button_3.setFlat(True)
        self.excel_generate_button_3 = QPushButton(self.buttonsFrame_3)
        self.excel_generate_button_3.setObjectName(u"excel_generate_button_3")
        self.excel_generate_button_3.setGeometry(QRect(850, 50, 201, 91))
        self.excel_generate_button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.excel_generate_button_3.setStyleSheet(u"QPushButton:hover\n"
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
        self.excel_generate_button_3.setIcon(icon4)
        self.excel_generate_button_3.setIconSize(QSize(200, 200))
        self.excel_generate_button_3.setFlat(True)
        self.marcar_salida_button_3 = QPushButton(self.buttonsFrame_3)
        self.marcar_salida_button_3.setObjectName(u"marcar_salida_button_3")
        self.marcar_salida_button_3.setGeometry(QRect(650, 50, 201, 91))
        self.marcar_salida_button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.marcar_salida_button_3.setStyleSheet(u"QPushButton:hover\n"
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
        self.marcar_salida_button_3.setIcon(icon5)
        self.marcar_salida_button_3.setIconSize(QSize(200, 200))
        self.marcar_salida_button_3.setFlat(True)
        self.searchButton_5 = QPushButton(self.buttonsFrame_3)
        self.searchButton_5.setObjectName(u"searchButton_5")
        self.searchButton_5.setGeometry(QRect(1170, 110, 151, 41))
        self.searchButton_5.setFont(font1)
        self.searchButton_5.setStyleSheet(u"QPushButton\n"
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
        self.searchButton_5.setIcon(icon3)
        self.searchButton_5.setIconSize(QSize(25, 25))
        self.label_21 = QLabel(self.buttonsFrame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 10, 1321, 41))
        self.label_21.setStyleSheet(u"background-color: BLUE;")
        self.label_advertencia_filtros_3 = QLabel(self.tab_3)
        self.label_advertencia_filtros_3.setObjectName(u"label_advertencia_filtros_3")
        self.label_advertencia_filtros_3.setGeometry(QRect(740, 140, 431, 21))
        self.label_advertencia_filtros_3.setFont(font)
        self.label_22 = QLabel(self.tab_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(110, 190, 81, 21))
        self.label_22.setFont(font3)
        self.searchByPiso_3 = QComboBox(self.tab_3)
        self.searchByPiso_3.setObjectName(u"searchByPiso_3")
        self.searchByPiso_3.setGeometry(QRect(110, 160, 131, 31))
        self.searchByPiso_3.setFont(font2)
        self.label_23 = QLabel(self.tab_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(250, 190, 81, 21))
        self.label_23.setFont(font3)
        self.searchByEstado_3 = QComboBox(self.tab_3)
        self.searchByEstado_3.setObjectName(u"searchByEstado_3")
        self.searchByEstado_3.setGeometry(QRect(1010, 160, 141, 31))
        self.searchByEstado_3.setFont(font2)
        self.label_24 = QLabel(self.tab_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(720, 190, 191, 21))
        self.label_24.setFont(font3)
        self.parameterLineEditDNI_3 = QLineEdit(self.tab_3)
        self.parameterLineEditDNI_3.setObjectName(u"parameterLineEditDNI_3")
        self.parameterLineEditDNI_3.setGeometry(QRect(0, 160, 101, 31))
        self.parameterLineEditDNI_3.setFont(font2)
        self.parameterLineEditFecha_3 = QLineEdit(self.tab_3)
        self.parameterLineEditFecha_3.setObjectName(u"parameterLineEditFecha_3")
        self.parameterLineEditFecha_3.setGeometry(QRect(250, 160, 111, 31))
        self.parameterLineEditFecha_3.setFont(font2)
        self.parameterLineEditMotivo_3 = QLineEdit(self.tab_3)
        self.parameterLineEditMotivo_3.setObjectName(u"parameterLineEditMotivo_3")
        self.parameterLineEditMotivo_3.setGeometry(QRect(720, 160, 281, 31))
        self.parameterLineEditMotivo_3.setFont(font2)
        self.label_25 = QLabel(self.tab_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(0, 190, 81, 21))
        self.label_25.setFont(font3)
        self.parameterLineEditVisitante_3 = QLineEdit(self.tab_3)
        self.parameterLineEditVisitante_3.setObjectName(u"parameterLineEditVisitante_3")
        self.parameterLineEditVisitante_3.setGeometry(QRect(370, 160, 341, 31))
        self.parameterLineEditVisitante_3.setFont(font2)
        self.label_advertencia_sin_resultados_3 = QLabel(self.tab_3)
        self.label_advertencia_sin_resultados_3.setObjectName(u"label_advertencia_sin_resultados_3")
        self.label_advertencia_sin_resultados_3.setGeometry(QRect(790, 140, 351, 21))
        self.label_advertencia_sin_resultados_3.setFont(font)
        self.searchButton_6 = QPushButton(self.tab_3)
        self.searchButton_6.setObjectName(u"searchButton_6")
        self.searchButton_6.setGeometry(QRect(1170, 160, 151, 41))
        self.searchButton_6.setFont(font1)
        self.searchButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton_6.setStyleSheet(u"QPushButton\n"
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
        self.searchButton_6.setIcon(icon6)
        self.searchButton_6.setIconSize(QSize(25, 25))
        self.ast_dni_3 = QLabel(self.tab_3)
        self.ast_dni_3.setObjectName(u"ast_dni_3")
        self.ast_dni_3.setGeometry(QRect(30, 190, 21, 21))
        self.ast_dni_3.setFont(font)
        self.label_26 = QLabel(self.tab_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(370, 190, 191, 21))
        self.label_26.setFont(font3)
        self.label_27 = QLabel(self.tab_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(1010, 190, 101, 21))
        self.label_27.setFont(font3)
        self.listBooksTable_3 = QTableWidget(self.tab_3)
        self.listBooksTable_3.setObjectName(u"listBooksTable_3")
        self.listBooksTable_3.setGeometry(QRect(0, 220, 1321, 411))
        self.listBooksTable_3.setToolTipDuration(-1)
        self.listBooksTable_3.setAutoFillBackground(True)
        self.listBooksTable_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listBooksTable_3.setTextElideMode(Qt.ElideLeft)
        self.listBooksTable_3.horizontalHeader().setMinimumSectionSize(10)
        self.label_28 = QLabel(self.tab_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(0, 630, 141, 16))
        self.label_28.setFont(font)
        self.booksQtyLabel_3 = QLabel(self.tab_3)
        self.booksQtyLabel_3.setObjectName(u"booksQtyLabel_3")
        self.booksQtyLabel_3.setGeometry(QRect(150, 630, 47, 16))
        self.booksQtyLabel_3.setFont(font)
        self.label_advertencia_dni_3 = QLabel(self.tab_3)
        self.label_advertencia_dni_3.setObjectName(u"label_advertencia_dni_3")
        self.label_advertencia_dni_3.setGeometry(QRect(810, 140, 351, 21))
        self.label_advertencia_dni_3.setFont(font)
        self.tabWidget.addTab(self.tab_3, "")
        QWidget.setTabOrder(self.parameterLineEditDNI, self.searchByPiso)
        QWidget.setTabOrder(self.searchByPiso, self.parameterLineEditFecha)
        QWidget.setTabOrder(self.parameterLineEditFecha, self.parameterLineEditVisitante)
        QWidget.setTabOrder(self.parameterLineEditVisitante, self.parameterLineEditMotivo)
        QWidget.setTabOrder(self.parameterLineEditMotivo, self.searchByEstado)
        QWidget.setTabOrder(self.searchByEstado, self.searchButton)
        QWidget.setTabOrder(self.searchButton, self.searchButton_2)
        QWidget.setTabOrder(self.searchButton_2, self.listBooksTable)
        QWidget.setTabOrder(self.listBooksTable, self.open_new_button)
        QWidget.setTabOrder(self.open_new_button, self.open_new_button_2)
        QWidget.setTabOrder(self.open_new_button_2, self.delete_book_button)
        QWidget.setTabOrder(self.delete_book_button, self.marcar_salida_button)
        QWidget.setTabOrder(self.marcar_salida_button, self.excel_generate_button)

        self.retranslateUi(ListBookForm)

        self.tabWidget.setCurrentIndex(0)
        self.open_new_button.setDefault(True)
        self.open_new_button_2.setDefault(True)
        self.delete_book_button.setDefault(True)
        self.searchButton_2.setDefault(True)
        self.excel_generate_button.setDefault(True)
        self.marcar_salida_button.setDefault(True)
        self.searchButton.setDefault(True)
        self.searchButton_3.setDefault(True)
        self.open_new_button_3.setDefault(True)
        self.open_new_button_4.setDefault(True)
        self.delete_book_button_2.setDefault(True)
        self.excel_generate_button_2.setDefault(True)
        self.marcar_salida_button_2.setDefault(True)
        self.searchButton_4.setDefault(True)
        self.tabWidget_2.setCurrentIndex(0)
        self.open_new_button_7.setDefault(True)
        self.open_new_button_8.setDefault(True)
        self.delete_book_button_4.setDefault(True)
        self.searchButton_7.setDefault(True)
        self.excel_generate_button_4.setDefault(True)
        self.marcar_salida_button_4.setDefault(True)
        self.searchButton_8.setDefault(True)
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
        self.open_new_button_6.setDefault(True)
        self.delete_book_button_3.setDefault(True)
        self.excel_generate_button_3.setDefault(True)
        self.marcar_salida_button_3.setDefault(True)
        self.searchButton_5.setDefault(True)
        self.searchButton_6.setDefault(True)


        QMetaObject.connectSlotsByName(ListBookForm)
    # setupUi

    def retranslateUi(self, ListBookForm):
        ListBookForm.setWindowTitle(QCoreApplication.translate("ListBookForm", u"Sistema de Registro de Ingresos - Banco de la Naci\u00f3n", None))
        self.label_advertencia_dni.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">El DNI debe contener 8 d\u00edgitos!</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.open_new_button.setText("")
        self.open_new_button_2.setText("")
        self.delete_book_button.setText("")
        self.label_7.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">REGISTRO DE VISITAS</span></p></body></html>", None))
        self.searchButton_2.setText(QCoreApplication.translate("ListBookForm", u" ACTUALIZAR", None))
        self.excel_generate_button.setText("")
        self.marcar_salida_button.setText("")
        self.booksQtyLabel.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.label_advertencia_filtros.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-style:italic; color:#ff0000;\">\u00a1Ingrese datos en al menos uno de los campos para realizar la b\u00fasqueda!</span></p></body></html>", None))
        self.label_advertencia_sin_resultados.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">No existen registros con los par\u00e1metros brindados...</span></p></body></html>", None))
        self.searchButton.setText(QCoreApplication.translate("ListBookForm", u" BUSCAR", None))
        self.label_13.setText(QCoreApplication.translate("ListBookForm", u"ESTADO", None))
        self.label_5.setText(QCoreApplication.translate("ListBookForm", u"DNI", None))
        self.ast_dni.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ff0000;\">*</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("ListBookForm", u"PISO", None))
        self.label_10.setText(QCoreApplication.translate("ListBookForm", u"FECHA", None))
        self.label_11.setText(QCoreApplication.translate("ListBookForm", u"NOMBRE DEL VISITANTE", None))
        self.label_12.setText(QCoreApplication.translate("ListBookForm", u"MOTIVO", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ListBookForm", u"VISITAS", None))
        self.searchButton_3.setText(QCoreApplication.translate("ListBookForm", u" BUSCAR", None))
        self.label_8.setText(QCoreApplication.translate("ListBookForm", u"DNI", None))
        self.label_14.setText(QCoreApplication.translate("ListBookForm", u"MOTIVO", None))
        self.label_15.setText(QCoreApplication.translate("ListBookForm", u"ESTADO", None))
        self.ast_dni_2.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ff0000;\">*</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("ListBookForm", u"FECHA", None))
        self.label_17.setText(QCoreApplication.translate("ListBookForm", u"NOMBRE DEL LOCADOR", None))
        self.open_new_button_3.setText("")
        self.open_new_button_4.setText("")
        self.delete_book_button_2.setText("")
        self.excel_generate_button_2.setText("")
        self.marcar_salida_button_2.setText("")
        self.searchButton_4.setText(QCoreApplication.translate("ListBookForm", u" ACTUALIZAR", None))
        self.label_19.setText(QCoreApplication.translate("ListBookForm", u"PISO", None))
        self.label_18.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">REGISTRO DE LOCADORES</span></p></body></html>", None))
        self.label_advertencia_sin_resultados_2.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">No existen registros con los par\u00e1metros brindados...</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.booksQtyLabel_2.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.label_advertencia_filtros_2.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-style:italic; color:#ff0000;\">\u00a1Ingrese datos en al menos uno de los campos para realizar la b\u00fasqueda!</span></p></body></html>", None))
        self.label_advertencia_dni_2.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">El DNI debe contener 8 d\u00edgitos!</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ListBookForm", u"LOCADORES", None))
        self.label_advertencia_dni_4.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">El DNI debe contener 8 d\u00edgitos!</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.open_new_button_7.setText("")
        self.open_new_button_8.setText("")
        self.delete_book_button_4.setText("")
        self.label_30.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">REGISTRO DE PERSONAL</span></p></body></html>", None))
        self.searchButton_7.setText(QCoreApplication.translate("ListBookForm", u" ACTUALIZAR", None))
        self.excel_generate_button_4.setText("")
        self.marcar_salida_button_4.setText("")
        self.booksQtyLabel_4.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.label_advertencia_filtros_4.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-style:italic; color:#ff0000;\">\u00a1Ingrese datos en al menos uno de los campos para realizar la b\u00fasqueda!</span></p></body></html>", None))
        self.label_advertencia_sin_resultados_4.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">No existen registros con los par\u00e1metros brindados...</span></p></body></html>", None))
        self.searchButton_8.setText(QCoreApplication.translate("ListBookForm", u" BUSCAR", None))
        self.label_31.setText(QCoreApplication.translate("ListBookForm", u"ESTADO", None))
        self.label_32.setText(QCoreApplication.translate("ListBookForm", u"DNI", None))
        self.ast_dni_4.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ff0000;\">*</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("ListBookForm", u"PISO", None))
        self.label_34.setText(QCoreApplication.translate("ListBookForm", u"FECHA", None))
        self.label_35.setText(QCoreApplication.translate("ListBookForm", u"NOMBRE DEL PERSONAL", None))
        self.label_36.setText(QCoreApplication.translate("ListBookForm", u"MOTIVO", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("ListBookForm", u"PERSONAL", None))
        self.open_new_button_5.setText("")
        self.open_new_button_6.setText("")
        self.delete_book_button_3.setText("")
        self.excel_generate_button_3.setText("")
        self.marcar_salida_button_3.setText("")
        self.searchButton_5.setText(QCoreApplication.translate("ListBookForm", u" ACTUALIZAR", None))
        self.label_21.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">REGISTRO DE PERSONAL DE MANTENIMIENTO</span></p></body></html>", None))
        self.label_advertencia_filtros_3.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-style:italic; color:#ff0000;\">\u00a1Ingrese datos en al menos uno de los campos para realizar la b\u00fasqueda!</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("ListBookForm", u"PISO", None))
        self.label_23.setText(QCoreApplication.translate("ListBookForm", u"FECHA", None))
        self.label_24.setText(QCoreApplication.translate("ListBookForm", u"MOTIVO", None))
        self.label_25.setText(QCoreApplication.translate("ListBookForm", u"DNI", None))
        self.label_advertencia_sin_resultados_3.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">No existen registros con los par\u00e1metros brindados...</span></p></body></html>", None))
        self.searchButton_6.setText(QCoreApplication.translate("ListBookForm", u" BUSCAR", None))
        self.ast_dni_3.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ff0000;\">*</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("ListBookForm", u"NOMBRE DEL PERSONAL", None))
        self.label_27.setText(QCoreApplication.translate("ListBookForm", u"ESTADO", None))
        self.label_28.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de registros:</span></p></body></html>", None))
        self.booksQtyLabel_3.setText(QCoreApplication.translate("ListBookForm", u"#", None))
        self.label_advertencia_dni_3.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"right\"><span style=\" font-style:italic; color:#ff0000;\">El DNI debe contener 8 d\u00edgitos!</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("ListBookForm", u"MANTENIMIENTO", None))
    # retranslateUi

