from PySide2.QtWidgets import QPushButton, QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2.QtGui import *
from views.new_padron import NewBookForm
#from db.books import EncontrarDni,UpdateAutoriza
from PySide2 import QtCore
from pys2_msgboxes import msg_boxes
from datetime import date, datetime



class NewBookWindow(QWidget,NewBookForm):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        #self.setMaximumSize(QtCore.QSize(1212, 562))
        #self.populate_comboboxAreaVisitada()

        '''
        self.onlyInt = QIntValidator()
        self.dniLineEdit.setValidator(self.onlyInt)

        '''
        
        listaPersonalFeban = select_all_personalFeban()
        listaPersonalFeban2 = select_all_personalFeban()
        listaVisitantesDNIS = select_all_visitantesDNI()
        listaVisitantesNombres = select_all_visitantesNombres()
        listaEntidades = select_all_EntidadTabla()
        listaMotivos = select_all_motivoTabla()
        listaAreaVisitada = EncontrarAreasDelBn()
        self.label_advertencia_dni.hide()
        fontMain = QFont()
        fontMain.setPointSize(12)
        #wordList = ["ARENAS ABAD CLAUDIA CECILIA","ASCENZO OSTOLAZA ERNESTO JAVIER","BARCENES JIMENEZ ROOSVETH FELIPE","DE LA ROSA VALVERDE PEDRO LUIS ENRIQUE","GARCIA TELLO PABLO CESAR","GONZALES MOLINA AUGUSTO","HIDALGO MEDINA NISIDA RAQUEL","MONCADA QUISPE LUIS ALBERTO","PANTA ALVA RONNIE FANNY","PARDO FIGUEROA HYNE CESAR ESTANISLAO","PEREZ TAPIA MHIRO EDUARDO","RAMIREZ SANTOS CYNTHIA MAGALY","SIHUINCHA MALDONADO JANET LUZMILA","VALVERDE CHEVEZ MAGALI ELIZABETH","VARGAS BASTANTE PAMELA DEL CARMEN","VASQUEZ SANTA MARIA CHRISTIAN WILBER","VELASQUEZ CHIPANA DEYVI JHONATHAN","ZAGACETA DURAND NATALY"]
        #lineEdit = QLineEdit(self)
        completer = QCompleter(listaPersonalFeban, self)
        #completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        completer.popup().setFont(fontMain)
        #self.titleLineEdit.setCompleter(completer)
        completer2 = QCompleter(listaPersonalFeban2, self)
        #completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer2.setFilterMode(Qt.MatchContains)
        completer2.popup().setFont(fontMain)

        completerAL = QCompleter(listaAreaVisitada, self)
        #completer.setCaseSensitivity(Qt.CaseInsensitive)
        completerAL.setFilterMode(Qt.MatchContains)
        completerAL.popup().setFont(fontMain)

        completerVisitantesDNI=QCompleter(listaVisitantesDNIS,self)
        completerVisitantesNombres=QCompleter(listaVisitantesNombres,self)
        completerEntidades=QCompleter(listaEntidades,self)
        completerMotivos=QCompleter(listaMotivos,self)

        completerVisitantesDNI.setFilterMode(Qt.MatchContains)
        completerVisitantesDNI.popup().setFont(fontMain)
        completerVisitantesNombres.setFilterMode(Qt.MatchContains)
        completerVisitantesNombres.popup().setFont(fontMain)
        completerEntidades.setFilterMode(Qt.MatchContains)
        completerEntidades.popup().setFont(fontMain)
        completerMotivos.setFilterMode(Qt.MatchContains)
        completerMotivos.popup().setFont(fontMain)

        
        self.titleLineEdit.textChanged.connect(lambda: (self.titleLineEdit.setCompleter(completer)))
        self.titleLineEdit.textChanged.connect(lambda: (self.to_upperTitle(self.titleLineEdit.text())))
        
        self.categoryLineEdit.textChanged.connect(lambda: (self.categoryLineEdit.setCompleter(completer2)))
        self.categoryLineEdit.textChanged.connect(lambda: (self.to_upperCategory(self.categoryLineEdit.text())))
        
        self.dniLineEdit.textChanged.connect(lambda: (self.dniLineEdit.setCompleter(completerVisitantesDNI)))
        
        self.dniLineEdit.textChanged.connect(lambda:(self.VerificarDni(self.dniLineEdit.text())))
        self.titleLineEdit.textChanged.connect(lambda:(self.VerificarAutoriza(self.titleLineEdit.text())))
        self.nombreVisitanteLineEdit.textChanged.connect(lambda: (self.nombreVisitanteLineEdit.setCompleter(completerVisitantesNombres)))
        self.nombreVisitanteLineEdit.textChanged.connect(lambda: (self.to_upperVisitante(self.nombreVisitanteLineEdit.text())))
        self.areaVisitadaLineEdit.textChanged.connect(lambda: (self.areaVisitadaLineEdit.setCompleter(completerAL)))
        self.areaVisitadaLineEdit.textChanged.connect(lambda: (self.to_upperAreavisitante(self.areaVisitadaLineEdit.text())))
        self.areaVisitadaLineEdit.textChanged.connect(lambda:(self.VerificarArea(self.areaVisitadaLineEdit.text())))

        self.nombreVisitanteLineEdit.textChanged.connect(lambda: (self.VerificarNombreVisitante(self.nombreVisitanteLineEdit.text())))

        self.categoryLineEditEntidadEmpresa.textChanged.connect(lambda: (self.categoryLineEditEntidadEmpresa.setCompleter(completerEntidades)))
        self.categoryLineEditEntidadEmpresa.textChanged.connect(lambda: (self.to_upperEntidad(self.categoryLineEditEntidadEmpresa.text())))

        self.motivoVisitaLineEdit.textChanged.connect(lambda: (self.motivoVisitaLineEdit.setCompleter(completerMotivos)))
        self.motivoVisitaLineEdit.textChanged.connect(lambda: (self.to_upperMotivo(self.motivoVisitaLineEdit.text())))
        
        horaActual=self.ObtenerHoraActual()
        self.horaIngresoLineEdit.setText(horaActual)

        fmt = QTextCharFormat()
        fmt.setFontCapitalization(QFont.AllUppercase)
        self.descriptionTextedit.setCurrentCharFormat(fmt)
        #self.descriptionTextedit.textChanged.connect(lambda: (self.to_upperObservacion(self.descriptionTextedit.toPlainText())))
        
        
        
        self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)

        #self.titleLineEdit.returnPressed.connect(self.addButton.click)
        #self.categoryLineEdit.returnPressed.connect(self.addButton.click)

        #self.dniLineEdit.returnPressed.connect(self.addButton.click)
        #self.nombreVisitanteLineEdit.returnPressed.connect(self.addButton.click)
        #self.categoryLineEdit.returnPressed.connect(self.addButton.click)
        #self.horaIngresoLineEdit.returnPressed.connect(self.addButton.click)
        #self.horaSalidaLineEdit.returnPressed.connect(self.addButton.click)
        #self.motivoVisitaLineEdit.returnPressed.connect(self.addButton.click)
        self.descriptionTextedit.setTabChangesFocus(True);
        
    
    def populate_inputs(self):

        #self.titleLineEdit.setText(data[1])
        #elf.categoryLineEdit.setText(data[2])
        #self.pageQtySpinBox.setValue(data[3])
        #self.pageReadQtySpinBox_2.setValue(data[4])
        #self.filePathLineEdit.setText(data[5])
        #self.descriptionTextedit.setText(data[6])
        self.ast_autoriza.hide()
        self.ast_aquienvisita.hide()
        self.label_nota_obligatoria.hide()
        self.ast_dni.hide()
        self.ast_visitante.hide()
        self.ast_entidadempresa.hide()
        self.ast_horaingreso.hide()
        self.ast_motivo.hide()
        self.ast_area.hide()
        self.ast_fecha.hide()
        self.ast_piso.hide()
        self.ast_estado.hide()


        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        print("d12222 =", d1)
        fechaConv = d1
        fechaConv2 = fechaConv.replace("/", "-")
        print(fechaConv2)
        qdate = QDate.fromString(fechaConv2, "d-MM-yyyy")
        
        print("--.DATE: "+str(qdate))

        self.dateEditNuevo.setDate(qdate)
  
    def VerificarDni(self,dni):
        print("EL DNI EN LABEL ES:"+dni)
        if (ExisteDni(dni)):
            print("DNI SI EXISTE - Verificacion!")
            nombreEncontrado= EncontrarDni(dni)
            print("NOMBRE ENCONTRADO:"+str(nombreEncontrado))
            self.nombreVisitanteLineEdit.setText(nombreEncontrado)
        else:
            print("DNI NO EXISTE - Verificacion!")
            #self.nombreVisitanteLineEdit.setText("")

    def VerificarAutoriza(self,nombreautoriza):
        print("EL nombreautoriza es:"+nombreautoriza)
        if (ExisteAutoriza(nombreautoriza)):
            print("DNI SI EXISTE - Verificacion!")
            areaEncontrada= EncontrarAutorizaArea(nombreautoriza)
            print("NOMBRE ENCONTRADO:"+str(areaEncontrada))
            self.areaVisitadaLineEdit.setText(areaEncontrada)
            self.categoryLineEdit.setText(nombreautoriza)
        else:
            print("DNI NO EXISTE - Verificacion!")


    def VerificarNombreVisitante(self,NombreVisitante):
        print("EL Nombre del Visitantes EN LABEL ES:"+NombreVisitante)
        if (ExisteNombreVisitante(NombreVisitante)):
            print("NombreVisitante SI EXISTE - Verificacion!")
            DniEncontrado= EncontrarNombreVisitante(NombreVisitante)
            print("NOMBRE Visitante:"+str(DniEncontrado))
            self.dniLineEdit.setText(DniEncontrado)
        else:
            print("NombreVisitante NO EXISTE - Verificacion!")
            #self.nombreVisitanteLineEdit.setText("")        

    def check_inputs(self):
        autoriza = self.titleLineEdit.text()
        autoriza=autoriza.strip()

        aquienvisita = self.categoryLineEdit.text()
        autoriza=autoriza.strip()

        areavisitada = self.areaVisitadaLineEdit.text()
        areavisitada=areavisitada.strip()
        #fechanuevo =self.dateEditNuevo.text()
        dni = self.dniLineEdit.text()
        dni=dni.strip()

        visitante = self.nombreVisitanteLineEdit.text()
        visitante=visitante.strip()

        entidadempresa = self.categoryLineEditEntidadEmpresa.text()
        entidadempresa=entidadempresa.strip()

        horaingreso = self.horaIngresoLineEdit.text()
        horaingreso=horaingreso.strip()

        horasalida = self.horaSalidaLineEdit.text()
        horasalida=horasalida.strip()

        motivovisita = self.motivoVisitaLineEdit.text()
        motivovisita=motivovisita.strip()
        

        errors_count = 0
        if autoriza == "":
            self.ast_autoriza.show()
            self.label_nota_obligatoria.show()
            errors_count += 1
        else:
            self.ast_autoriza.hide()

        if aquienvisita == "":
            self.ast_aquienvisita.show()
            self.label_nota_obligatoria.show()
            print("El campo aquienvisita es obligatorio")
            errors_count +=1
        else:
            self.ast_aquienvisita.hide()

        if areavisitada == "":
            print("El campo areavisitada es obligatorio")
            self.ast_area.show()
            self.label_nota_obligatoria.show()
            errors_count +=1
        else:
            self.ast_area.hide()

        if dni == "":
            print("Debe ingresar un DNI")
            self.ast_dni.show()
            self.label_nota_obligatoria.show()
            errors_count +=1
        else:
            self.ast_dni.hide()

        
        if visitante == "":
            print("Debe seleccionar un visitante")
            self.ast_visitante.show()
            self.label_nota_obligatoria.show()
            errors_count +=1
        else:
            self.ast_visitante.hide()

        if entidadempresa == "":
            print("Debe seleccionar un entidadempresa")
            self.ast_entidadempresa.show()
            self.label_nota_obligatoria.show()
            errors_count +=1
        else:
            self.ast_entidadempresa.hide()
        
        if horaingreso == "":
            print("Debe seleccionar un horaingreso")
            self.ast_horaingreso.show()
            self.label_nota_obligatoria.show()
            errors_count +=1
        else:
            self.ast_horaingreso.hide()
        
        
        if motivovisita == "":
            print("Debe seleccionar un motivovisita")
            self.ast_motivo.show()
            self.label_nota_obligatoria.show()
            errors_count +=1
        else:
            self.ast_motivo.hide()
        
        if errors_count==0:
            return (True)
            
        
    def add_book(self):
        
        autoriza = self.titleLineEdit.text()
        autoriza=autoriza.strip()
        aquienvisita = self.categoryLineEdit.text()
        aquienvisita=aquienvisita.strip()

        areavisitada = self.areaVisitadaLineEdit.text()
        areavisitada=areavisitada.strip()
        fechanuevo =self.dateEditNuevo.text()
        fechanuevo=fechanuevo.strip()

        dni = self.dniLineEdit.text()
        dni=dni.strip()

        visitante = self.nombreVisitanteLineEdit.text()
        visitante=visitante.strip()

        entidadempresa = self.categoryLineEditEntidadEmpresa.text()
        entidadempresa=entidadempresa.strip()

        horaingreso = self.horaIngresoLineEdit.text()
        horaingreso=horaingreso.strip()

        horasalida = self.horaSalidaLineEdit.text()
        horasalida=horasalida.strip()

        motivovisita = self.motivoVisitaLineEdit.text()
        motivovisita=motivovisita.strip()

        observaciones1 = self.descriptionTextedit.toPlainText()
        observaciones= observaciones1.upper()
        piso = self.comboBoxPiso.currentText()
        estado = self.comboBoxEstado.currentText()
        self.label_advertencia_dni.hide()
        print("NOMBRE ACTUAL: "+visitante)
        self.ast_dni.hide()
        self.ActualizarVisitante(dni,visitante)
        if self.check_inputs():
            #new_path = shutil.copy(path, "book_files")
            self.label_nota_obligatoria.hide()
            data = (fechanuevo, dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada, piso,horaingreso,horasalida,observaciones,estado) 
            self.AnadirNuevos(dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada) 
            if insert_book(data):
                self.clean_inputs()
                msg_boxes.correct_msgbox("¡Registro Exitoso!","¡Se registró exitosamente!")
                self.parent.refresh_table_from_child_window()
                self.close()
            else: 
                print("ERROR EN EL REGISTRO!")
            '''
            if(len(dni)!=8):
                self.label_advertencia_dni.show()
                self.ast_dni.show()
            else:
            '''    

    def clean_inputs(self):
        self.titleLineEdit.clear()
        self.categoryLineEdit.clear()
        self.areaVisitadaLineEdit.clear()
        self.dniLineEdit.clear()
        self.nombreVisitanteLineEdit.clear()
        self.categoryLineEditEntidadEmpresa.clear()
        self.horaIngresoLineEdit.clear()
        self.horaSalidaLineEdit.clear()
        self.motivoVisitaLineEdit.clear()
        self.comboBoxPiso.setCurrentText("")
        self.comboBoxEstado.setCurrentText("")

    def select_file(self):
        file_path = QFileDialog.getOpenFileName()[0]
        self.filePathLineEdit.setText(file_path)


    def populate_comboboxPiso(self):
        cb_options = ("","SÓTANO 1", "SÓTANO 2", "SÓTANO 3", "SÓTANO 4", "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26")
        self.comboBoxPiso.addItems(cb_options)
    
    def populate_comboboxEstado(self):
        cb_options = ("PENDIENTE", "REGISTRADO")
        self.comboBoxEstado.addItems(cb_options)
    
    

    def populate_comboboxAreaVisitada(self):
        cb_options = ("","ÁREA DE COBRANZA Y RECUPERACIONES","ÁREA DE COMPRAS","ÁREA DE CONTABILIDAD","ÁREA DE IMAGEN Y COMUNICACIONES","ÁREA DE INFRAESTRUCTURA","ÁREA DE PERSONAL","ÁREA DE SEGURIDAD Y TRANSPORTE","ÁREA DE SEGURO MEDICO","ÁREA DE TESORERÍA","AUDITORÍA INTERNA","DIVISIÓN DE SERVICIOS AL AFILIADO","DIVISIÓN DE SERVICIOS INTERNOS","FEBAN","FEBAN ADMINISTRATIVA","FEBAN GERENCIAS","GERENCIA","UNIDAD DE BIENESTAR SOCIAL","UNIDAD DE CEREBANES","UNIDAD DE CRÉDITOS Y SEGUROS","UNIDAD DE FINANZAS","UNIDAD DE LEGAL","UNIDAD DE LOGÍSTICA","UNIDAD DE PAM","UNIDAD DE RECURSOS HUMANOS","UNIDAD TECNOLOGÍA DE LA INFORMACIÓN")
        self.comboBoxAreaVisitada.addItems(cb_options)
        
    def config_comboBoxes(self):
        font1 = QFont()
        font1.setPointSize(12)
        
        #line_editcomboBoxAreaVisitada = self.comboBoxAreaVisitada.lineEdit()  
        #line_editcomboBoxAreaVisitada.setFont(font1)

        #line_editcomboBoxPiso = self.comboBoxPiso.lineEdit()  
        #line_editcomboBoxPiso.setFont(font1)

        #line_editcomboBoxEstado = self.comboBoxEstado.lineEdit()  
        #line_editcomboBoxEstado.setFont(font1)
        #line_edit.setAlignment(QtCore.Qt.AlignCenter)

    def to_upperTitle(self, txt):
        pos2=self.titleLineEdit.cursorPosition()
        self.titleLineEdit.setText(txt.upper())
        self.titleLineEdit.setCursorPosition(pos2)
    
    def to_upperCategory(self, txt):
        pos2=self.categoryLineEdit.cursorPosition()
        self.categoryLineEdit.setText(txt.upper())
        self.categoryLineEdit.setCursorPosition(pos2)
    

    
    def to_upperVisitante(self, txt):
        pos2=self.nombreVisitanteLineEdit.cursorPosition()
        self.nombreVisitanteLineEdit.setText(txt.upper())
        self.nombreVisitanteLineEdit.setCursorPosition(pos2)

    def to_upperAreavisitante(self, txt):
        pos2=self.areaVisitadaLineEdit.cursorPosition()
        self.areaVisitadaLineEdit.setText(txt.upper())
        self.areaVisitadaLineEdit.setCursorPosition(pos2)
    
    def to_upperEntidad(self, txt):
        pos2=self.categoryLineEditEntidadEmpresa.cursorPosition()
        self.categoryLineEditEntidadEmpresa.setText(txt.upper())
        self.categoryLineEditEntidadEmpresa.setCursorPosition(pos2)
    
    
    def to_upperMotivo(self, txt):
        pos2=self.motivoVisitaLineEdit.cursorPosition()
        self.motivoVisitaLineEdit.setText(txt.upper())
        self.motivoVisitaLineEdit.setCursorPosition(pos2)

    def AnadirNuevos(self, dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada):
        if (ExisteDni(dni)):
            print("DNI SI EXISTE!")
        else:
            print("DNI NO EXISTE!")
            insert_NuevoDNI(dni,visitante)
        
        if (ExisteEntidad(entidadempresa)):
            print("Entidad SI EXISTE!")
        else:
            print("Entidad NO EXISTE!")
            insert_NuevoEntidad(entidadempresa) 
        
        if (ExisteMotivo(motivovisita)):
            print("Motivo SI EXISTE!")
        else:
            print("Motivo NO EXISTE!")
            insert_NuevoMotivo(motivovisita) 
        
        if (ExisteVisita(aquienvisita)):
            print("Visita SI EXISTE!")
        else:
            print("Visita NO EXISTE!")
            insert_NuevoVisita(aquienvisita) 

        if (ExisteAutoriza(autoriza)):
            print("Autoriza SI EXISTE!")
            UpdateAutoriza(autoriza,areavisitada)
        else:
            print("Autoriza NO EXISTE!")
            insert_NuevoAutoriza(autoriza,areavisitada)    

    def ObtenerHoraActual(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print("Current Time =", current_time)
        return current_time
    
    def ActualizarVisitante(self,dni,visitante):
        nombreEncontrado= EncontrarDni(dni)
        if nombreEncontrado==visitante:
            print("No hay nada que actualizar")
        else:
            print("NOMBRE NUEVO:: "+visitante)
            UpdateVisitante(dni,visitante)
            print("Actualizado!!!")

    
    def ListaAreas(self):
        AreasDelBN=EncontrarAreasDelBn()
        return AreasDelBN

    def CompletarPiso(self,pisoseleccionado):
        print("EL nombreautoriza es:"+pisoseleccionado)
        if pisoseleccionado=="SÓTANO 1":
            pisoseleccionado = "ST1"
        if pisoseleccionado=="SÓTANO 2":
            pisoseleccionado = "ST2"
        if pisoseleccionado=="SÓTANO 3":
            pisoseleccionado = "ST3"
        if pisoseleccionado=="SÓTANO 4":
            pisoseleccionado = "ST4"
        areaEncontrada= EncontrarPisoSeleccionado(pisoseleccionado)+""
        print(areaEncontrada)
        if areaEncontrada=="0":
            print("no hay cambios")
        else:
            self.areaVisitadaLineEdit.setText(areaEncontrada)
        
    def VerificarArea(self,areaseleccionada):
        print("EL areaseleccionada es:"+areaseleccionada)
        pisoencontrado= EncontrarAreaSeleccionada(areaseleccionada)
        
        if pisoencontrado=="0":
            print("no hay cambios")
        else:
            if pisoencontrado=="ST1":
                pisoencontrado = "SÓTANO 1"
            if pisoencontrado=="ST2":
                pisoencontrado = "SÓTANO 2"
            if pisoencontrado=="ST3":
                pisoencontrado = "SÓTANO 3"
            if pisoencontrado=="ST4":
                pisoencontrado = "SÓTANO 4"
            self.comboBoxPiso.setCurrentText(pisoencontrado)