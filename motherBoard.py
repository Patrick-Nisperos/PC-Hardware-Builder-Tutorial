from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
import sys
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.acceptDrops()
        # set the title
        self.setWindowTitle("MotherBoard Window")

        self.setStyleSheet("background-color: white;")
        # setting  the geometry of window
        self.setGeometry(100, 50, 1600, 1000)

        # loading header
        self.header = QLabel("Intel MotherBoard: Gigabyte Z690 Aorus Pro", self)
        self.header.setFont(QFont("Times", 24))
        self.header.adjustSize()
        self.header.move(400, 0)

        # creating label
        self.image = QLabel(self)

        # loading image
        self.pixmap = QPixmap('media/IntelMotherBoard.jpg')

        # adding image to label and centering it
        self.image.setPixmap(self.pixmap)
        self.image.move(300, 100)

        # Needed! Resize label to image size
        # Otherwise image is super small
        self.image.resize(self.pixmap.width(),
                          self.pixmap.height())


        # show all the widgets
        self.show()

if __name__ == "__main__":

    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())