from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QDrag, QPixmap, QColor

import PartAnalyzer as Analyzer
import mainMenu
from hover import hoverExit, hoverEnter

# on the motherboard
# Not dragable, No Image, Has Part Analyzer, Has Hover Description
class Part(QLabel):
    def __init__(self, MainWindow, name, x, y, width, height):
        QLabel.__init__(self, MainWindow)
        self.effect = QGraphicsOpacityEffect()
        self.effect.setOpacity(0.3)
        self.name = name
        self.setStyleSheet("QLabel::hover" "{ background-color : yellow; }")
        self.setGeometry(QtCore.QRect(x, y, width, height))
        self.setMouseTracking(True)
        self.clear()
        self.setObjectName(self.name)
        self.setGraphicsEffect(self.effect)
    
    def mousePressEvent(self, event):
        if(event.button() == Qt.RightButton):
            index = 0
            for names in Analyzer.partNames:
                if(self.name == names and index < len(Analyzer.partNames)):
                    Ui_MotherBoard.openPartAnalyzer(self, Analyzer.partNames[index],Analyzer.descriptions[index], Analyzer.descriptions2[index],
                                                    Analyzer.partImages[index][0], Analyzer.partImages[index][1],
                                                    Analyzer.partCoordinates[index][0], Analyzer.partCoordinates[index][1], Analyzer.partCoordinates[index][2], Analyzer.partCoordinates[index][3])
                index += 1

# on the motherboard
# dragable, Has Image, Has Part Analyzer, Has Hover Description
class DragLabel(QLabel):
    def __init__(self, MainWindow, top_image, mv_image, top_x, top_y, top_width, top_height, mv_width, mv_height, name):
        QLabel.__init__(self, MainWindow)
        self.name = name
        self.effect = QGraphicsColorizeEffect()
        self.effect.setColor(QColor("yellow"))
        self.effect.setStrength(0.13)
        self.setStyleSheet("QLabel::hover")
        self.setGeometry(QtCore.QRect(top_x, top_y, top_width, top_height))
        self.setMouseTracking(True)
        self.clear()
        self.setObjectName(self.name) 
        self.setPixmap(QPixmap(top_image).scaled(top_width,top_height))
        self.setGraphicsEffect(self.effect)
        self.image = QPixmap(mv_image).scaled(mv_width,mv_height)
        

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
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        if self.pixmap() == None:
            return
        
        mimedata = QMimeData()
        mimedata.setText(self.name)
        mimedata.setImageData(self.image.toImage())
        
        drag = QDrag(self)
        drag.setMimeData(mimedata)
        drag.setPixmap(self.image)
        drag.setHotSpot(QPoint(30,30))
        drag.exec_(Qt.MoveAction)

        
   
# on the right side Hardware Components
# dropable, Has Image, No Part Analyzer, No Hover Description
class DropLabel(QLabel):
    def __init__(self, centralwidget, image, x, y, width, height, name):
        QLabel.__init__(self, centralwidget)
        self.name = name
        self.setGeometry(QtCore.QRect(x, y, width, height))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.clear()
        self.setPixmap(QtGui.QPixmap(image))
        self.setScaledContents(True)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setObjectName(self.name)
        self.effect = QGraphicsOpacityEffect()
        self.effect.setOpacity(0.3)
        self.setGraphicsEffect(self.effect)
        self.setAcceptDrops(True)
        self.setPixmap(QPixmap(image).scaled(width, height))
        
       
    matched = pyqtSignal()

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            event.acceptProposedAction()
        
    def dropEvent(self,event):
        pos = event.pos()
        
        if event.mimeData().hasImage() and event.mimeData().text() == self.name:
            self.effect.setOpacity(1)
            event.acceptProposedAction()
            self.matched.emit()
            
            


# on the right side Hardware Components
# Titles and descriptions
class NameLabel(QLabel):
    def __init__(self, centralwidget, font_size, underline, weight, x, y, width, height, name):
        QLabel.__init__(self, centralwidget)
        self.setGeometry(QtCore.QRect(x, y, width, height))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(font_size)
        font.setWeight(weight)
        font.setStrikeOut(False)
        font.setUnderline(underline)
        self.setFont(font)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setText(name)

class Ui_MotherBoard(object):
    def openPartAnalyzer(self, name, description, description2,  image, image2, width, height, width2, height2):
        self.partView = QtWidgets.QMainWindow()
        self.partView.setWindowTitle("Part Analyzer")
        self.ui2 = Analyzer.Ui_PartAnalyzer()
        self.ui2.setupUi(self.partView, name, description, description2, image, image2, width, height, width2, height2)
        self.partView.show()

    def matched_events(self, MainWindow, centralwidget):
        self.cpu_img.matched.connect(lambda: self.cpu.hide())
        self.cpu_cooler_img.matched.connect(lambda: self.cpu_cooler.hide())
        self.gpu_img.matched.connect(lambda: self.gpu.hide())
        self.ram_img1.matched.connect(lambda: self.ram1.hide())
        self.ram_img2.matched.connect(lambda: self.ram2.hide())
        self.ssd_img.matched.connect(lambda: self.m2.hide())

    def hover_events(self, MainWindow):
        self.cpu.leaveEvent = lambda e: hoverExit("CPU", self.hover_actual_description_label)
        self.cpu.enterEvent = lambda e: hoverEnter("CPU", self.hover_actual_description_label)
        self.cpu_img.leaveEvent = lambda e: hoverExit("CPU", self.hover_actual_description_label)
        self.cpu_img.enterEvent = lambda e: hoverEnter("CPU", self.hover_actual_description_label)
        self.gpu.leaveEvent = lambda e: hoverExit("GPU", self.hover_actual_description_label)
        self.gpu.enterEvent = lambda e: hoverEnter("GPU", self.hover_actual_description_label)
        self.gpu_img.leaveEvent = lambda e: hoverExit("GPU", self.hover_actual_description_label)
        self.gpu_img.enterEvent = lambda e: hoverEnter("GPU", self.hover_actual_description_label)
        self.pcie_x16.leaveEvent = lambda e: hoverExit("PCIe_x16", self.hover_actual_description_label)
        self.pcie_x16.enterEvent = lambda e: hoverEnter("PCIe_x16", self.hover_actual_description_label)
        self.ram1.leaveEvent = lambda e: hoverExit("RAM", self.hover_actual_description_label)
        self.ram1.enterEvent = lambda e: hoverEnter("RAM", self.hover_actual_description_label)
        self.ram2.leaveEvent = lambda e: hoverExit("RAM", self.hover_actual_description_label)
        self.ram2.enterEvent = lambda e: hoverEnter("RAM", self.hover_actual_description_label)
        self.ram3.leaveEvent = lambda e: hoverExit("RAM Slot", self.hover_actual_description_label)
        self.ram3.enterEvent = lambda e: hoverEnter("RAM Slot", self.hover_actual_description_label)
        self.ram4.leaveEvent = lambda e: hoverExit("RAM Slot", self.hover_actual_description_label)
        self.ram4.enterEvent = lambda e: hoverEnter("RAM Slot", self.hover_actual_description_label)
        self.ram_img1.leaveEvent = lambda e: hoverExit("RAM", self.hover_actual_description_label)
        self.ram_img1.enterEvent = lambda e: hoverEnter("RAM", self.hover_actual_description_label)
        self.ram_img2.leaveEvent = lambda e: hoverExit("RAM", self.hover_actual_description_label)
        self.ram_img2.enterEvent = lambda e: hoverEnter("RAM", self.hover_actual_description_label)
        self.cpu_cooler.leaveEvent = lambda e: hoverExit("CPU-COOLER", self.hover_actual_description_label)
        self.cpu_cooler.enterEvent = lambda e: hoverEnter("CPU-COOLER", self.hover_actual_description_label)
        self.cpu_cooler_img.leaveEvent = lambda e: hoverExit("CPU-COOLER", self.hover_actual_description_label)
        self.cpu_cooler_img.enterEvent = lambda e: hoverEnter("CPU-COOLER", self.hover_actual_description_label)
        self.m2.leaveEvent = lambda e: hoverExit("SSD", self.hover_actual_description_label)
        self.m2.enterEvent = lambda e: hoverEnter("SSD", self.hover_actual_description_label)
        self.ssd_img.leaveEvent = lambda e: hoverExit("SSD", self.hover_actual_description_label)
        self.ssd_img.enterEvent = lambda e: hoverEnter("SSD", self.hover_actual_description_label)

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

        self.background = QtWidgets.QLabel(MainWindow)
        self.background.setGeometry(QtCore.QRect(0, 0, 1600, 986))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap('../images/disbackground.jpg'))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.background.lower()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #labels
        self.hardware_list_label = NameLabel(self.centralwidget, 16, True, 75, 1055, 20, 241, 41, "Hardware Components")
        
        self.cpu_label = NameLabel(self.centralwidget, 12, False, 75, 1040, 70, 151, 31, "CPU")
        
        self.cpu_cooler_label = NameLabel(self.centralwidget, 12, False, 75, 1220, 70, 151, 31, "CPU Cooler")
       
        self.gpu_label = NameLabel(self.centralwidget, 12, False, 75, 1130, 210, 151, 31, "GPU")
        
        self.ram_label = NameLabel(self.centralwidget, 12, False, 75, 1140, 370, 151, 31, "RAM Sticks")
        
        self.ssd_label = NameLabel(self.centralwidget, 12, False, 75, 1140, 530, 151, 31, "M.2 SSD")

        self.hover_description_label = NameLabel(self.centralwidget, 14, True, 75, 1092, 650, 250, 31, "Part Description")

        self.hover_actual_description_label = NameLabel(self.centralwidget, 10, False, 0, 1100, 680, 241, 200, "Hover over a part to see description!         Right click to analyze a part!")
        self.hover_actual_description_label.setWordWrap(True)
        self.hover_actual_description_label.setLayoutDirection(QtCore.Qt.LeftToRight)

        #images
        self.cpu_img = DropLabel(self.centralwidget, "../images/i7_cpu.jpg", 1070, 110, 91, 81, "CPU")
        
        self.cpu_cooler_img = DropLabel(self.centralwidget, "../images/cpu_cooler.png", 1240, 100, 111, 111, "CPU-COOLER")
        
        self.gpu_img = DropLabel(self.centralwidget, "../images/gpu.png", 1090, 250, 221, 121, "GPU")

        self.ssd_img = DropLabel(self.centralwidget, "../images/m.2_ssd.jpg", 1090, 560, 251, 61, "SSD")
        
        self.ram_img1 = DropLabel(self.centralwidget, "../images/ram stick.jpg", 1100, 410, 221, 51, "RAM")

        self.ram_img2 = DropLabel(self.centralwidget, "../images/ram stick.jpg", 1100, 470, 221, 51, "RAM")   

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
        self.cpu = DragLabel(MainWindow, "../images/i7_cpu.jpg", "../images/i7_cpu.jpg", 355, 230, 91, 81, 91, 81, "CPU")

        #CPU cooler on motherboard on top of CPU
        self.cpu_cooler = DragLabel(MainWindow, "../images/cpu_fan.jpeg", "../images/cpu_cooler.png", 250, 150, 300, 300, 111, 111, "CPU-COOLER")
        
        #GPU on motherboard
        self.gpu = DragLabel(MainWindow, "../images/GPU_topview.png" , "../images/gpu.png", 20, 525, 800, 91, 221,121, "GPU")

        #PCIe x16 on motherboard (no image and no draglabel)
        self.pcie_x16 = Part(MainWindow, "PCIe_x16", 170, 760, 321, 31)
        
        #2 RAM sticks on motherboard       
        self.ram1 = DragLabel(MainWindow, "../images/ram_topview.jpg","../images/ram stick.jpg", 560, 50, 20, 440, 221, 51, "RAM")
        self.ram2 = DragLabel(MainWindow, "../images/ram_topview.jpg","../images/ram stick.jpg", 589, 50, 20, 440, 221, 51, "RAM")
        
        #2 RAM slots on motherboard (no image and no draglabel)
        self.ram3 = Part(MainWindow, "RAM Slot", 618, 50, 20, 440)
        self.ram4 = Part(MainWindow, "RAM Slot", 647, 50, 20, 440)
        
        #SSD on motherboard
        self.m2 = DragLabel(MainWindow, "../images/m.2_ssd.jpg", "../images/m.2_ssd.jpg", 460, 830, 251, 71, 221, 61, "SSD")

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

        #3 small PCIe x1 at y=500, 700, 890 (no image and no dragLabel)
        self.pcie1 = Part(MainWindow, "PCIe_x1", 170, 500, 80, 30)
        self.pcie2 = Part(MainWindow, "PCIe_x1", 170, 700, 80, 30)
        self.pcie3 = Part(MainWindow, "PCIe_x1", 170, 890, 80, 30)

        #CMOS battery on motherboard (no image and no dragLabel)
        self.cmos = Part(MainWindow, "CMOS", 430, 616, 60, 60)

        # call mouse hover events
        self.hover_events(MainWindow)

        # call match events
        self.matched_events(MainWindow, self.centralwidget)
        
        self.retranslateMotherboard(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self.centralwidget)

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(1500, 25, 70, 31))
        self.startButton.setText("back")
        self.startButton.setObjectName("")

        self.startButton.clicked.connect(self.motherBoard.close)
        self.startButton.clicked.connect(MainWindow.close)
        self.startButton.clicked.connect(lambda : self.openMain())
    
    def retranslateMotherboard(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.centralwidget.setWindowTitle(_translate("MotherBoard", "MotherBoard"))

    def retranslateHardware(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hardware_list_label.adjustSize()

    def openMain(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mainMenu.Ui_MainMenu()
        self.ui.setupUi(self.window)
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