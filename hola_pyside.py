from PySide6 import QtWidgets as QW
# Creamos una nueva app
app = QW.QApplication()
# Creamos la ventana principal y la mostramos
window = QW.QMainWindow()
window.resize(200, 100)
window.show()
# Iniciamos el bucle
app.exec_()



def hola(self):
 print("¡Hola mundo!")
# ...
# Creamos el botón y lo conectamos
button = QW.QPushButton("Hola", window)
button.clicked.connect(hola)

# Creamos la ventana principal
window = QW.QMainWindow()
window.resize(200, 100)
# Creamos el botón y lo conectamos
button = QW.QPushButton("Hola", window)
button.clicked.connect(hola)
# Mostramos la ventana principal
window.show()





