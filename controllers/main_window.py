from PySide2.QtWidgets import QWidget, QTableWidgetItem,QMessageBox
from views.main_windows import *
from controllers.AlignDelegate import *
from PySide2 import QtCore
from db.books import select_all_inmuebles,select_all_books,delete_book,select_all_books_general,select_book_by_all_corretivos1,select_book_by_all_corretivos2,select_book_by_all_general,select_book_by_all,select_all_books_correctivos1,select_all_books_correctivos2
#from pys2_msgboxes import msgboxes
from pys2_msg_boxes import msg_boxes
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
import shutil
import math
import pandas as pd
import os


class ListBookWindow(QWidget,Ui_ListBookForm):
    

    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.dataframePadron = None
        self.dataframeBanco = None
        # Conecta la señal textChanged de inputDNI a la función que manejará el bloqueo de otros campos
        self.inputDNI.textChanged.connect(self.bloquear_campos)

        # Conecta las señales textChanged de los otros campos a la misma función
        self.inputNombres.textChanged.connect(self.bloquear_campos)
        self.inputApellidoPaterno.textChanged.connect(self.bloquear_campos)
        self.inputApellidoMaterno.textChanged.connect(self.bloquear_campos)

        self.btnGenerarPadron.clicked.connect(self.open_generar_padron)
        self.btnGenerarBanco.clicked.connect(self.open_generar_banco)

        self.table_config()
        #Actualizar
        self.btnBuscar.clicked.connect(self.search)#BUSCAR BOTON
        self.btnConsultaMasiva.clicked.connect(self.seleccionar_archivo_xlsx)#BUSCAR BOTON
        self.btnConsultaMasiva_3.clicked.connect(self.seleccionar_archivo_Plantilla_xlsx)#BUSCAR BOTON
        self.btnDescargaExcel.clicked.connect(self.descargar_excel)#BUSCAR BOTON
        self.btnDescargaExcel_2.clicked.connect(self.descargar_excel_masivo1)#BUSCAR BOTON
        self.btnDescargaExcel_3.clicked.connect(self.descargar_excel_masivo2)#BUSCAR BOTON

        self.tableGeneral.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableGeneral.verticalHeader().setVisible(False)
        self.tableGeneral.setColumnWidth(0,19)


        headerVertical3 = self.tableGeneral.verticalHeader()
        headerVertical3.resizeSections(QHeaderView.ResizeToContents)
        headerVertical3.setStretchLastSection(True)

        delegate3= AlignDelegate(self.tableGeneral)

        self.tableGeneral.setItemDelegateForColumn(0,delegate3)
        self.tableGeneral.setItemDelegateForColumn(1,delegate3)
        self.tableGeneral.setItemDelegateForColumn(2,delegate3)
        self.tableGeneral.setItemDelegateForColumn(4,delegate3)
        self.tableGeneral.setItemDelegateForColumn(5,delegate3)
        self.tableGeneral.setItemDelegateForColumn(6,delegate3)
        self.tableGeneral.setItemDelegateForColumn(7,delegate3)
        self.tableGeneral.setItemDelegateForColumn(8,delegate3)
        self.tableGeneral.setItemDelegateForColumn(9,delegate3)
        self.tableGeneral.setItemDelegateForColumn(10,delegate3)
        self.tableGeneral.setItemDelegateForColumn(11,delegate3)
        self.tableGeneral.setItemDelegateForColumn(12,delegate3)
        self.tableGeneral.setItemDelegateForColumn(13,delegate3)
        self.tableGeneral.doubleClicked.connect(lambda: self.FilaSeleccionada())


        self.table_config_masivo1()
        #Actualizar

        self.tableMasiva1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableMasiva1.verticalHeader().setVisible(False)
        self.tableMasiva1.setColumnWidth(0,19)


        headerVertical3 = self.tableMasiva1.verticalHeader()
        headerVertical3.resizeSections(QHeaderView.ResizeToContents)
        headerVertical3.setStretchLastSection(True)

        delegate3= AlignDelegate(self.tableMasiva1)

        self.tableMasiva1.setItemDelegateForColumn(0,delegate3)
        self.tableMasiva1.setItemDelegateForColumn(1,delegate3)
        self.tableMasiva1.setItemDelegateForColumn(2,delegate3)
        self.tableMasiva1.setItemDelegateForColumn(4,delegate3)
        self.tableMasiva1.setItemDelegateForColumn(5,delegate3)
        self.tableMasiva1.setItemDelegateForColumn(6,delegate3)
        self.tableMasiva1.setItemDelegateForColumn(7,delegate3)
        self.tableMasiva1.setItemDelegateForColumn(8,delegate3)
        self.tableMasiva1.setItemDelegateForColumn(9,delegate3)
        self.tableMasiva1.setItemDelegateForColumn(10,delegate3)
        self.tableMasiva1.setItemDelegateForColumn(11,delegate3)
        self.tableMasiva1.setItemDelegateForColumn(12,delegate3)
        self.tableMasiva1.setItemDelegateForColumn(13,delegate3)
        self.tableMasiva1.doubleClicked.connect(lambda: self.FilaSeleccionada())

        self.table_config_masivo2()
        #Actualizar

        self.tableMasiva2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableMasiva2.verticalHeader().setVisible(False)
        self.tableMasiva2.setColumnWidth(0,19)


        headerVertical4 = self.tableMasiva2.verticalHeader()
        headerVertical4.resizeSections(QHeaderView.ResizeToContents)
        headerVertical4.setStretchLastSection(True)

        delegate4= AlignDelegate(self.tableMasiva2)

        self.tableMasiva2.setItemDelegateForColumn(0,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(1,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(2,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(4,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(5,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(6,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(7,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(8,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(9,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(10,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(11,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(12,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(13,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(14,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(15,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(16,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(17,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(18,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(19,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(20,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(21,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(22,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(23,delegate4)
        self.tableMasiva2.setItemDelegateForColumn(24,delegate4)
        self.tableMasiva2.doubleClicked.connect(lambda: self.FilaSeleccionada())


        self.setWindowIcon(QIcon('./pys2_msgboxes/icons/banco_icon.png'))

    

    #################################FUNCIONES#######################################
    


    
    def refresh_table_from_child_window(self):
        print("REFRESH FROM CHILD...")
        print("REFRESH1")
        data = select_all_books()
        data1 = select_all_books_correctivos1()
        data2 = select_all_books_correctivos2()
        print("REFRESH2")
        self.populate_table(data)
        self.populate_table_correctivos1(data1)
        self.populate_table_correctivos2(data2)

    

    def populate_table_general(self,data):
        self.tableGeneral.setRowCount(len(data))
        print("REFRESH4")
        for index_row, row in enumerate(data):
            # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
            order_number = index_row + 1
            
            # Establecemos el número de orden en la primera columna
            self.tableGeneral.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
            
            for index_cell, cell in enumerate(row):
                if cell is None or cell == "NULL" or (isinstance(cell, float) and math.isnan(cell)):
                    cell = ""
                # Llenamos los datos de la fila a partir de la segunda columna
                if index_cell == len(row) - 1:  # Verificar si estamos en la última columna
                    if cell == "1":
                        cell_text = "MASCULINO"
                    elif cell == "2":
                        cell_text = "FEMENINO"
                    else:
                        cell_text = str(cell)  # Mantener el valor original si no es 1 ni 2
                    self.tableGeneral.setItem(index_row, index_cell + 1, QTableWidgetItem(cell_text))
                else:
                    self.tableGeneral.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))


            

        print("REFRESH5")
        headerVertical = self.tableGeneral.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)

        self.records_qty()

    def populate_table_masivo1(self,data):
        self.tableMasiva1.setRowCount(len(data))
        print("REFRESH4")
        for index_row, row in enumerate(data):
            # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
            order_number = index_row + 1
            
            # Establecemos el número de orden en la primera columna
            self.tableMasiva1.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
            
            for index_cell, cell in enumerate(row):
                if cell is None or cell == "NULL" or (isinstance(cell, float) and math.isnan(cell)):
                    cell = ""                
                # Llenamos los datos de la fila a partir de la segunda columna
                if index_cell == len(row) - 1:  # Verificar si estamos en la última columna
                    if cell == "1":
                        cell_text = "MASCULINO"
                    elif cell == "2":
                        cell_text = "FEMENINO"
                    else:
                        cell_text = str(cell)  # Mantener el valor original si no es 1 ni 2
                    self.tableMasiva1.setItem(index_row, index_cell + 1, QTableWidgetItem(cell_text))
                else:
                    self.tableMasiva1.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
        print("REFRESH5")
        headerVertical = self.tableMasiva1.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)

        self.records_qty_masivo1()
    
    def populate_table_masivo2(self,data):
        self.tableMasiva2.setRowCount(len(data))
        print("REFRESH4")
        for index_row, row in enumerate(data):

            # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
            order_number = index_row + 1
            
            # Establecemos el número de orden en la primera columna
            self.tableMasiva2.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
            
            for index_cell, cell in enumerate(row):
                if cell is None or cell == "NULL" or (isinstance(cell, float) and math.isnan(cell)):
                    cell = ""
                # Llenamos los datos de la fila a partir de la segunda columna
                if index_cell == len(row) - 13:  # Verificar si estamos en la última columna
                    if cell == "1":
                        cell_text = "MASCULINO"
                    elif cell == "2":
                        cell_text = "FEMENINO"
                    else:
                        cell_text = str(cell)  # Mantener el valor original si no es 1 ni 2
                    self.tableMasiva2.setItem(index_row, index_cell + 1, QTableWidgetItem(cell_text))
                else:
                    self.tableMasiva2.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
        print("REFRESH5")
        headerVertical = self.tableMasiva2.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)

        self.records_qty_masivo2()


    def table_config(self):
        
        column_headers = ("N°","DNI", "NOMBRES", "AP_PAT", "AP_MAT", "FECHA_NAC", "DIRECCION", "EST_CIVIL", "MADRE", "PADRE","SEXO")
        self.tableGeneral.setColumnCount(len(column_headers))
        self.tableGeneral.setHorizontalHeaderLabels(column_headers)
        
        stylesheet = "::section{Background-color:red;border:1px solid black;color: white;}"
        self.tableGeneral.horizontalHeader().setStyleSheet(stylesheet)

        self.tableGeneral.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableGeneral.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableGeneral.setAlternatingRowColors(True)
        #self.tablePreventivos.color
    
    def table_config_masivo1(self):
        
        column_headers = ("N°","DNI", "NOMBRES", "AP_PAT", "AP_MAT", "FECHA_NAC", "DIRECCION", "EST_CIVIL", "MADRE", "PADRE","SEXO")
        self.tableMasiva1.setColumnCount(len(column_headers))
        self.tableMasiva1.setHorizontalHeaderLabels(column_headers)
        
        stylesheet = "::section{Background-color:red;border:1px solid black;color: white;}"
        self.tableMasiva1.horizontalHeader().setStyleSheet(stylesheet)

        self.tableMasiva1.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableMasiva1.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableMasiva1.setAlternatingRowColors(True)

    def table_config_masivo2(self):
        
        #column_headers = ("N°","DNI", "AP_PAT", "AP_MAT","NOMBRES", "GENERO","FECHA_NAC", "DIRECCION","UBIGEO_NAC","UBIGEO_DIR", "PADRE", "MADRE", "EST_CIVIL")
        column_headers = ("N°","SECUENCIA","USUARIO","SECTOR","FECHA REGISTRO","DEPARTAMENTO",
                          "ANVERSO_DNI","REVERSO_DNI","DNI","SUPERFICIE","Monto_Indemnizable","AP_PAT", "AP_MAT","NOMBRES",
                          "SEXO","FECHA_NAC", "DIRECCION","UBIGEO_DIR","DEPARTAMENTO_D","PROVINCIA_D","DISTRITO_D",
                          "PADRE","MADRE","UBIGEO_NAC","DEPARTAMENTO_N","PROVINCIA_N","DISTRITO_N")
        self.tableMasiva2.setColumnCount(len(column_headers))
        self.tableMasiva2.setHorizontalHeaderLabels(column_headers)
        
        stylesheet = "::section{Background-color:red;border:1px solid black;color: white;}"
        self.tableMasiva2.horizontalHeader().setStyleSheet(stylesheet)

        self.tableMasiva2.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableMasiva2.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableMasiva2.setAlternatingRowColors(True)

    def search(self):
        
        inputDNI = self.inputDNI.text()
        inputDNI=inputDNI.strip()

        inputNombres = self.inputNombres.text()
        inputNombres=inputNombres.strip()

        inputApellidoPaterno = self.inputApellidoPaterno.text()
        inputApellidoPaterno=inputApellidoPaterno.strip()

        inputApellidoMaterno = self.inputApellidoMaterno.text()
        inputApellidoMaterno=inputApellidoMaterno.strip()
        print("----------------------------------")
        print("inputDNI: "+inputDNI)
        print("inputNombres: "+inputNombres)
        print("inputApellidoPaterno: "+inputApellidoPaterno)
        print("inputApellidoMaterno: "+inputApellidoMaterno)
        if(inputDNI==""):
            data = self.ConsultaNombresApellidos(inputNombres.upper(),inputApellidoPaterno.upper(),inputApellidoMaterno.upper())
            print("CONSULTA X NOMBRE")
            print(data)
        elif inputDNI!="":
            print ("CONSULTA X DNI")
            data = self.ConsultaDNI(inputDNI)
            print(data)
        self.populate_table_general(data)


    def records_qty(self):
        print("CANTIDAD1")
        qty_rows3 = str(self.tableGeneral.rowCount())
        print("CANTIDAD2")
        self.labelNumeroRegistros.setText(qty_rows3)

    def records_qty_masivo1(self):
        print("CANTIDAD1")
        qty_rows3 = str(self.tableMasiva1.rowCount())
        print("CANTIDAD2")
        self.labelNumeroRegistroMasiva1.setText(qty_rows3)
        #self.labelNumeroRegistros.setText(len(set(index.row() for index in QTableWidget.selectedIndexes())))

    def records_qty_masivo2(self):
        print("CANTIDAD1")
        qty_rows3 = str(self.tableMasiva2.rowCount())
        print("CANTIDAD2")
        self.booksQtyLabel_4.setText(qty_rows3)
        #self.labelNumeroRegistros.setText(len(set(index.row() for index in QTableWidget.selectedIndexes())))


    def limpiarCamposRefresh(self):
        self.parameterLineEditDNI.clear()
        self.searchByPiso.setCurrentIndex(0)
        self.parameterLineEditVisitante.clear()
        self.parameterLineEditFecha.clear()
        self.parameterLineEditMotivo.clear()
        self.searchByEstado.setCurrentIndex(0)
        



   
    def to_upperVisitante(self, txt):
        self.parameterLineEditVisitante.setText(txt.upper())
    

    def to_upperMotivo(self, txt):
        self.parameterLineEditMotivo.setText(txt.upper())
    
    def FilaSeleccionada(self):
        print("ENTRO A DOUBLE CLICK!")
        from controllers.new_window_preventivo_edit import NewBookWindow
        selected_row = self.tablePreventivos.selectedItems()

        if selected_row:
            book_id = int(selected_row[1].text())
            window = NewBookWindow(self, book_id)
            window.show()
        
        self.tablePreventivos.clearSelection()

    
    def open_confirm_excel(self):
        from controllers.confirm_excel import ConfirmExcel
        window= ConfirmExcel(self)
        window.show()
    def open_confirm_excel_preventivo(self):
        from controllers.confirm_excel_preventivo import ConfirmExcel
        window= ConfirmExcel(self)
        window.show()
    def open_confirm_excel_correctivo1(self):
        from controllers.confirm_excel_correctivo1 import ConfirmExcel
        window= ConfirmExcel(self)
        window.show()
    def open_confirm_excel_correctivo2(self):
        from controllers.confirm_excel_correctivo2 import ConfirmExcel
        window= ConfirmExcel(self)
        window.show()

    def to_upperInmueble(self, txt):
        pos2=self.inputInmuebleGeneral.cursorPosition()
        self.inputInmuebleGeneral.setText(txt.upper())
        self.inputInmuebleGeneral.setCursorPosition(pos2)

    def to_upperInmueble2(self, txt):
        pos2=self.inputInmueble.cursorPosition()
        self.inputInmueble.setText(txt.upper())
        self.inputInmueble.setCursorPosition(pos2)

    def to_upperInmueble3(self, txt):
        pos2=self.inputInmuebleCorrectivo1.cursorPosition()
        self.inputInmuebleCorrectivo1.setText(txt.upper())
        self.inputInmuebleCorrectivo1.setCursorPosition(pos2)

    def to_upperInmueble4(self, txt):
        pos2=self.inputInmuebleCorrectivo2.cursorPosition()
        self.inputInmuebleCorrectivo2.setText(txt.upper())
        self.inputInmuebleCorrectivo2.setCursorPosition(pos2)

    def ConsultaDNI(self,dni):
        # Filtra el DataFrame para obtener la fila con el DNI buscado
        resultado = self.df.filter(self.df["DNI"] == dni)
        # Selecciona solo las columnas requeridas
        resultado_seleccionado = resultado.select("DNI", "NOMBRES", "AP_PAT", "AP_MAT", "FECHA_NAC", "DIRECCION", "EST_CIVIL", "MADRE", "PADRE","SEXO")
        
        # Convierte el DataFrame a una lista de tuplas
        resultado_tuplas = [tuple(row) for row in resultado_seleccionado.collect()]
        
        return resultado_tuplas

    def ConsultaNombresApellidos(self, Nom, Ap_pat, Ap_mat):
        # Filtra el DataFrame para obtener la fila con el DNI buscado

        #print("DATAFRAME RESULTADOS"+str(self.df.count()))
        if Nom != "" and Ap_pat != "" and Ap_mat != "":
            resultado = self.df.filter((self.df["NOMBRES"] == Nom) & (self.df["AP_PAT"] == Ap_pat) & (self.df["AP_MAT"] == Ap_mat))
            
        elif Nom == "" and Ap_pat != "" and Ap_mat != "":
            resultado = self.df.filter((self.df["AP_PAT"] == Ap_pat) & (self.df["AP_MAT"] == Ap_mat))
            resultado.show()
        # Selecciona solo las columnas requeridas
        resultado_seleccionado = resultado.select("DNI", "NOMBRES", "AP_PAT", "AP_MAT", "FECHA_NAC", "DIRECCION", "EST_CIVIL", "MADRE", "PADRE","SEXO")
        
        # Convierte el DataFrame a una lista de tuplas
        resultado_tuplas = [tuple(row) for row in resultado_seleccionado.collect()]

        return resultado_tuplas
    
    #Funcion carga masiva dde DNI
    
    def CargaMasivaDNI(self,lista_dni):
        
        # Filtrar el DataFrame por los números de DNI especificados
        resultado = self.df.filter(self.df['DNI'].isin(lista_dni))
        # Selecciona solo las columnas requeridas
        resultado_seleccionado = resultado.select("DNI", "NOMBRES", "AP_PAT", "AP_MAT", "FECHA_NAC", "DIRECCION", "EST_CIVIL", "MADRE", "PADRE","SEXO")
        # Convierte el DataFrame a una lista de tuplas
        resultado_tuplas = [tuple(row) for row in resultado_seleccionado.collect()]
        
        return resultado_tuplas
    

    def CargaMasivaPlantillaDNI(self,lista_dni):
        
        # Filtrar el DataFrame por los números de DNI especificados
        resultado = self.df.filter(self.df['DNI'].isin(lista_dni))
        # Selecciona solo las columnas requeridas
        resultado_seleccionado = resultado.select("DNI", "AP_PAT", "AP_MAT","NOMBRES","SEXO","FECHA_NAC", "DIRECCION","UBIGEO_DIR","UBIGEO_NAC","EST_CIVIL","PADRE", "MADRE")
        return resultado_seleccionado
    
    

    def bloquear_campos_dni(self):
        # Bloquea los otros campos mientras el usuario está escribiendo en inputDNI
        if self.inputDNI.text():
            self.inputNombres.setText("")
            self.inputApellidoPaterno.setText("")
            self.inputApellidoMaterno.setText("")
            self.inputNombres.setEnabled(False)
            self.inputApellidoPaterno.setEnabled(False)
            self.inputApellidoMaterno.setEnabled(False)
        else:
            self.inputNombres.setEnabled(True)
            self.inputApellidoPaterno.setEnabled(True)
            self.inputApellidoMaterno.setEnabled(True)

    def bloquear_campos(self):
        # Verifica qué campo de entrada está activo
        sender = self.sender()

        # Si el campo activo es inputDNI, bloquea los otros campos
        if sender == self.inputDNI:
            self.inputNombres.setEnabled(not sender.text())
            self.inputApellidoPaterno.setEnabled(not sender.text())
            self.inputApellidoMaterno.setEnabled(not sender.text())

        # Si el campo activo es uno de los otros campos, bloquea inputDNI
        else:
            self.inputDNI.setEnabled(not sender.text())

    def seleccionar_archivo_xlsx(self):
        opciones = QFileDialog.Options()
        # No especificar DontUseNativeDialog
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo XLSX", "", "Archivos XLSX (*.xlsx);;Todos los archivos (*)", options=opciones)
        if archivo:
            nombre_destino = "consulta.xlsx"
            ruta_destino = os.path.join(os.path.dirname(__file__), nombre_destino)
            
            try:
                # Copiar el archivo seleccionado a la carpeta del proyecto como "consulta.xlsx"
                shutil.copy(archivo, ruta_destino)
                print(f"Archivo 'consulta.xlsx' copiado exitosamente a la carpeta del proyecto.")
            except Exception as e:
                print(f"Error al copiar el archivo: {e}")
        #Prueba commit
        #ruta_destino = "controllers/consulta.xlsx"
        dfDNI = pd.read_excel(ruta_destino, dtype={'DNI': str})
        lista_DNI = dfDNI['DNI'].tolist()
        
        data = self.CargaMasivaDNI(lista_DNI)
        
        #CAMBIOS ULTIMOS
        self.populate_table_masivo1(data)
        
        # Verificar si el archivo existe antes de intentar eliminarlo
        if os.path.exists(ruta_destino):
            os.remove(ruta_destino)
            print(f"El archivo {ruta_destino} ha sido eliminado exitosamente.")
        else:
            print(f"El archivo {ruta_destino} no existe.")


    def seleccionar_archivo_Plantilla_xlsx(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo XLSX", "", "Archivos XLSX (*.xlsx);;Todos los archivos (*)", options=opciones)
        if archivo:
            nombre_destino = "consultaPlantilla.xlsx"
            ruta_destino = os.path.join(os.path.dirname(__file__), nombre_destino)
            
            try:
                shutil.copy(archivo, ruta_destino)
                print(f"Archivo 'consultaPlantilla.xlsx' copiado exitosamente a la carpeta del proyecto.")
            except Exception as e:
                print(f"Error al copiar el archivo: {e}")
        
        dfDNI = pd.read_excel(ruta_destino, dtype={'DNI': str})
        print(dfDNI)
        lista_DNI = dfDNI['DNI'].tolist()
        
        DataFrameSpark = self.CargaMasivaPlantillaDNI(lista_DNI)
        Pandas_DataFrameSpark = DataFrameSpark.toPandas()
        
        lista_DNI_Spark = Pandas_DataFrameSpark["DNI"].tolist()
        
        #Crear el Dataframe completo a la lista de DNI's  encontrados
        Nuevo_dfDNI = dfDNI[dfDNI["DNI"].isin(lista_DNI_Spark)].copy()  # Asegurarse de crear una copia

        # Evitar SettingWithCopyWarning usando .loc
        Nuevo_dfDNI.loc[:, 'DNI'] = Nuevo_dfDNI['DNI'].astype(str)
        Pandas_DataFrameSpark.loc[:, 'DNI'] = Pandas_DataFrameSpark['DNI'].astype(str)

        # Unir los DataFrames por la columna 'DNI', manteniendo el orden de Nuevo_dfDNI
        merged_df = pd.merge(Nuevo_dfDNI, Pandas_DataFrameSpark, on='DNI', how='left')
        

        # Seleccionar todas las columnas del segundo DataFrame excepto 'DNI' después de la fusión si es necesario
        merged_df = merged_df.drop(columns=['DNI_y']) if 'DNI_y' in merged_df.columns else merged_df

        # Separar los valores de la columna "UBIGEO_DIR" en nuevas columnas
        merged_df[['DEPARTAMENTO_D', 'PROVINCIA_D', 'DISTRITO_D']] = merged_df['UBIGEO_DIR'].str.split('-', expand=True)
        merged_df["UBIGEO_DIR"]=" "

        #Cargar Ubigeos
        dfUbigeos=pd.read_excel("./geodir-ubigeo-reniec.xlsx",dtype={"Ubigeo":str})
        dfUbigeos=dfUbigeos.drop(["Poblacion","Superficie","Y","X"],axis=1)
        dfUbigeos_nac = dfUbigeos.rename(columns={
            "Ubigeo": "UBIGEO_NAC",
            "Distrito": "DISTRITO_N",
            "Provincia": "PROVINCIA_N",
            "Departamento": "DEPARTAMENTO_N"
        })

        
        merged_df1 = pd.merge(merged_df,dfUbigeos_nac, on='UBIGEO_NAC', how='left')
        merged_df2 = merged_df1[["Secuencia","Usuario","Sector","Fecha_Registro","Departamento",
                          "Anverso_DNI","Reverso_DNI","DNI","Superficie","Monto_Indemnizable","AP_PAT", "AP_MAT","NOMBRES",
                          "SEXO","FECHA_NAC","EST_CIVIL","DIRECCION","UBIGEO_DIR","DEPARTAMENTO_D","PROVINCIA_D","DISTRITO_D",
                          "PADRE","MADRE","UBIGEO_NAC","DEPARTAMENTO_N","PROVINCIA_N","DISTRITO_N"]]

        #Realizar el codigo para completar la columna "UBIGEO_DIR" que está vacia
        #Renombrar las columnas de dfUbigeos_nac
        dfUbigeos_nac_renamed = dfUbigeos_nac.rename(columns={
                "DEPARTAMENTO_N": "DEPARTAMENTO_DIR",
                "PROVINCIA_N": "PROVINCIA_DIR",
                "DISTRITO_N": "DISTRITO_DIR",
                "UBIGEO_NAC": "UBIGEO_DIR_TEMP"
            })
        
        #Realizar el merge condicional
        merged_df2 = merged_df2.merge(dfUbigeos_nac_renamed[['DEPARTAMENTO_DIR', 'PROVINCIA_DIR', 'DISTRITO_DIR', 'UBIGEO_DIR_TEMP']],
                              left_on=['DEPARTAMENTO_D', 'PROVINCIA_D', 'DISTRITO_D'],
                              right_on=['DEPARTAMENTO_DIR', 'PROVINCIA_DIR', 'DISTRITO_DIR'],
                              how='left')
        
        #Completar la columna UBIGEO_DIR
        merged_df2['UBIGEO_DIR'] = merged_df2['UBIGEO_DIR_TEMP']
        #Limpiar el DataFrame
        merged_df2.drop(columns=['DEPARTAMENTO_DIR', 'PROVINCIA_DIR', 'DISTRITO_DIR', 'UBIGEO_DIR_TEMP'], inplace=True)

        #########################################################################################
        lista_DNI_NoEncontrados=[]
        #Crear el Dataframe completo a la lista de DNI's no encontrados
        for i in lista_DNI:
            if not i in lista_DNI_Spark:
                lista_DNI_NoEncontrados.append(i)
        print("**********************************************************")
        print("DNI NO ENCONTRADOS :",lista_DNI_NoEncontrados)

        if len(lista_DNI_NoEncontrados)!=0:
            Nuevo_dfDNI_NoEncontrados=dfDNI[dfDNI["DNI"].isin(lista_DNI_NoEncontrados)].copy()
            # Lista de nombres de las nuevas columnas
            columnas_nuevas = ['AP_PAT', 'AP_MAT', 'NOMBRES', 'SEXO', 'FECHA_NAC', 'DIRECCION','UBIGEO_DIR',
                            'DEPARTAMENTO_D', 'PROVINCIA_D', 'DISTRITO_D', 'PADRE','MADRE', 'UBIGEO_NAC',
                            'DEPARTAMENTO_N', 'PROVINCIA_N', 'DISTRITO_N']

            # Añadir las columnas nuevas con campos vacios " "
            for columna in columnas_nuevas:
                Nuevo_dfDNI_NoEncontrados[columna] =' '
            
            merged_df2=pd.concat([merged_df2, Nuevo_dfDNI_NoEncontrados], ignore_index=True)

        #Creando los dataframe para las plantillas
        self.dataframePadron= merged_df2[["DNI","AP_PAT","AP_MAT","NOMBRES","SEXO","FECHA_NAC","UBIGEO_DIR",
                                          "DIRECCION","DISTRITO_D","PROVINCIA_D","Superficie","Monto_Indemnizable"]]

        self.dataframeBanco= merged_df2[["DNI","NOMBRES","AP_PAT","AP_MAT","FECHA_NAC",
                                          "EST_CIVIL","SEXO"]]

        merged_df2.drop(columns=['EST_CIVIL'], inplace=True)

        DataTuplas = merged_df2.values.tolist()
        print("**********************************************************************************")
        print(merged_df2)
       
        # Cambios últimos
        self.populate_table_masivo2(DataTuplas)
        
        # Verificar si el archivo existe antes de intentar eliminarlo
        if os.path.exists(ruta_destino):
            os.remove(ruta_destino)
            print(f"El archivo {ruta_destino} ha sido eliminado exitosamente.")
        else:
            print(f"El archivo {ruta_destino} no existe.")

        #EXCEL!
    def descargar_excel(self):
        opciones = QFileDialog.Options()
        nombre_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo Excel", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)", options=opciones)
        if nombre_archivo:
            # Convertir los datos de QTableWidget a un DataFrame de Pandas
            df = pd.DataFrame(columns=[self.tableGeneral.horizontalHeaderItem(col).text() for col in range(self.tableGeneral.columnCount())])

            for row in range(self.tableGeneral.rowCount()):
                data = []
                for col in range(self.tableGeneral.columnCount()):
                    item = self.tableGeneral.item(row, col)
                    if item is not None:
                        data.append(item.text())
                    else:
                        data.append("")  # Manejar celdas vacías
                df = pd.concat([df, pd.DataFrame([data], columns=df.columns)], ignore_index=True)

            # Guardar el DataFrame como un archivo Excel en la ruta especificada
            if not nombre_archivo.endswith('.xlsx'):
                nombre_archivo += '.xlsx'
            df.to_excel(nombre_archivo, index=False)

            print(f"Archivo '{nombre_archivo}' descargado exitosamente.")
            msg_boxes.correct_msgbox("¡Descarga Exitosa!","¡Se ha guardado el archivo en la carpeta indicada!")

    def descargar_excel_masivo1(self):
        opciones = QFileDialog.Options()
        nombre_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo Excel", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)", options=opciones)
        if nombre_archivo:
            # Convertir los datos de QTableWidget a un DataFrame de Pandas
            df = pd.DataFrame(columns=[self.tableMasiva1.horizontalHeaderItem(col).text() for col in range(self.tableMasiva1.columnCount())])

            for row in range(self.tableMasiva1.rowCount()):
                data = []
                for col in range(self.tableMasiva1.columnCount()):
                    item = self.tableMasiva1.item(row, col)
                    if item is not None:
                        data.append(item.text())
                    else:
                        data.append("")  # Manejar celdas vacías
                df = pd.concat([df, pd.DataFrame([data], columns=df.columns)], ignore_index=True)

            # Guardar el DataFrame como un archivo Excel en la ruta especificada
            if not nombre_archivo.endswith('.xlsx'):
                nombre_archivo += '.xlsx'
            df.to_excel(nombre_archivo, index=False)

            print(f"Archivo '{nombre_archivo}' descargado exitosamente.")
            msg_boxes.correct_msgbox("¡Descarga Exitosa!","¡Se ha guardado el archivo en la carpeta indicada!")

    def descargar_excel_masivo2(self):
        opciones = QFileDialog.Options()
        nombre_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo Excel", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)", options=opciones)
        if nombre_archivo:
            # Convertir los datos de QTableWidget a un DataFrame de Pandas
            df = pd.DataFrame(columns=[self.tableMasiva2.horizontalHeaderItem(col).text() for col in range(self.tableMasiva2.columnCount())])

            for row in range(self.tableMasiva2.rowCount()):
                data = []
                for col in range(self.tableMasiva2.columnCount()):
                    item = self.tableMasiva2.item(row, col)
                    if item is not None:
                        data.append(item.text())
                    else:
                        data.append("")  # Manejar celdas vacías
                df = pd.concat([df, pd.DataFrame([data], columns=df.columns)], ignore_index=True)

            # Guardar el DataFrame como un archivo Excel en la ruta especificada
            if not nombre_archivo.endswith('.xlsx'):
                nombre_archivo += '.xlsx'
            df.to_excel(nombre_archivo, index=False)

            print(f"Archivo '{nombre_archivo}' descargado exitosamente.")
            msg_boxes.correct_msgbox("¡Descarga Exitosa!","¡Se ha guardado el archivo en la carpeta indicada!")


    def open_generar_padron(self,dataframePadron):
        from controllers.new_book_padron import NewBookWindow
        dataframePadron= self.dataframePadron
        window= NewBookWindow(self,dataframePadron)
        window.show()
    #Nuevos cambios
    def open_generar_banco(self,dataframeBanco):
        from controllers.new_book_banco import NewBookWindow
        dataframeBanco= self.dataframeBanco
        window= NewBookWindow(self,dataframeBanco)
        window.show()


    # Inicializa una sesión de Spark
    spark = SparkSession.builder \
        .appName("Lectura de archivo") \
        .getOrCreate()

    # Define el esquema de tu DataFrame
    schema = StructType() \
        .add("DNI", StringType(), True) \
        .add("AP_PAT", StringType(), True) \
        .add("AP_MAT", StringType(), True) \
        .add("NOMBRES", StringType(), True) \
        .add("FECHA_NAC", StringType(), True) \
        .add("FCH_INSCRIPCION", StringType(), True) \
        .add("FCH_EMISION", StringType(), True) \
        .add("FCH_CADUCIDAD", StringType(), True) \
        .add("UBIGEO_NAC", StringType(), True) \
        .add("UBIGEO_DIR", StringType(), True) \
        .add("DIRECCION", StringType(), True) \
        .add("SEXO", StringType(), True) \
        .add("EST_CIVIL", StringType(), True) \
        .add("DIG_RUC", StringType(), True) \
        .add("MADRE", StringType(), True) \
        .add("PADRE", StringType(), True)

    # Lee el archivo con separador '|'
    df = spark.read \
        .option("delimiter", "|") \
        .schema(schema) \
        .csv("./reniec.txt")\
        .repartition("DNI")
    

    
#Nuevos cambios
#HECHOS!
            
