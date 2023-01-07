from PySide6 import QtWidgets as QW
# Creamos una nueva app
app = QW.QApplication()
# # Creamos la ventana principal y la mostramos
# window = QW.QMainWindow()
# window.resize(200, 100)
# window.show()
# # Iniciamos el bucle
# app.exec_()



def hola(self):
    print("¡Hola mundo!")


# Creamos la ventana principal
window = QW.QMainWindow()
window.resize(200, 100)
# ...
# Creamos el botón y lo conectamos
button = QW.QPushButton("Hola", window)
button.clicked.connect(hola)
# Creamos el botón y lo conectamos
button = QW.QPushButton("Hola", window)
button.clicked.connect(hola)
# Mostramos la ventana principal
window.show()
app.exec_()

#Nuestra propia clase
class MainWindow(QW.QMainWindow):
# Creamos nuestra ventana a partir de un QMainWindow
    def _init_(self):
        # Con super ejecutamos su propio constructor
        # Así se crea la ventana en su propia instancia self
        super()._init_()
        # Redimensionamos y añadimos el botón
        self.resize(200, 100)
        button = QW.QPushButton("Hola", self)
        button.clicked.connect(self.hola)
        # Finalmente mostramos la ventana
        self.show()
    def hola(self):
        print("¡Hola mundo!")
# Creamos la aplicación, la ventana e iniciamos el bucle
app = QW.QApplication()
window = MainWindow()
app.exec_()



