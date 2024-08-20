from typing import List

from PySide2 import QtCore
from views.login_window import LoginRegistroForm
from PySide2.QtWidgets import QWidget, QTableWidgetItem,QMessageBox
from views.main_windows import *
from db.books import BuscarUsuario
#from pys2_msgboxes import msg_boxes
#from pys2_msg_boxes import msgboxes
import time

class LoginWindowForm(QWidget,LoginRegistroForm):
    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.ingresarButton.clicked.connect(self.open_main_window)
        #self.label_nota_obligatoria.hide()
        self.progressBar.setValue(0)
        self.label_validacion_password.hide()
        self.label_validacion_usuario.hide()
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setPlaceholderText("Contraseña")
        self.usuarioLineEdit.setPlaceholderText("Usuario")
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint)
        #self.setMaximumSize(QtCore.QSize(480, 327))
        self.passwordLineEdit.returnPressed.connect(self.ingresarButton.click)
        self.usuarioLineEdit.returnPressed.connect(self.ingresarButton.click)
        self.setWindowIcon(QIcon('./pys2_msgboxes/icons/banco_icon.png'))


    def open_main_window(self):
        from controllers.main_window import ListBookWindow
        window= ListBookWindow(self)
        
        nombreUsuario= self.usuarioLineEdit.text()
        nombreUsuario=nombreUsuario.strip()
        password=self.passwordLineEdit.text()
        passwordEncontrada=BuscarUsuario(nombreUsuario)
        
        print("PASS ENCNTRADA:: "+str(passwordEncontrada))
        if(passwordEncontrada!=""):
            
            self.label_validacion_usuario.hide()
            if(password==passwordEncontrada):
                print("Acceso Correcto")
                
                self.label_validacion_password.hide()
                for i in range(0,99):
                    time.sleep(0.005)
                    self.progressBar.setValue(i)
                window.show()
                self.hide()
            else:
                print("ERROR DE CONTRASEÑA")    
                
                self.label_validacion_password.show()
        else:
            print("NO HAY USUARIO")
            
            self.label_validacion_usuario.show()
        