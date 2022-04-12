from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QImage

import PartAnalyzer
from hover import hoverExit, hoverEnter

# Dragging
class DraggableLabel(QLabel):
    def __init__(self,parent, mv_image, mv_width, mv_height, name):
        super(QLabel,self).__init__(parent)
        self.setPixmap(QPixmap("..images/yellowBox.png"))
        self.setScaledContents(True)
        self.image = QPixmap(mv_image).scaled(mv_width,mv_height)
        self.name = name
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
        if(event.button() == Qt.RightButton):
            if(self.name == PartAnalyzer.partNames[0]):
                Ui_MotherBoard.openPartAnalyzer(self, PartAnalyzer.partNames[0], PartAnalyzer.descriptions[0], "../images/i7_cpu.jpg", "../images/ryzen9.jpg", 200, 200, 200, 200)
                #print("cpu clicked")
            elif(self.name == PartAnalyzer.partNames[1]):
                print("gpu clicked")
            elif(self.name == PartAnalyzer.partNames[2]):
                print("cpu-cooler clicked")
            elif(self.name == PartAnalyzer.partNames[3]):
                print("ram clicked")
            elif(self.name == PartAnalyzer.partNames[4]):
                print("ssd clicked")

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        
        mimedata = QMimeData()
        mimedata.setText(self.text())
        mimedata.setImageData(self.pixmap().toImage())

        drag.setMimeData(mimedata)
        #painter = QPainter(self.image)
        #painter.drawPixmap(self.rect(), self.image)
        #painter.end()

        drag.setPixmap(self.image)
        drag.setHotSpot(QPoint(self.x()+self.width()/2,self.y()+30))
        drag.exec_(Qt.CopyAction | Qt.MoveAction)

class my_label(QLabel):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self,event):
        if event.mimeData().hasImage():
            print("event accepted")
            event.accept()
        else:
            print("event rejected")
            event.ignore()
    def dropEvent(self,event):
        if event.mimeData().hasImage():
            self.setPixmap(QPixmap.fromImage(QImage(event.mimeData().imageData())))


class Ui_MotherBoard(object):

    def openPartAnalyzer(self, name, description, image, image2, width, height, width2, height2):
            self.partView = QtWidgets.QMainWindow()
            ui2 = PartAnalyzer.Ui_PartAnalyzer()
            ui2.setupUi(self.partView, "Central Processing Unit", PartAnalyzer.descriptions[0], "../images/i7_cpu.jpg", "../images/ryzen9.JPG", 200, 200, 200, 200)
            self.partView.show()

    def hover_events(self, MainWindow):
        self.cpu_img.leaveEvent = lambda e: hoverExit("cpu", self.hover_actual_description_label)
        self.cpu_img.enterEvent = lambda e: hoverEnter("cpu", self.hover_actual_description_label)
        self.gpu_img.leaveEvent = lambda e: hoverExit("gpu", self.hover_actual_description_label)
        self.gpu_img.enterEvent = lambda e: hoverEnter("gpu", self.hover_actual_description_label)
        self.ram_img1.leaveEvent = lambda e: hoverExit("ram", self.hover_actual_description_label)
        self.ram_img1.enterEvent = lambda e: hoverEnter("ram", self.hover_actual_description_label)
        self.ram_img2.leaveEvent = lambda e: hoverExit("ram", self.hover_actual_description_label)
        self.ram_img2.enterEvent = lambda e: hoverEnter("ram", self.hover_actual_description_label)
        self.cpu_cooler_img.leaveEvent = lambda e: hoverExit("cpu cooler", self.hover_actual_description_label)
        self.cpu_cooler_img.enterEvent = lambda e: hoverEnter("cpu cooler", self.hover_actual_description_label)
        self.ssd_img.leaveEvent = lambda e: hoverExit("ssd", self.hover_actual_description_label)
        self.ssd_img.enterEvent = lambda e: hoverEnter("ssd", self.hover_actual_description_label)


    def setupHardware(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 986)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cpu_label = QtWidgets.QLabel(self.centralwidget)
        self.cpu_label.setGeometry(QtCore.QRect(1040, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        
        self.cpu_label.setFont(font)
        self.cpu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_label.setObjectName("cpu_label")
        self.cpu_img = QtWidgets.QLabel(self.centralwidget)
        self.cpu_img.setGeometry(QtCore.QRect(1070, 110, 91, 81))
        self.cpu_img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cpu_img.setText("")
        self.cpu_img.setPixmap(QtGui.QPixmap("../images/i7_cpu.jpg"))
        self.cpu_img.setScaledContents(True)
        self.cpu_img.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_img.setObjectName("cpu_img")

        self.cpu_cooler_img = QtWidgets.QLabel(self.centralwidget)
        self.cpu_cooler_img.setGeometry(QtCore.QRect(1240, 100, 111, 111))
        self.cpu_cooler_img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cpu_cooler_img.setText("")
        self.cpu_cooler_img.setPixmap(QtGui.QPixmap("../images/cpu_cooler.png"))
        self.cpu_cooler_img.setScaledContents(True)
        self.cpu_cooler_img.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_cooler_img.setObjectName("cpu_cooler_img")
        self.cpu_cooler_label = QtWidgets.QLabel(self.centralwidget)
        self.cpu_cooler_label.setGeometry(QtCore.QRect(1220, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.cpu_cooler_label.setFont(font)
        self.cpu_cooler_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_cooler_label.setObjectName("cpu_cooler_label")
        self.hardware_list_label = QtWidgets.QLabel(self.centralwidget)
        self.hardware_list_label.setGeometry(QtCore.QRect(1100, 10, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.hardware_list_label.setFont(font)
        self.hardware_list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hardware_list_label.setObjectName("hardware_list_label")
        self.gpu_img = QtWidgets.QLabel(self.centralwidget)
        self.gpu_img.setGeometry(QtCore.QRect(1090, 250, 221, 121))
        self.gpu_img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gpu_img.setText("")
        self.gpu_img.setPixmap(QtGui.QPixmap("../images/gpu.png"))
        self.gpu_img.setScaledContents(True)
        self.gpu_img.setAlignment(QtCore.Qt.AlignCenter)
        self.gpu_img.setObjectName("gpu_img")
        self.gpu_label = QtWidgets.QLabel(self.centralwidget)
        self.gpu_label.setGeometry(QtCore.QRect(1130, 210, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.gpu_label.setFont(font)
        self.gpu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gpu_label.setObjectName("gpu_label")
        self.ram_label = QtWidgets.QLabel(self.centralwidget)
        self.ram_label.setGeometry(QtCore.QRect(1140, 370, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.ram_label.setFont(font)
        self.ram_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ram_label.setObjectName("ram_label")
        self.ssd_label = QtWidgets.QLabel(self.centralwidget)
        self.ssd_label.setGeometry(QtCore.QRect(1140, 530, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.ssd_label.setFont(font)
        self.ssd_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ssd_label.setObjectName("ssd_label")
        self.ssd_img = QtWidgets.QLabel(self.centralwidget)
        self.ssd_img.setGeometry(QtCore.QRect(1090, 560, 251, 61))
        self.ssd_img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ssd_img.setText("")
        self.ssd_img.setPixmap(QtGui.QPixmap("../images/m.2_ssd.jpg"))
        self.ssd_img.setScaledContents(True)
        self.ssd_img.setAlignment(QtCore.Qt.AlignCenter)
        self.ssd_img.setObjectName("ssd_img")
        self.ram_img1 = QtWidgets.QLabel(self.centralwidget)
        self.ram_img1.setGeometry(QtCore.QRect(1100, 410, 221, 51))
        self.ram_img1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ram_img1.setText("")
        self.ram_img1.setPixmap(QtGui.QPixmap("../images/ram stick.jpg"))
        self.ram_img1.setScaledContents(True)
        self.ram_img1.setAlignment(QtCore.Qt.AlignCenter)
        self.ram_img1.setObjectName("ram_img1")
        self.ram_img2 = QtWidgets.QLabel(self.centralwidget)
        self.ram_img2.setGeometry(QtCore.QRect(1100, 470, 221, 51))
        self.ram_img2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ram_img2.setText("")
        self.ram_img2.setPixmap(QtGui.QPixmap("../images/ram stick.jpg"))
        self.ram_img2.setScaledContents(True)
        self.ram_img2.setAlignment(QtCore.Qt.AlignCenter)
        self.ram_img2.setObjectName("ram_img2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.hover_events(MainWindow)

        self.hover_actual_description_label = QtWidgets.QLabel(self.centralwidget)
        self.hover_actual_description_label.setGeometry(QtCore.QRect(1100, 680, 241, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hover_actual_description_label.setFont(font)
        self.hover_actual_description_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hover_actual_description_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hover_actual_description_label.setWordWrap(True)
        self.hover_actual_description_label.setObjectName("hover_actual_description_label")
        self.hover_description_label = QtWidgets.QLabel(self.centralwidget)
        self.hover_description_label.setGeometry(QtCore.QRect(1130, 680, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.hover_description_label.setFont(font)
        self.hover_description_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hover_description_label.setObjectName("hover_description_label")

        self.retranslateHardware(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        

    def setupMotherboard(self, MainWindow):

        #Format is as follows for all components
        #Add to the GUI
        #Style sheet for hover and color of label
        #Set Coordinates x1 and y1 for placement x2 and y2 for size
        #Set mouse tracking on for dragging later
        #Clear text so we can have just the highlight w/o text
        #Name the label


        self.motherBoard = QtWidgets.QLabel(MainWindow)
        self.motherBoard.setGeometry(QtCore.QRect(0, 0, 801, 971))
        self.motherBoard.setMouseTracking(True)
        self.motherBoard.setPixmap(QtGui.QPixmap("../images/IntelMotherBoard.jpg"))
        self.motherBoard.setObjectName("MotherBoard")

        #Opacity effect doesn't work with multiple labels 
        #Also tried setting opacity 1 to 0 but it doesnt work
        #Forced to initialize new opacities w/ same values                                      

        self.opacityEffect0 = QGraphicsOpacityEffect()
        self.opacityEffect0.setOpacity(0.3)

        self.opacityEffect1 = QGraphicsOpacityEffect()
        self.opacityEffect1.setOpacity(0.3)

        self.opacityEffect2 = QGraphicsOpacityEffect()
        self.opacityEffect2.setOpacity(0.3)

        self.opacityEffect3 = QGraphicsOpacityEffect()
        self.opacityEffect3.setOpacity(0.3)

        self.opacityEffect4 = QGraphicsOpacityEffect()
        self.opacityEffect4.setOpacity(0.3)

        self.opacityEffect5 = QGraphicsOpacityEffect()
        self.opacityEffect5.setOpacity(0.3)

        self.opacityEffect6 = QGraphicsOpacityEffect()
        self.opacityEffect6.setOpacity(0.3)

        self.opacityEffect7 = QGraphicsOpacityEffect()
        self.opacityEffect7.setOpacity(0.3)

        #CPU ON LABEL
        self.cpu = QtWidgets.QLabel(MainWindow)
        self.cpu.setStyleSheet("QLabel::hover" "{ background-color : yellow; }")
        self.cpu.setGeometry(QtCore.QRect(330, 170, 131, 211))
        self.cpu.setMouseTracking(True)
        self.cpu.clear()
        self.cpu.setObjectName("CPU")
        self.cpu.setGraphicsEffect(self.opacityEffect0)

        self.cpu = DraggableLabel(self.cpu, "../images/i7_cpu.jpg", 91, 81, "CPU").resize(131,211)
        
        self.cpuCable = QtWidgets.QLabel(MainWindow)
        self.cpuCable.setStyleSheet("QLabel::hover"
                                   "{ background-color : yellow; }")
        self.cpuCable.setGeometry(QtCore.QRect(170, 19, 50, 25))
        self.cpuCable.setMouseTracking(True)
        self.cpuCable.clear()
        self.cpuCable.setObjectName("CPU-Cable")
        self.cpuCable.setGraphicsEffect(self.opacityEffect1)

        #GPU ON LABEL
        self.gpu = QtWidgets.QLabel(MainWindow)
        self.gpu.setStyleSheet("QLabel::hover" "{ background-color : yellow; }")
        self.gpu.setGeometry(QtCore.QRect(170, 565, 321, 31))
        self.gpu.setMouseTracking(True)
        self.gpu.clear()
        self.gpu.setObjectName("GPU")
        self.gpu.setGraphicsEffect(self.opacityEffect2)

        self.gpu = DraggableLabel(self.gpu, "../images/gpu.png", 221,121, "GPU").resize(321, 31)
        
        
        #RAM STICKS ON LABELS
        self.ram1 = QtWidgets.QLabel(MainWindow)
        self.ram1.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow }")
        self.ram1.setGeometry(QtCore.QRect(560, 50, 20, 440))
        self.ram1.setMouseTracking(True)
        self.ram1.clear()
        self.ram1.setObjectName("RamStick1")
        self.ram1.setGraphicsEffect(self.opacityEffect3)
      
        self.ram2 = QtWidgets.QLabel(MainWindow)
        self.ram2.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow }")
        self.ram2.setGeometry(QtCore.QRect(589, 50, 20, 440))
        self.ram2.setMouseTracking(True)
        self.ram2.clear()
        self.ram2.setObjectName("RamStick2")
        self.ram2.setGraphicsEffect(self.opacityEffect4)
     
        self.ram3 = QtWidgets.QLabel(MainWindow)
        self.ram3.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow }")
        self.ram3.setGeometry(QtCore.QRect(618, 50, 20, 440))
        self.ram3.setMouseTracking(True)
        self.ram3.clear()
        self.ram3.setObjectName("RamStick3")
        self.ram3.setGraphicsEffect(self.opacityEffect5)

        self.ram4 = QtWidgets.QLabel(MainWindow)
        self.ram4.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow }")
        self.ram4.setGeometry(QtCore.QRect(647, 50, 20, 440))
        self.ram4.setMouseTracking(True)
        self.ram4.clear()
        self.ram4.setObjectName("RamStick4")
        self.ram4.setGraphicsEffect(self.opacityEffect6)

        
        self.ram1 = DraggableLabel(self.ram1, "../images/ram stick.jpg", 221, 51, "RAM").resize(20, 440)
        self.ram2 = DraggableLabel(self.ram2, "../images/ram stick.jpg", 221, 51, "RAM").resize(20, 440)
        self.ram3 = DraggableLabel(self.ram3, "../images/ram stick.jpg", 221, 51, "RAM").resize(20, 440)
        self.ram4 = DraggableLabel(self.ram4, "../images/ram stick.jpg", 221, 51, "RAM").resize(20, 440)
        
        
        #label 8 is m.2
        self.m2 = QtWidgets.QLabel(MainWindow)
        self.m2.setStyleSheet("QLabel::hover"
                             "{ background-color : yellow }")
        self.m2.setGeometry(QtCore.QRect(460, 830, 251, 71))
        self.m2.clear()
        self.m2.setObjectName("M.2 SSD")
        self.m2.setGraphicsEffect(self.opacityEffect7)

        self.m2 = DraggableLabel(self.m2,  "../images/m.2_ssd.jpg", 221, 61, "SSD").resize(251, 71)

        self.retranslateMotherboard(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self.centralwidget)
    
    def retranslateMotherboard(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.centralwidget.setWindowTitle(_translate("MotherBoard", "MotherBoard"))

    def retranslateHardware(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cpu_label.setText(_translate("MainWindow", "CPU"))
        self.cpu_cooler_label.setText(_translate("MainWindow", "CPU Cooler"))
        self.hardware_list_label.setText(_translate("MainWindow", "Hardware Components"))
        self.hardware_list_label.adjustSize()
        self.gpu_label.setText(_translate("MainWindow", "GPU"))
        self.ram_label.setText(_translate("MainWindow", "RAM Sticks"))
        self.ssd_label.setText(_translate("MainWindow", "M.2 SSD"))

        self.hover_actual_description_label.setText(_translate("MainWindow", "Hover over a part to see description!"))
        self.hover_description_label.setText(_translate("MainWindow", "Part Description"))

    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MotherBoard()
    ui.setupHardware(MainWindow)
    ui.setupMotherboard(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())