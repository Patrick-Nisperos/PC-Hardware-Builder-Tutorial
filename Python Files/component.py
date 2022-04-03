from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    xpos, ypos, width, height = 200,200,300,300
    win.setGeometry(xpos, ypos, width, height)
    win.setWindowTitle("Components")

    win.show()
    sys.exit(app.exec_())

window()

    
    

