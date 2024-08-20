from sqlite3.dbapi2 import ProgrammingError
from typing import Text
from PySide2.QtGui import *
from PySide2.QtWidgets import QWidget, QFileDialog,QCompleter
from PySide2.QtCore import Qt, QDate
from PySide2 import QtCore
from views.marcar_salida import MarcarSalidaForm
from db.books import select_book_by_id,UpdateAutoriza,EncontrarAutorizaArea, update_book,select_all_personalFeban, select_all_EntidadTabla,select_all_motivoTabla,select_all_visitantesDNI, select_all_visitantesNombres,EncontrarDni,ExisteDni,ExisteAutoriza,ExisteEntidad,ExisteMotivo,ExisteVisita,insert_NuevoEntidad,insert_NuevoAutoriza,insert_NuevoDNI,insert_NuevoMotivo,insert_NuevoVisita,EncontrarNombreVisitante,ExisteNombreVisitante,UpdateVisitante,EncontrarAreasDelBn,EncontrarPisoSeleccionado,EncontrarAreaSeleccionada
from pys2_msgboxes import msg_boxes
from PySide2.QtGui import QFont
from datetime import  datetime
import re
import os
import shutil

class MarcarSalida(QWidget, MarcarSalidaForm):
    def __init__(self, parent=None, _id=None):
        self._id=_id
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        #self.setMaximumSize(QtCore.QSize(1212, 573))
        #self.populate_comboboxAreaVisitada()
        self.populate_comboboxPiso()
        self.populate_comboboxEstado()
        self.populate_inputs()
        self.config_comboBoxes()
        listaAreaVisitada = EncontrarAreasDelBn()
        '''
        self.onlyInt = QIntValidator()
        self.dniLineEdit.setValidator(self.onlyInt)
        '''
        
        
        fontMain = QFont()
        fontMain.setPointSize(12)
        
        
        listaPersonalFeban = select_all_personalFeban()
        completer = QCompleter(listaPersonalFeban, self)
        completer.setFilterMode(Qt.MatchContains)
        completer.popup().setFont(fontMain)

        listaPersonalFeban2 = select_all_personalFeban()
        completer2 = QCompleter(listaPersonalFeban2, self)
        completer2.setFilterMode(Qt.MatchContains)
        completer2.popup().setFont(fontMain)

        listaVisitantesDNIS = select_all_visitantesDNI()
        listaVisitantesNombres = select_all_visitantesNombres()
        listaEntidades = select_all_EntidadTabla()
        listaMotivos = select_all_motivoTabla()

        completerVisitantesDNI=QCompleter(listaVisitantesDNIS,self)
        completerVisitantesNombres=QCompleter(listaVisitantesNombres,self)
        completerEntidades=QCompleter(listaEntidades,self)
        completer2.popup().setFont(fontMain)
        completerMotivos=QCompleter(listaMotivos,self)
   
        completerVisitantesDNI.setFilterMode(Qt.MatchContains)
        completerVisitantesDNI.popup().setFont(fontMain)
        completerVisitantesNombres.setFilterMode(Qt.MatchContains)
        completerVisitantesNombres.popup().setFont(fontMain)
        completerEntidades.setFilterMode(Qt.MatchContains)
        completerEntidades.popup().setFont(fontMain)
        completerMotivos.setFilterMode(Qt.MatchContains)
        completerMotivos.popup().setFont(fontMain)

        completerAL = QCompleter(listaAreaVisitada, self)
        #completer.setCaseSensitivity(Qt.CaseInsensitive)
        completerAL.setFilterMode(Qt.MatchContains)
        completerAL.popup().setFont(fontMain)
        
        self.titleLineEdit.textChanged.connect(lambda: (self.to_upperTitle(self.titleLineEdit.text())))
        self.titleLineEdit.textChanged.connect(lambda: (self.titleLineEdit.setCompleter(completer)))
        self.categoryLineEdit.textChanged.connect(lambda: (self.to_upperCategory(self.categoryLineEdit.text())))       
        self.categoryLineEdit.textChanged.connect(lambda: (self.categoryLineEdit.setCompleter(completer2)))
        
        self.dniLineEdit.textChanged.connect(lambda: (self.dniLineEdit.setCompleter(completerVisitantesDNI)))
        self.areaVisitadaLineEdit.textChanged.connect(lambda:(self.VerificarArea(self.areaVisitadaLineEdit.text())))

        self.dniLineEdit.textChanged.connect(lambda:(self.VerificarDni(self.dniLineEdit.text())))
        self.titleLineEdit.textChanged.connect(lambda:(self.VerificarAutoriza(self.titleLineEdit.text())))
        self.nombreVisitanteLineEdit.textChanged.connect(lambda: (self.nombreVisitanteLineEdit.setCompleter(completerVisitantesNombres)))
        self.nombreVisitanteLineEdit.textChanged.connect(lambda: (self.to_upperVisitante(self.nombreVisitanteLineEdit.text())))
        self.nombreVisitanteLineEdit.textChanged.connect(lambda: (self.VerificarNombreVisitante(self.nombreVisitanteLineEdit.text())))
        self.comboBoxPiso.currentTextChanged.connect(lambda:(self.CompletarPiso(self.comboBoxPiso.currentText())))

        self.categoryLineEditEntidadEmpresa.textChanged.connect(lambda: (self.categoryLineEditEntidadEmpresa.setCompleter(completerEntidades)))
        self.categoryLineEditEntidadEmpresa.textChanged.connect(lambda: (self.to_upperEntidad(self.categoryLineEditEntidadEmpresa.text())))

        self.motivoVisitaLineEdit.textChanged.connect(lambda: (self.motivoVisitaLineEdit.setCompleter(completerMotivos)))
        self.motivoVisitaLineEdit.textChanged.connect(lambda: (self.to_upperMotivo(self.motivoVisitaLineEdit.text())))
        self.areaVisitadaLineEdit.textChanged.connect(lambda: (self.areaVisitadaLineEdit.setCompleter(completerAL)))
        self.areaVisitadaLineEdit.textChanged.connect(lambda: (self.to_upperAreavisitante(self.areaVisitadaLineEdit.text())))

        horaActual=self.ObtenerHoraActual()
        self.horaSalidaLineEdit.setText(horaActual)

        fmt1 = QTextCharFormat()
        fmt1.setFontCapitalization(QFont.AllUppercase)
        self.descriptionTextedit.setCurrentCharFormat(fmt1)

                
        
        self.editButton.clicked.connect(self.edit_book)

        #self.titleLineEdit.returnPressed.connect(self.editButton.click)
        #self.categoryLineEdit.returnPressed.connect(self.editButton.click)
        
        #self.dniLineEdit.returnPressed.connect(self.editButton.click)
        #self.nombreVisitanteLineEdit.returnPressed.connect(self.editButton.click)
        #self.categoryLineEdit.returnPressed.connect(self.editButton.click)
        #self.horaIngresoLineEdit.returnPressed.connect(self.editButton.click)
        #self.horaSalidaLineEdit.returnPressed.connect(self.editButton.click)
        #self.motivoVisitaLineEdit.returnPressed.connect(self.editButton.click)
        
        self.descriptionTextedit.setTabChangesFocus(True);
        self.editButton.setAutoDefault(True)

        self.label_advertencia_dni.hide()
        self.cancelButton.clicked.connect(self.close)
        self.comboBoxEstado.setCurrentIndex(1)

    def populate_inputs(self):
        self.ast_autoriza.hide()
        self.ast_aquienvisita.hide()
        self.label_nota_obligatoria.hide()
        self.ast_dni.hide()
        self.ast_visitante.hide()
        self.ast_entidadempresa.hide()
        self.ast_horaingreso.hide()
        self.ast_horaSalida.hide()
        self.ast_motivo.hide()
        self.ast_area.hide()
        self.ast_fecha.hide()
        self.ast_piso.hide()
        self.ast_estado.hide()

        fmt2 = QTextCharFormat()
        fmt2.setFontCapitalization(QFont.AllUppercase)
        self.descriptionTextedit.setCurrentCharFormat(fmt2)
        data = select_book_by_id(self._id)
        
        #self.titleLineEdit.setText(data[1])
        #elf.categoryLineEdit.setText(data[2])
        #self.pageQtySpinBox.setValue(data[3])
        #self.pageReadQtySpinBox_2.setValue(data[4])
        #self.filePathLineEdit.setText(data[5])
        #self.descriptionTextedit.setText(data[6])
        fechaConv = data[1]
        fechaConv2 = fechaConv.replace("/", "-")
        #print(fechaConv2)

        qdate = QDate.fromString(fechaConv2, "d-MM-yyyy")
        #qhoraIngreso = QTime.fromString(data[10], "hh:mm")
        #qHoraSalida = QTime.fromString(data[11], "hh:mm")
        

        #print("--.DATE: "+str(qdate))
        self.titleLineEdit.setText(data[7])
        self.categoryLineEdit.setText(data[6])
        self.areaVisitadaLineEdit.setText(data[8])
        self.dateEditNuevo.setDate(qdate)
        self.dniLineEdit.setText(data[2])
        self.nombreVisitanteLineEdit.setText(data[3])
        self.categoryLineEditEntidadEmpresa.setText(data[4])
        self.horaIngresoLineEdit.setText(data[10])
        self.horaSalidaLineEdit.setText(data[11])

        self.motivoVisitaLineEdit.setText(data[5])
        #print("CURRENT INDEX: "+str(self.comboBoxMotivoVisita.currentIndex()))
        #self.comboBoxMotivoVisita.setCurrentIndex(data[5])
        self.descriptionTextedit.setText(data[12])
        self.comboBoxPiso.setCurrentText(data[9])
        self.comboBoxEstado.setCurrentText(data[13])

    def check_inputs(self):
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
        
        if horasalida == "":
            print("Debe seleccionar un horaSalida")
            self.ast_horaSalida.show()
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
        if errors_count == 0:
            return True

    def select_file(self):
        self.old_path = self.filePathLineEdit.text()
        file_path = QFileDialog.getOpenFileName()[0]
        self.filePathLineEdit.setText(file_path)

        print(file_path)

    def edit_book(self):
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

        observaciones = self.descriptionTextedit.toPlainText()
        observaciones=observaciones.strip()

        piso = self.comboBoxPiso.currentText()
        estado = self.comboBoxEstado.currentText()
        observaciones= observaciones.upper()
        
        self.ActualizarVisitante(dni,visitante)
        self.label_advertencia_dni.hide()
        self.ast_dni.hide()
        data = (fechanuevo, dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada, piso,horaingreso,horasalida,observaciones,estado) 
        print("QUE DATA HAY: "+str(data))
        if self.check_inputs():
            self.label_nota_obligatoria.hide()
            self.AnadirNuevos(dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada) 
            if update_book(self._id, data):
                msg_boxes.marc_salida_msgbox("Marcar Salida","¡Se marcó la salida correctamente!")
                self.parent.refresh_table_from_child_window()
                print("MODIF EXIT")
                self.close()
        
            
            '''
            if(len(dni)!=8):
                self.label_advertencia_dni.show()
                self.ast_dni.show()
            else:
            ''' 


            
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

        #line_editcomboBoxMotivoVisita = self.comboBoxMotivoVisita.lineEdit()  
        #line_editcomboBoxMotivoVisita.setFont(font1)

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
    
    def to_upperEntidad(self, txt):
        pos2=self.categoryLineEditEntidadEmpresa.cursorPosition()
        self.categoryLineEditEntidadEmpresa.setText(txt.upper())
        self.categoryLineEditEntidadEmpresa.setCursorPosition(pos2)

    def to_upperMotivo(self, txt):
        pos2=self.motivoVisitaLineEdit.cursorPosition()
        self.motivoVisitaLineEdit.setText(txt.upper())
        self.motivoVisitaLineEdit.setCursorPosition(pos2)

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

    def AnadirNuevos(self, dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,area):
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
            UpdateAutoriza(autoriza,area)
        else:
            print("Autoriza NO EXISTE!")
            insert_NuevoAutoriza(autoriza,area)    

    def ActualizarVisitante(self,dni,visitante):
        nombreEncontrado= EncontrarDni(dni)
        if nombreEncontrado==visitante:
            print("No hay nada que actualizar")
        else:
            UpdateVisitante(dni,visitante)
            print("Actualizado!!!")

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


    def ObtenerHoraActual(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print("Current Time =", current_time)
        return current_time

    def to_upperAreavisitante(self, txt):
        pos2=self.areaVisitadaLineEdit.cursorPosition()
        self.areaVisitadaLineEdit.setText(txt.upper())
        self.areaVisitadaLineEdit.setCursorPosition(pos2)
    
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