# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hardware.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QImage
from PyQt5.QtCore import *
from hover import hoverExit, hoverEnter
import PartAnalyzer as Analyzer
import mainMenu

# Dragging
class DraggableLabel(QLabel):
    def __init__(self,parent,image, name):
        super(QLabel,self).__init__(parent)
        self.setPixmap(QPixmap(image))
        self.setScaledContents(True)
        self.name = name
        self.show()


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
        if(event.button() == Qt.RightButton):
            index = 0
            for names in Analyzer.partNames:
                if(self.name == names and index < len(Analyzer.partNames)):
                    Ui_MotherBoard.openPartAnalyzer(self, Analyzer.partNames[index],Analyzer.descriptions[index], Analyzer.descriptions2[index],
                                                    Analyzer.partImages[index][0], Analyzer.partImages[index][1],
                                                    Analyzer.partCoordinates[index][0], Analyzer.partCoordinates[index][1], Analyzer.partCoordinates[index][2], Analyzer.partCoordinates[index][3])
                index += 1

    def mouseMoveEvent(self, event):
        #if(self.name == PartAnalyzer.partNames[5] or self.name == PartAnalyzer.partNames[6] or self.name == PartAnalyzer.partNames[7] or self.name == PartAnalyzer.partNames[8] or self.name == PartAnalyzer.partNames[9]:
        for names in Analyzer.partNames[5:]:
            if(self.name == names):
                return
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        mimedata.setImageData(self.pixmap().toImage())

        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
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
    def openPartAnalyzer(self, name, description, description2,  image, image2, width, height, width2, height2):
            self.partView = QtWidgets.QMainWindow()
            self.partView.setWindowTitle("Part Analyzer")
            self.ui2 = Analyzer.Ui_PartAnalyzer()
            self.ui2.setupUi(self.partView, name, description, description2, image, image2, width, height, width2, height2)
            self.partView.show()

    def hover_events(self, MainWindow):
        # PC COMPONENTS hover events
        self.cpu_img.leaveEvent = lambda e: hoverExit("CPU", self.hover_actual_description_label)
        self.cpu_img.enterEvent = lambda e: hoverEnter("CPU", self.hover_actual_description_label)
        self.gpu_img.leaveEvent = lambda e: hoverExit("GPU", self.hover_actual_description_label)
        self.gpu_img.enterEvent = lambda e: hoverEnter("GPU", self.hover_actual_description_label)
        self.ram_img1.leaveEvent = lambda e: hoverExit("RAM", self.hover_actual_description_label)
        self.ram_img1.enterEvent = lambda e: hoverEnter("RAM", self.hover_actual_description_label)
        self.ram_img2.leaveEvent = lambda e: hoverExit("RAM", self.hover_actual_description_label)
        self.ram_img2.enterEvent = lambda e: hoverEnter("RAM", self.hover_actual_description_label)
        self.cpu_cooler_img.leaveEvent = lambda e: hoverExit("CPU-COOLER", self.hover_actual_description_label)
        self.cpu_cooler_img.enterEvent = lambda e: hoverEnter("CPU-COOLER", self.hover_actual_description_label)
        self.ssd_img.leaveEvent = lambda e: hoverExit("SSD", self.hover_actual_description_label)
        self.ssd_img.enterEvent = lambda e: hoverEnter("SSD", self.hover_actual_description_label)

        # IO Ports Hover Events
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
        self.hover_description_label.setGeometry(QtCore.QRect(1130, 650, 171, 31))

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
        #self.hover_description_label.adjustSize()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateHardware(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.cpu_imgD = (DraggableLabel(self.cpu_img, "../images/i7_cpu.jpg", "CPU").resize(91, 81))
        self.gpu_imgD = (DraggableLabel(self.gpu_img, "../images/gpu.png", "GPU").resize(221, 121))
        self.cpu_cooler_imgD = (DraggableLabel(self.cpu_cooler_img, "../images/cpu_cooler.png", "CPU-COOLER").resize(111, 111))
        self.ram_img1D = (DraggableLabel(self.ram_img1, "../images/ram stick.jpg", "RAM").resize(221, 51))
        self.ram_img2D = (DraggableLabel(self.ram_img2, "../images/ram stick.jpg", "RAM").resize(221, 51))
        self.ssd_imgD = (DraggableLabel(self.ssd_img, "../images/m.2_ssd.jpg", "SSD").resize(221, 61))
        
    def io_ports(self, MainWindow):
        # IO PORTS INVISIBLE IMAGES
        self.antenna_port = QtWidgets.QLabel(MainWindow)
        self.antenna_port.setStyleSheet("QLabel::hover" "{ background-color : yellow; }")
        self.antenna_port.setGeometry(QtCore.QRect(15, 10, 81, 51))
        self.antenna_port.setMouseTracking(True)
        self.antenna_port.clear()
        self.antenna_port.setObjectName("ANTENNA")
        self.antenna_port = DraggableLabel(self.antenna_port, "../images/clear_image", "ANTENNA")

        self.hdmi_port = QtWidgets.QLabel(MainWindow)
        self.hdmi_port.setStyleSheet("QLabel::hover" "{ background-color : yellow; }")
        self.hdmi_port.setGeometry(QtCore.QRect(25, 70, 61, 51))
        self.hdmi_port.setMouseTracking(True)
        self.hdmi_port.clear()
        self.hdmi_port.setObjectName("HDMI")
        self.hdmi_port = DraggableLabel(self.hdmi_port, "../images/clear_image", "HDMI")

        self.usb32_ps2_port = QtWidgets.QLabel(MainWindow)
        self.usb32_ps2_port.setStyleSheet("QLabel::hover" "{ background-color : yellow; }")
        self.usb32_ps2_port.setGeometry(QtCore.QRect(25, 210, 71, 51))
        self.usb32_ps2_port.setMouseTracking(True)
        self.usb32_ps2_port.clear()
        self.usb32_ps2_port.setObjectName("USB3.2_PS2")
        self.usb32_ps2_port = DraggableLabel(self.usb32_ps2_port, "../images/clear_image", "USB3.2_PS2")

        self.usb32_typeA_typeC_port = QtWidgets.QLabel(MainWindow)
        self.usb32_typeA_typeC_port.setStyleSheet("QLabel::hover" "{ background-color : yellow; }")
        self.usb32_typeA_typeC_port.setGeometry(QtCore.QRect(25, 320, 61, 45))
        self.usb32_typeA_typeC_port.setMouseTracking(True)
        self.usb32_typeA_typeC_port.clear()
        self.usb32_typeA_typeC_port.setObjectName("USB3.2_TypeA_TypeC")
        self.usb32_typeA_typeC_port = DraggableLabel(self.usb32_typeA_typeC_port, "../images/clear_image", "USB3.2_TypeA_TypeC")

        self.lan_usb20_port = QtWidgets.QLabel(MainWindow)
        self.lan_usb20_port.setStyleSheet("QLabel::hover" "{ background-color : yellow; }")
        self.lan_usb20_port.setGeometry(QtCore.QRect(25, 380, 81, 65))
        self.lan_usb20_port.setMouseTracking(True)
        self.lan_usb20_port.clear()
        self.lan_usb20_port.setObjectName("LAN_USB2.0")
        self.lan_usb20_port = DraggableLabel(self.lan_usb20_port, "../images/clear_image", "LAN_USB2.0")

        self.audio_jacks_port = QtWidgets.QLabel(MainWindow)
        self.audio_jacks_port.setStyleSheet("QLabel::hover" "{ background-color : yellow; }")
        self.audio_jacks_port.setGeometry(QtCore.QRect(25, 450, 71, 45))
        self.audio_jacks_port.setMouseTracking(True)
        self.audio_jacks_port.clear()
        self.audio_jacks_port.setObjectName("AUDIO-JACKS")
        self.audio_jacks_port = DraggableLabel(self.audio_jacks_port, "../images/clear_image", "AUDIO-JACKS")
        

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

        # call io ports
        self.io_ports(MainWindow)

        # call hover events
        self.hover_events(MainWindow)
        self.motherBoardD = (DraggableLabel(self.motherBoard, "../images/IntelMotherBoard.jpg", "MotherBoard"))

        #Opacity effect doesn't work with multiple labels 
        #Also tried setting opacity 1 to 0 but it doesnt work
        #Forced to initialize new opacities w/ same values                                      

        self.opacityEffect0 = QGraphicsOpacityEffect()#cpu
        self.opacityEffect0.setOpacity(0.3)
        self.opacityEffect1 = QGraphicsOpacityEffect()#cpu cable
        self.opacityEffect1.setOpacity(0.3)
        self.opacityEffect2 = QGraphicsOpacityEffect()#pciex16
        self.opacityEffect2.setOpacity(0.3)
        self.opacityEffect2p0 = QGraphicsOpacityEffect()#pciex16
        self.opacityEffect2p0.setOpacity(0.3)
        self.opacityEffect3 = QGraphicsOpacityEffect()#ram
        self.opacityEffect3.setOpacity(0.3)
        self.opacityEffect4 = QGraphicsOpacityEffect()#--
        self.opacityEffect4.setOpacity(0.3)
        self.opacityEffect5 = QGraphicsOpacityEffect()#--
        self.opacityEffect5.setOpacity(0.3)
        self.opacityEffect6 = QGraphicsOpacityEffect()#ram
        self.opacityEffect6.setOpacity(0.3)
        self.opacityEffect7 = QGraphicsOpacityEffect()#ssd
        self.opacityEffect7.setOpacity(0.3)
        self.opacityEffect8 = QGraphicsOpacityEffect()#pcie x1
        self.opacityEffect8.setOpacity(0.3)
        self.opacityEffect8p0 = QGraphicsOpacityEffect()#pcie x1
        self.opacityEffect8p0.setOpacity(0.3)
        self.opacityEffect8p1 = QGraphicsOpacityEffect()
        self.opacityEffect8p1.setOpacity(0.3)
        self.opacityEffect8p2 = QGraphicsOpacityEffect()
        self.opacityEffect8p2.setOpacity(0.3)
        self.opacityEffect8p3 = QGraphicsOpacityEffect()
        self.opacityEffect8p3.setOpacity(0.3)
        self.opacityEffect9 = QGraphicsOpacityEffect()#for cmos
        self.opacityEffect9.setOpacity(0.3)


        #CPU ON LABEL
        self.cpu = QtWidgets.QLabel(MainWindow)
        self.cpu.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow; }")
        self.cpu.setGeometry(QtCore.QRect(330, 170, 131, 211))
        self.cpu.setMouseTracking(True)
        self.cpu.clear()
        self.cpu.setObjectName("CPU") 
        self.cpu.setGraphicsEffect(self.opacityEffect0)

        self.cpuD = (DraggableLabel(self.cpu, "../images/clear_image.png", "CPU-SOCKET"))


        self.cpuCable = QtWidgets.QLabel(MainWindow)
        self.cpuCable.setStyleSheet("QLabel::hover"
                                   "{ background-color : yellow; }")
        self.cpuCable.setGeometry(QtCore.QRect(170, 19, 50, 25))
        self.cpuCable.setMouseTracking(True)
        self.cpuCable.clear()
        self.cpuCable.setObjectName("CPU-CABLE")
        self.cpuCable.setGraphicsEffect(self.opacityEffect1)

        self.cpuCableD = (DraggableLabel(self.cpuCable, "../images/clear_image.png", "CPU-CABLE"))

        #Small pcie 


        self.pcie = QtWidgets.QLabel(MainWindow)
        self.pcie.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow; }")
        self.pcie.setGeometry(QtCore.QRect(170, 500, 80, 30))
        self.pcie.setMouseTracking(True)
        self.pcie.clear()
        self.pcie.setObjectName("PCIe_x1")
        self.pcie.setGraphicsEffect(self.opacityEffect8)

        self.pcie1 = QtWidgets.QLabel(MainWindow)
        self.pcie1.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow; }")
        self.pcie1.setGeometry(QtCore.QRect(170, 700, 80, 30))
        self.pcie1.setMouseTracking(True)
        self.pcie1.clear()
        self.pcie1.setObjectName("PCIe_x1")
        self.pcie1.setGraphicsEffect(self.opacityEffect8p0)

        self.pcie2 = QtWidgets.QLabel(MainWindow)
        self.pcie2.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow; }")
        self.pcie2.setGeometry(QtCore.QRect(170, 890, 80, 30))
        self.pcie2.setMouseTracking(True)
        self.pcie2.clear()
        self.pcie2.setObjectName("PCIe_x1")
        self.pcie2.setGraphicsEffect(self.opacityEffect8p1)

        self.pcieD = (DraggableLabel(self.pcie, "../images/clear_image.png", "PCIe_x1"))
        self.pcie1D = (DraggableLabel(self.pcie1, "../images/clear_image.png", "PCIe_x1"))
        self.pcie2D = (DraggableLabel(self.pcie2, "../images/clear_image.png", "PCIe_x1"))

       

        #GPU ON LABEL
        self.gpu = QtWidgets.QLabel(MainWindow)
        self.gpu.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow; }")
        self.gpu.setGeometry(QtCore.QRect(170, 565, 321, 31))
        self.gpu.setMouseTracking(True)
        self.gpu.clear()
        self.gpu.setObjectName("GPU")
        self.gpu.setGraphicsEffect(self.opacityEffect2)

        self.gpu2 = QtWidgets.QLabel(MainWindow)
        self.gpu2.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow; }")
        self.gpu2.setGeometry(QtCore.QRect(170, 760, 321, 31))
        self.gpu2.setMouseTracking(True)
        self.gpu2.clear()
        self.gpu2.setObjectName("GPU")
        self.gpu2.setGraphicsEffect(self.opacityEffect2p0)

        self.gpuD = (DraggableLabel(self.gpu, "../images/clear_image.png", "PCIe_x16"))
        self.gpu2D = (DraggableLabel(self.gpu2, "../images/clear_image.png", "PCIe_x16"))
        
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

        self.ram1D = (DraggableLabel(self.ram1, "../images/clear_image.png", "RAM Slot"))
        self.ram2D = (DraggableLabel(self.ram2, "../images/clear_image.png", "RAM Slot"))
        self.ram3D = (DraggableLabel(self.ram3, "../images/clear_image.png", "RAM Slot"))
        self.ram4D = (DraggableLabel(self.ram4, "../images/clear_image.png", "RAM Slot"))


        #label 8 is m.2
        self.m2 = QtWidgets.QLabel(MainWindow)
        self.m2.setStyleSheet("QLabel::hover"
                             "{ background-color : yellow }")
        self.m2.setGeometry(QtCore.QRect(460, 830, 251, 71))
        self.m2.clear()
        self.m2.setObjectName("M.2 SSD")
        self.m2.setGraphicsEffect(self.opacityEffect7)

        self.m2D = (DraggableLabel(self.m2, "../images/clear_image.png", "M.2 Slot"))

        self.cmos = QtWidgets.QLabel(MainWindow)
        self.cmos.setPixmap(QtGui.QPixmap("../images/clear_image.png"))
        self.cmos.setGeometry(QtCore.QRect(430, 616, 60, 60))

        self.cmos.setStyleSheet("QLabel::hover"
                             "{ background-color : yellow;"
                             "  border-radius: 30px;}")
        self.cmos.clear()
        self.cmos.setObjectName("CMOS")
        self.cmos.setGraphicsEffect(self.opacityEffect9)
        self.cmosD = (DraggableLabel(self.cmos, "../images/clear_image.png", "CMOS"))



        self.retranslateMotherboard(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self.centralwidget)

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(1500, 25, 70, 31))
        self.startButton.setText("back")
        self.startButton.setObjectName("")
        self.startButton.clicked.connect(lambda : self.openMain())


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

        self.hover_actual_description_label.setText(_translate("MainWindow", "Hover over a part to see description!\nRight click to analyze a part!"))
        self.hover_description_label.setText(_translate("MainWindow", "Part Description"))
        self.hover_description_label.adjustSize()

    def openMain(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mainMenu.Ui_MainMenu()
        self.ui.setupUi(self.window)
        MainWindow.close()
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MotherBoard()
    ui.setupHardware(MainWindow)
    ui.setupMotherboard(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
