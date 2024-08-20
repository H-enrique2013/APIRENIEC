from PySide2.QtWidgets import QApplication
from controllers.login_window import LoginWindowForm

#ESTE ES EL INICIO DEL PROYECTO22
if __name__ == "__main__":
    app = QApplication()
    window = LoginWindowForm()
    window.show()
    app.exec_()
