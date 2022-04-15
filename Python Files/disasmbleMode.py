from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QImage

import PartAnalyzer as Analyzer
import math
from hover import hoverExit, hoverEnter

# For part analyzer
class Part(QLabel):
    def __init__(self, MainWindow, name, x, y, width, height):
        QLabel.__init__(self, MainWindow)
        self.opacityEffect0 = QGraphicsOpacityEffect()
        self.opacityEffect0.setOpacity(0.3)
        self.name = name
        self.setStyleSheet("QLabel::hover" "{ background-color : yellow; }")
        self.setGeometry(QtCore.QRect(x, y, width, height))
        self.setMouseTracking(True)
        self.clear()
        self.setObjectName(self.name)
        self.setGraphicsEffect(self.opacityEffect0)
    
    def mousePressEvent(self, event):
        if(event.button() == Qt.RightButton):
            index = 0
            for names in Analyzer.partNames:
                if(self.name == names and index < len(Analyzer.partNames)):
                    Ui_MotherBoard.openPartAnalyzer(self, Analyzer.partNames[index],Analyzer.descriptions[index], Analyzer.descriptions2[index],
                                                    Analyzer.partImages[index][0], Analyzer.partImages[index][1],
                                                    Analyzer.partCoordinates[index][0], Analyzer.partCoordinates[index][1], Analyzer.partCoordinates[index][2], Analyzer.partCoordinates[index][3])
                index += 1

# Dragging
class DragLabel(QLabel):
    #self.gpu = DragLabel(self.gpu,"../images/GPU_topview.jpg" , "../images/gpu.png", 321, 31, 221,121, "GPU")
    def __init__(self,parent, top_image, mv_image, top_width, top_height, mv_width, mv_height, name):
        super(QLabel,self).__init__(parent)
        self.setPixmap(QPixmap(top_image).scaled(top_width,top_height))
        if mv_image != None:
            self.image = QPixmap(mv_image).scaled(mv_width,mv_height)
        self.name = name
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        if self.pixmap() == None:
            return
        drag = QDrag(self)
        
        mimedata = QMimeData()
        mimedata.setText(self.text())
        mimedata.setImageData(self.image.toImage())

        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()

        drag.setPixmap(self.image)
        drag.setHotSpot(QPoint(self.x()+math.floor(self.width()/2),self.y()+30))
        drag.exec_(Qt.MoveAction)
        self.hide()
        
class DropLabel(QLabel):
    def __init__(self, label, parent, image, width, height, effect):
        super(QLabel,self).__init__(parent)
        self.setAcceptDrops(True)
        self.setPixmap(QPixmap(image).scaled(width, height))
        self.effect = effect
    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            event.acceptProposedAction()
        
    
    def dropEvent(self,event):
        pos = event.pos()
        
        if event.mimeData().hasImage():
            self.effect.setOpacity(1)
            event.acceptProposedAction()
            

class Ui_MotherBoard(object):
    def openPartAnalyzer(self, name, description, description2,  image, image2, width, height, width2, height2):
            self.partView = QtWidgets.QMainWindow()
            self.partView.setWindowTitle("Part Analyzer")
            self.ui2 = Analyzer.Ui_PartAnalyzer()
            self.ui2.setupUi(self.partView, name, description, description2, image, image2, width, height, width2, height2)
            self.partView.show()

    def hover_events(self, MainWindow):
        self.cpu.leaveEvent = lambda e: hoverExit("CPU", self.hover_actual_description_label)
        self.cpu.enterEvent = lambda e: hoverEnter("CPU", self.hover_actual_description_label)
        self.gpu1.leaveEvent = lambda e: hoverExit("GPU", self.hover_actual_description_label)
        self.gpu1.enterEvent = lambda e: hoverEnter("GPU", self.hover_actual_description_label)
        self.pcie_x16.leaveEvent = lambda e: hoverExit("PCIe_x16", self.hover_actual_description_label)
        self.pcie_x16.enterEvent = lambda e: hoverEnter("PCIe_x16", self.hover_actual_description_label)
        self.ram1.leaveEvent = lambda e: hoverExit("RAM", self.hover_actual_description_label)
        self.ram1.enterEvent = lambda e: hoverEnter("RAM", self.hover_actual_description_label)
        self.ram2.leaveEvent = lambda e: hoverExit("RAM", self.hover_actual_description_label)
        self.ram2.enterEvent = lambda e: hoverEnter("RAM", self.hover_actual_description_label)
        self.ram3.leaveEvent = lambda e: hoverExit("RAM", self.hover_actual_description_label)
        self.ram3.enterEvent = lambda e: hoverEnter("RAM", self.hover_actual_description_label)
        self.ram4.leaveEvent = lambda e: hoverExit("RAM", self.hover_actual_description_label)
        self.ram4.enterEvent = lambda e: hoverEnter("RAM", self.hover_actual_description_label)
        self.cpu_cooler_img.leaveEvent = lambda e: hoverExit("CPU-COOLER", self.hover_actual_description_label)
        self.cpu_cooler_img.enterEvent = lambda e: hoverEnter("CPU-COOLER", self.hover_actual_description_label)
        self.m2.leaveEvent = lambda e: hoverExit("SSD", self.hover_actual_description_label)
        self.m2.enterEvent = lambda e: hoverEnter("SSD", self.hover_actual_description_label)

        self.cpuCable.leaveEvent = lambda e: hoverExit("CPU-CABLE", self.hover_actual_description_label)
        self.cpuCable.enterEvent = lambda e: hoverEnter("CPU-CABLE", self.hover_actual_description_label)
        self.antenna_port.leaveEvent = lambda e: hoverExit("ANTENNA", self.hover_actual_description_label)
        self.antenna_port.enterEvent = lambda e: hoverEnter("ANTENNA", self.hover_actual_description_label)
        self.hdmi_port.leaveEvent = lambda e: hoverExit("HDMI", self.hover_actual_description_label)
        self.hdmi_port.enterEvent = lambda e: hoverEnter("HDMI", self.hover_actual_description_label)
        self.usb32_ps2_port.leaveEvent = lambda e: hoverExit("USB3.2_PS2", self.hover_actual_description_label)
        self.usb32_ps2_port.enterEvent = lambda e: hoverEnter("USB3.2_PS2", self.hover_actual_description_label)
        self.usb32_typeA_typeC_port.leaveEvent = lambda e: hoverExit("USB3.2_TypeA_TypeC", self.hover_actual_description_label)
        self.usb32_typeA_typeC_port.enterEvent = lambda e: hoverEnter("USB3.2_TypeA_TypeC", self.hover_actual_description_label)
        self.lan_usb20_port.leaveEvent = lambda e: hoverExit("LAN_USB2.0", self.hover_actual_description_label)
        self.lan_usb20_port.enterEvent = lambda e: hoverEnter("LAN_USB2.0", self.hover_actual_description_label)
        self.audio_jacks_port.leaveEvent = lambda e: hoverExit("AUDIO-JACKS", self.hover_actual_description_label)
        self.audio_jacks_port.enterEvent = lambda e: hoverEnter("AUDIO-JACKS", self.hover_actual_description_label)

        self.pcie1.leaveEvent = lambda e: hoverExit("PCIe_x1", self.hover_actual_description_label)
        self.pcie1.enterEvent = lambda e: hoverEnter("PCIe_x1", self.hover_actual_description_label)
        self.pcie2.leaveEvent = lambda e: hoverExit("PCIe_x1", self.hover_actual_description_label)
        self.pcie2.enterEvent = lambda e: hoverEnter("PCIe_x1", self.hover_actual_description_label)
        self.pcie3.leaveEvent = lambda e: hoverExit("PCIe_x1", self.hover_actual_description_label)
        self.pcie3.enterEvent = lambda e: hoverEnter("PCIe_x1", self.hover_actual_description_label)

        self.cmos.leaveEvent = lambda e: hoverExit("CMOS", self.hover_actual_description_label)
        self.cmos.enterEvent = lambda e: hoverEnter("CMOS", self.hover_actual_description_label)

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
        
        #self.testDropLabel = QtWidgets.QLabel(self.centralwidget)
        #self.testDropLabel.setGeometry(800, 800, 30,30)
        #self.testDropLabel = DropLabel("Droplabel", self.testDropLabel)
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

        #labels

        self.cpu_label.setFont(font)
        self.cpu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_label.setObjectName("cpu_label")
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
        self.gpu_label = QtWidgets.QLabel(self.centralwidget)
        self.gpu_label.setGeometry(QtCore.QRect(1130, 210, 151, 31))
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
        
    
        #image
        self.cpu_img = QtWidgets.QLabel(self.centralwidget)
        self.cpu_img.setGeometry(QtCore.QRect(1070, 110, 91, 81))
        self.cpu_img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cpu_img.setText("")
        self.cpu_img.setPixmap(QtGui.QPixmap("../images/i7_cpu.jpg"))
        self.cpu_img.setScaledContents(True)
        self.cpu_img.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_img.setObjectName("cpu_img")
        self.cpu_img.effect = QGraphicsOpacityEffect()
        self.cpu_img.effect.setOpacity(0.3)
        self.cpu_img.setGraphicsEffect(self.cpu_img.effect)
        self.cpu_img = DropLabel("CPU", self.cpu_img, "../images/i7_cpu.jpg", 91, 81, self.cpu_img.effect)
        

        self.cpu_cooler_img = QtWidgets.QLabel(self.centralwidget)
        self.cpu_cooler_img.setGeometry(QtCore.QRect(1240, 100, 111, 111))
        self.cpu_cooler_img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cpu_cooler_img.setText("")
        self.cpu_cooler_img.setPixmap(QtGui.QPixmap("../images/cpu_cooler.png"))
        self.cpu_cooler_img.setScaledContents(True)
        self.cpu_cooler_img.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_cooler_img.setObjectName("cpu_cooler_img")
        self.cpu_cooler_img.setGraphicsEffect(self.opacityEffect1)
        
        self.gpu_img = QtWidgets.QLabel(self.centralwidget)
        self.gpu_img.setGeometry(QtCore.QRect(1090, 250, 221, 121))
        self.gpu_img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gpu_img.setText("")
        self.gpu_img.setPixmap(QtGui.QPixmap("../images/gpu.png"))
        self.gpu_img.setScaledContents(True)
        self.gpu_img.setAlignment(QtCore.Qt.AlignCenter)
        self.gpu_img.setObjectName("gpu_img")
        self.gpu_img.effect = QGraphicsOpacityEffect()
        self.gpu_img.effect.setOpacity(0.3)
        self.gpu_img.setGraphicsEffect(self.gpu_img.effect)
        self.gpu_img = DropLabel("GPU", self.gpu_img, "../images/gpu.png", 221, 121, self.gpu_img.effect)

        
        self.ssd_img = QtWidgets.QLabel(self.centralwidget)
        self.ssd_img.setGeometry(QtCore.QRect(1090, 560, 251, 61))
        self.ssd_img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ssd_img.setText("")
        self.ssd_img.setPixmap(QtGui.QPixmap("../images/m.2_ssd.jpg"))
        self.ssd_img.setScaledContents(True)
        self.ssd_img.setAlignment(QtCore.Qt.AlignCenter)
        self.ssd_img.setObjectName("ssd_img")
        self.ssd_img.effect = QGraphicsOpacityEffect()
        self.ssd_img.effect.setOpacity(0.3)
        self.ssd_img.setGraphicsEffect(self.ssd_img.effect)
        self.ssd_img = DropLabel("SSD", self.ssd_img, "../images/m.2_ssd.jpg", 251, 61, self.ssd_img.effect)
        
        self.ram_img1 = QtWidgets.QLabel(self.centralwidget)
        self.ram_img1.setGeometry(QtCore.QRect(1100, 410, 221, 51))
        self.ram_img1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ram_img1.setText("")
        self.ram_img1.setPixmap(QtGui.QPixmap("../images/ram stick.jpg"))
        self.ram_img1.setScaledContents(True)
        self.ram_img1.setAlignment(QtCore.Qt.AlignCenter)
        self.ram_img1.setObjectName("ram_img1")
        self.ram_img1.effect = QGraphicsOpacityEffect()
        self.ram_img1.effect.setOpacity(0.3)
        self.ram_img1.setGraphicsEffect(self.ram_img1.effect)
        self.ram_img1 = DropLabel("RAM", self.ram_img1, "../images/ram stick.jpg", 221, 51, self.ram_img1.effect)
        
        self.ram_img2 = QtWidgets.QLabel(self.centralwidget)
        self.ram_img2.setGeometry(QtCore.QRect(1100, 470, 221, 51))
        self.ram_img2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ram_img2.setText("")
        self.ram_img2.setPixmap(QtGui.QPixmap("../images/ram stick.jpg"))
        self.ram_img2.setScaledContents(True)
        self.ram_img2.setAlignment(QtCore.Qt.AlignCenter)
        self.ram_img2.setObjectName("ram_img2")
        self.ram_img2.effect = QGraphicsOpacityEffect()
        self.ram_img2.effect.setOpacity(0.3)
        self.ram_img2.setGraphicsEffect(self.ram_img2.effect)
        self.ram_img2 = DropLabel("RAM", self.ram_img2, "../images/ram stick.jpg", 221, 51, self.ram_img2.effect)   



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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

        #CPU on motherboard
        self.cpu = QtWidgets.QLabel(MainWindow)
        self.cpu.setStyleSheet("QLabel::hover" "{ background-color : yellow; }")
        self.cpu.setGeometry(QtCore.QRect(355, 230, 91, 81))
        self.cpu.setMouseTracking(True)
        self.cpu.clear()
        self.cpu.setObjectName("CPU")        
        self.cpu = DragLabel(self.cpu, "../images/i7_cpu.jpg", "../images/i7_cpu.jpg", 91, 81, 91, 81, "CPU")

        #GPU on motherboard
        self.gpu1 = QtWidgets.QLabel(MainWindow)
        self.gpu1.setStyleSheet("QLabel::hover" "{ background-color : yellow; }")
        self.gpu1.setGeometry(QtCore.QRect(170, 565, 321, 31))
        self.gpu1.setMouseTracking(True)
        self.gpu1.clear()
        self.gpu1.setObjectName("GPU")
        self.gpu1 = DragLabel(self.gpu1,"../images/GPU_topview.jpg" , "../images/gpu.png", 321, 31, 221,121, "GPU")

        #PCIe x16 on motherboard (no image and no draglabel)
        self.pcie_x16 = Part(MainWindow, "PCIe_x16", 170, 760, 321, 31)
        
        #RAM STICKS on motherboard
        self.ram1 = QtWidgets.QLabel(MainWindow)
        self.ram1.setStyleSheet("QLabel::hover"
                                "{ background-color : yellow }")
        self.ram1.setGeometry(QtCore.QRect(560, 50, 20, 440))
        self.ram1.setMouseTracking(True)
        self.ram1.clear()
        self.ram1.setObjectName("RamStick1")
      
        self.ram2 = QtWidgets.QLabel(MainWindow)
        self.ram2.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow }")
        self.ram2.setGeometry(QtCore.QRect(589, 50, 20, 440))
        self.ram2.setMouseTracking(True)
        self.ram2.clear()
        self.ram2.setObjectName("RamStick2")
     
        self.ram3 = QtWidgets.QLabel(MainWindow)
        self.ram3.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow }")
        self.ram3.setGeometry(QtCore.QRect(618, 50, 20, 440))
        self.ram3.setMouseTracking(True)
        self.ram3.clear()
        self.ram3.setObjectName("RamStick3")

        self.ram4 = QtWidgets.QLabel(MainWindow)
        self.ram4.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow }")
        self.ram4.setGeometry(QtCore.QRect(647, 50, 20, 440))
        self.ram4.setMouseTracking(True)
        self.ram4.clear()
        self.ram4.setObjectName("RamStick4")
        
        self.ram1 = DragLabel(self.ram1, "../images/ram_topview.jpg","../images/ram stick.jpg", 20, 440, 221, 51, "RAM")
        self.ram2 = DragLabel(self.ram2, "../images/ram_topview.jpg","../images/ram stick.jpg", 20, 440, 221, 51, "RAM")
        self.ram3 = DragLabel(self.ram3, "../images/ram_topview.jpg","../images/ram stick.jpg", 20, 440, 221, 51, "RAM")
        self.ram4 = DragLabel(self.ram4, "../images/ram_topview.jpg","../images/ram stick.jpg", 20, 440, 221, 51, "RAM")
        
        
        #SSD on motherboard
        self.m2 = QtWidgets.QLabel(MainWindow)
        self.m2.setStyleSheet("QLabel::hover"
                             "{ background-color : yellow }")
        self.m2.setGeometry(QtCore.QRect(460, 830, 251, 71))
        self.m2.clear()
        self.m2.setObjectName("M.2 SSD")
        self.m2 = DragLabel(self.m2, "../images/m.2_ssd.jpg", "../images/m.2_ssd.jpg", 251, 71, 221, 61, "SSD")

        #CPU cable on motherboard (no image and no dragLabel)
        self.cpuCable = Part(MainWindow, "CPU-CABLE", 170, 19, 50, 25)

        #Antenna port on motherboard (no image and no dragLabel)
        self.antenna_port = Part(MainWindow, "ANTENNA", 15, 10, 81, 51)

        #HDMI port on motherboard (no image and no dragLabel)
        self.hdmi_port = Part(MainWindow, "HDMI", 25, 70, 61, 51)

        #USB3.2 PS2 port on motherboard (no image and no dragLabel)
        self.usb32_ps2_port = Part(MainWindow, "USB3.2_PS2", 25, 210, 71, 51)

        #USB3.2 TypeA TypeC port on motherboard (no image and no dragLabel)
        self.usb32_typeA_typeC_port = Part(MainWindow, "USB3.2_TypeA_TypeC", 25, 320, 61, 45)

        #USB2.0 port on motherboard (no image and no dragLabel)
        self.lan_usb20_port = Part(MainWindow, "LAN_USB2.0", 25, 380, 81, 65)

        #Audio jack port on motherboard (no image and no dragLabel)
        self.audio_jacks_port = Part(MainWindow, "AUDIO-JACKS", 25, 450, 71, 45)

        #Three small PCIe x1 at y=500, 700, 890 (no image and no dragLabel)
        self.pcie1 = Part(MainWindow, "PCIe_x1", 170, 500, 80, 30)
        self.pcie2 = Part(MainWindow, "PCIe_x1", 170, 700, 80, 30)
        self.pcie3 = Part(MainWindow, "PCIe_x1", 170, 890, 80, 30)

        #CMOS battery on motherboard (no image and no dragLabel)
        self.cmos = Part(MainWindow, "CMOS", 430, 616, 60, 60)

        # call mouse hover events
        self.hover_events(MainWindow)

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

        self.hover_actual_description_label.setText(_translate("MainWindow", "Hover over a part to see description!         Right click to analyze a part!"))
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