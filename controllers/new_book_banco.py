from PySide2.QtWidgets import QTableWidget,QTableWidgetItem,QHeaderView,QAbstractItemView,QPushButton, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
from controllers.AlignDelegate import *
from views.new_banco import Ui_NewBook
#from db.books import EncontrarDni,UpdateAutoriza
from PySide2 import QtCore
from pys2_msg_boxes import msg_boxes
from datetime import date, datetime
import math
import xlsxwriter
import pandas as pd



class NewBookWindow(QWidget,Ui_NewBook):
    def __init__(self, parent=None,_dataframePadron=None):
        super().__init__(parent)
        self.parent = parent
        self.dataframePadron = _dataframePadron
        print("DATA ENTREGADO ES:")
        print(_dataframePadron["EST_CIVIL"])
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        #self.setMaximumSize(QtCore.QSize(1212, 562))
        #self.populate_comboboxAreaVisitada()
        

        '''
        self.onlyInt = QIntValidator()
        self.dniLineEdit.setValidator(self.onlyInt)

        '''
        print("DATAFRAME PADRON:---BANCO")
        print(self.dataframePadron)
        
        self.btnExcel.clicked.connect(self.generar_padron_excel)
        #self.addPdf.clicked.connect(self.generar_padron_pdf)
        self.cancelButton.clicked.connect(self.close)

        
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
        self.tableMasiva2.cellChanged.connect(self.cell_was_edited)

        self.table_config_masivo2()
        self.generar_padron()

    def table_config_masivo2(self):
        
        #column_headers = ("N°","DNI", "AP_PAT", "AP_MAT","NOMBRES", "GENERO","FECHA_NAC", "DIRECCION","UBIGEO_NAC","UBIGEO_DIR", "PADRE", "MADRE", "EST_CIVIL")
        column_headers = ("N°", "SITUACION DEL TRABAJADOR", "TIPO DE IDENTIFICACIÓN","N° DNI" ,"NOMBRES", "APELLIDO PATERNO", "APELLIDO MATERNO","APELLIDO DE CASADA", "PAIS DE RESIDENCIA", "FECHA DE NACIMIENTO", "ESTADO CIVIL","SEXO", "NACIONALIDAD")
        self.tableMasiva2.setColumnCount(len(column_headers))
        self.tableMasiva2.setHorizontalHeaderLabels(column_headers)
        
        stylesheet = "::section{Background-color:red;border:1px solid black;color: white;}"
        self.tableMasiva2.horizontalHeader().setStyleSheet(stylesheet)

        self.tableMasiva2.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableMasiva2.setStyleSheet("QTableWidget{ gridline-color:black;alternate-background-color: #E2DED0;}")
        self.tableMasiva2.setAlternatingRowColors(True)
        self.tableMasiva2.setEditTriggers(QTableWidget.DoubleClicked)
    
    def cell_was_edited(self, row, column):
        item = self.tableMasiva2.item(row, column)
        if item is not None:
            new_value = item.text()
            print(f'Cell at row {row}, column {column} was edited. New value: {new_value}')
            # Aquí puedes agregar lógica adicional para manejar el nuevo valor si es necesario

    def generar_padron(self):
        
        mapeo_est_civil = {
            'SOLTERO': '01',
            'DIVORCIADO': '03',
            'VIUDO': '04',
            'CASADO': '05',
            'CONVIVIENTE': '06'
        }
        

        dataframeDepurado = self.dataframePadron
        dataframeDepurado["SITUACION DEL TRABAJADOR"]="B"
        dataframeDepurado["TIPO DE IDENTIFICACIÓN"]="51"
        dataframeDepurado["PAIS DE RESIDENCIA"]="504"
        dataframeDepurado["NACIONALIDAD"]="504"
        dataframeDepurado['EST_CIVIL'] = dataframeDepurado['EST_CIVIL'].map(mapeo_est_civil).fillna('')
        

        dataframeDepurado = dataframeDepurado.rename(columns={
            'DNI': 'N° DNI',
            'AP_PAT': 'APELLIDO PATERNO',
            'AP_MAT': 'APELLIDO MATERNO',
            'FECHA_NAC': 'FECHA DE NACIMIENTO',
            'EST_CIVIL': 'ESTADO CIVIL'
        })

        # Crear la nueva columna 'APELLIDO DE CASADA' inicialmente vacía
        dataframeDepurado['APELLIDO DE CASADA'] = ''
        #Función para separar y reasignar los apellidos con condiciones específicas
        def separar_apellido(row):
            if row['ESTADO CIVIL'] == '05' and row['SEXO'] == '2':
                apellido_materno = row['APELLIDO MATERNO']
                if 'DE ' in apellido_materno.upper():
                    partes = apellido_materno.upper().split('DE ')
                    if partes[0]!='':
                        row['APELLIDO MATERNO'] = partes[0].strip()
                        row['APELLIDO DE CASADA'] = 'DE ' + partes[1].strip()
                    

                

            return row

        # Aplicar la función al dataframe
        dataframeDepurado = dataframeDepurado.apply(separar_apellido, axis=1)
        # Aplicar la función de conversión a la columna 'FECHA DE NACIMIENTO'
        dataframeDepurado['FECHA DE NACIMIENTO'] = dataframeDepurado['FECHA DE NACIMIENTO'].apply(self.convert_dates)

        # Convertir la columna a datetime, forzando errores a NaT
        dataframeDepurado['FECHA DE NACIMIENTO'] = pd.to_datetime(dataframeDepurado['FECHA DE NACIMIENTO'], errors='coerce')

        # Convertir a formato '%Y%m%d' para los valores no nulos
        dataframeDepurado['FECHA DE NACIMIENTO'] = dataframeDepurado['FECHA DE NACIMIENTO'].apply(
            lambda x: x.strftime('%Y%m%d') if pd.notnull(x) else ''
        )

        #dataframeDepurado["N°"] = range(1, len(dataframeDepurado) + 1)
        # Ordenar el DataframeDepurado
        dataframeDepurado = dataframeDepurado[['SITUACION DEL TRABAJADOR', 'TIPO DE IDENTIFICACIÓN','N° DNI',
                                               'NOMBRES', 'APELLIDO PATERNO', 'APELLIDO MATERNO','APELLIDO DE CASADA',
                                               'PAIS DE RESIDENCIA', 'FECHA DE NACIMIENTO', 'ESTADO CIVIL','SEXO', 'NACIONALIDAD']]
        
        # Reemplazar los valores de la columna 'SEXO'
        dataframeDepurado['SEXO'] = dataframeDepurado['SEXO'].replace({'2': 'M', '1': 'H'})

        # Mostrar el dataframe resultante
        print(dataframeDepurado)
        DataTuplas = dataframeDepurado.values.tolist()
      
        # Cambios últimos
        self.populate_table_masivo2(DataTuplas)


    def generar_padron_excel(self):
        row_count = self.tableMasiva2.rowCount()
        column_count = self.tableMasiva2.columnCount()
        
        data = []
        for row in range(row_count):
            row_data = []
            for column in range(1,column_count):
                item = self.tableMasiva2.item(row, column)
                row_data.append(item.text() if item is not None else "")
            data.append(row_data)
        
        column_headers = [self.tableMasiva2.horizontalHeaderItem(i).text() for i in range(1,column_count)]
        df = pd.DataFrame(data, columns=column_headers)

        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
        dt_string_final = 'Padron_BANCO' + '_'+dt_string
        nombre_archivo = QFileDialog.getSaveFileName(self, 'Guardar Archivo Excel', f'{dt_string_final}.xlsx', 'Excel Files (*.xlsx)')[0]

        workbook = xlsxwriter.Workbook(nombre_archivo)
        worksheet = workbook.add_worksheet()

        formato_general = workbook.add_format({'font_name': 'Cambria', 'font_size': 10})

        for i, data_row in df.iterrows():
            for j, value in enumerate(data_row):
                value = self.limpiar_dato(value)
                worksheet.write(i, j, value, formato_general)

        workbook.close()
        
        print(f"Archivo Excel guardado como {nombre_archivo}")
        msg_boxes.correct_msgbox("¡Generación Exitosa!","¡Se ha guardado el archivo en la ubicación seleccionada!")

       #    CONTINUA EL CODIGO
    def separar_apellido(self,row):
        estado_civil = row[9]  # Suponiendo que la columna 'ESTADO CIVIL' es la cuarta columna (índice 3)
        sexo = row[10]  # Suponiendo que la columna 'SEXO' es la quinta columna (índice 4)
        apellido_materno = row[5]  # Suponiendo que la columna 'APELLIDO MATERNO' es la tercera columna (índice 2)
        apellido_de_casada_index = 6  # Suponiendo que la columna 'APELLIDO DE CASADA' es la sexta columna (índice 5)

        if estado_civil == '05' and sexo == '2':
            if 'DE ' in apellido_materno.upper():
                partes = apellido_materno.upper().split('DE ')
                if partes[0] != '':
                    row[2] = partes[0].strip()
                    row[apellido_de_casada_index] = 'DE ' + partes[1].strip()
                else:
                    row[apellido_de_casada_index] = ''  # Añadir una columna vacía si no se encuentra la parte antes de 'DE '
            else:
                row[apellido_de_casada_index] = ''  # Añadir una columna vacía si no hay 'DE ' en el apellido materno
        else:
            row[apellido_de_casada_index] = ''  # Añadir una columna vacía si las condiciones no se cumplen

        return row

    def generar_padron_pdf(self):
        
        inputRegion = self.inputRegion.text()
        inputProvincia = self.inputProvincia.text()
        inputDistrito = self.inputDistrito.text()
        inputSector = self.inputSector.text()
        inputCultivo = self.inputCultivo.text()
        inputSuperficie = self.inputSuperficie.text()
        inputMonto = self.inputMonto.text()
        dataframeDepurado = self.dataframePadron
       #    CONTINUA EL CODIGO
    
  
    def clean_inputs(self):
        self.inputRegion.clear()
        self.inputProvincia.clear()
        self.inputDistrito.clear()
        self.inputSector.clear()
        self.inputCultivo.clear()
        self.inputSuperficie.clear()
        self.inputMonto.clear()
       
    def limpiar_dato(self,valor):
        if isinstance(valor, float) and (math.isnan(valor) or math.isinf(valor)):
            return ""
        return valor
    
    def populate_table_masivo2(self,data):
        self.tableMasiva2.setRowCount(len(data))
        print("REFRESH4")
        for index_row, row in enumerate(data):
            #row = self.separar_apellido(row)

            # Incrementamos el índice de fila en 1 para comenzar con el número de orden en 1
            order_number = index_row + 1
            # Establecemos el número de orden en la primera columna
            self.tableMasiva2.setItem(index_row, 0, QTableWidgetItem(str(order_number)))
            
            for index_cell, cell in enumerate(row):
                if cell is None or cell == "NULL" or (isinstance(cell, float) and math.isnan(cell)):
                    cell = ""
                # Llenamos los datos de la fila a partir de la segunda columna
                if index_cell == 4: 
                    print("LA CELDA ES:") 
                    print(cell) 
                    if cell == "1":
                        cell_text = "H"
                    elif cell == "2":
                        cell_text = "M"
                    else:
                        cell_text = str(cell)  # Mantener el valor original si no es 1 ni 2
                    self.tableMasiva2.setItem(index_row, index_cell + 1, QTableWidgetItem(cell_text))
                else:
                    self.tableMasiva2.setItem(index_row, index_cell + 1, QTableWidgetItem(str(cell)))
        print("REFRESH5")
        headerVertical = self.tableMasiva2.verticalHeader()
        headerVertical.resizeSections(QHeaderView.ResizeToContents)
        headerVertical.setStretchLastSection(True)


    def convert_dates(self,date_series):
        formats = ['%d/%m/%Y', '%Y%m%d']
        if pd.isnull(date_series) or date_series == '':
            return ''
        for fmt in formats:
            try:
                return pd.to_datetime(date_series, format=fmt)
            except ValueError:
                pass
        return '' 
