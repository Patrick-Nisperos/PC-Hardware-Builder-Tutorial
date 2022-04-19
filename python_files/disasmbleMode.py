from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QDrag, QPixmap, QColor

import PartAnalyzer as Analyzer
import mainMenu
from hover import hoverExit, hoverEnter
import Labels

class Ui_MotherBoard(object):
    def openPartAnalyzer(self, name, description, description2,  image, image2, width, height, width2, height2):
        self.PartView = QtWidgets.QMainWindow()
        self.PartView.setWindowTitle("Labels.Part Analyzer")
        self.ui2 = Analyzer.Ui_PartAnalyzer()
        self.ui2.setupUi(self.PartView, name, description, description2, image, image2, width, height, width2, height2)
        self.PartView.show()

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
        self.hardware_list_label = Labels.NameLabel(self.centralwidget, 16, True, 75, 1055, 20, 241, 41, "Hardware Components")
        
        self.cpu_label = Labels.NameLabel(self.centralwidget, 12, False, 75, 1040, 70, 151, 31, "CPU")
        
        self.cpu_cooler_label = Labels.NameLabel(self.centralwidget, 12, False, 75, 1220, 70, 151, 31, "CPU Cooler")
       
        self.gpu_label = Labels.NameLabel(self.centralwidget, 12, False, 75, 1130, 210, 151, 31, "GPU")
        
        self.ram_label = Labels.NameLabel(self.centralwidget, 12, False, 75, 1140, 370, 151, 31, "RAM Sticks")
        
        self.ssd_label = Labels.NameLabel(self.centralwidget, 12, False, 75, 1140, 530, 151, 31, "M.2 SSD")

        self.hover_description_label = Labels.NameLabel(self.centralwidget, 14, True, 75, 1092, 650, 250, 31, "Labels.Part Description")

        self.hover_actual_description_label = Labels.NameLabel(self.centralwidget, 10, False, 0, 1100, 680, 241, 200, "Hover over a Labels.Part to see description!         Right click to analyze a Labels.Part!")
        self.hover_actual_description_label.setWordWrap(True)
        self.hover_actual_description_label.setLayoutDirection(QtCore.Qt.LeftToRight)

        #images
        self.cpu_img = Labels.DropLabel(self.centralwidget, "../images/i7_cpu.jpg", 1070, 110, 91, 81, "CPU")
        
        self.cpu_cooler_img = Labels.DropLabel(self.centralwidget, "../images/cpu_cooler.png", 1240, 100, 111, 111, "CPU-COOLER")
        
        self.gpu_img = Labels.DropLabel(self.centralwidget, "../images/gpu.png", 1090, 250, 221, 121, "GPU")

        self.ssd_img = Labels.DropLabel(self.centralwidget, "../images/m.2_ssd.jpg", 1090, 560, 251, 61, "SSD")
        
        self.ram_img1 = Labels.DropLabel(self.centralwidget, "../images/ram stick.jpg", 1100, 410, 221, 51, "RAM")

        self.ram_img2 = Labels.DropLabel(self.centralwidget, "../images/ram stick.jpg", 1100, 470, 221, 51, "RAM")   

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
        self.cpu = Labels.DragLabel(MainWindow, "../images/i7_cpu.jpg", "../images/i7_cpu.jpg", 355, 230, 91, 81, 91, 81, "CPU")

        #CPU cooler on motherboard on top of CPU
        self.cpu_cooler = Labels.DragLabel(MainWindow, "../images/cpu_fan.jpeg", "../images/cpu_cooler.png", 250, 150, 300, 300, 111, 111, "CPU-COOLER")
        
        #GPU on motherboard
        self.gpu = Labels.DragLabel(MainWindow, "../images/GPU_topview.png" , "../images/gpu.png", 20, 525, 800, 91, 221,121, "GPU")

        #PCIe x16 on motherboard (no image and no Labels.DragLabel)
        self.pcie_x16 = Labels.Part(MainWindow, "PCIe_x16", 170, 760, 321, 31)
        
        #2 RAM sticks on motherboard       
        self.ram1 = Labels.DragLabel(MainWindow, "../images/ram_topview.jpg","../images/ram stick.jpg", 560, 50, 20, 440, 221, 51, "RAM")
        self.ram2 = Labels.DragLabel(MainWindow, "../images/ram_topview.jpg","../images/ram stick.jpg", 589, 50, 20, 440, 221, 51, "RAM")
        
        #2 RAM slots on motherboard (no image and no Labels.DragLabel)
        self.ram3 = Labels.Part(MainWindow, "RAM Slot", 618, 50, 20, 440)
        self.ram4 = Labels.Part(MainWindow, "RAM Slot", 647, 50, 20, 440)
        
        #SSD on motherboard
        self.m2 = Labels.DragLabel(MainWindow, "../images/m.2_ssd.jpg", "../images/m.2_ssd.jpg", 460, 830, 251, 71, 221, 61, "SSD")

        #CPU cable on motherboard (no image and no Labels.DragLabel)
        self.cpuCable = Labels.Part(MainWindow, "CPU-CABLE", 170, 19, 50, 25) 

        #Antenna port on motherboard (no image and no Labels.DragLabel)
        self.antenna_port = Labels.Part(MainWindow, "ANTENNA", 15, 10, 81, 51)

        #HDMI port on motherboard (no image and no Labels.DragLabel)
        self.hdmi_port = Labels.Part(MainWindow, "HDMI", 25, 70, 61, 51)

        #USB3.2 PS2 port on motherboard (no image and no Labels.DragLabel)
        self.usb32_ps2_port = Labels.Part(MainWindow, "USB3.2_PS2", 25, 210, 71, 51)

        #USB3.2 TypeA TypeC port on motherboard (no image and no Labels.DragLabel)
        self.usb32_typeA_typeC_port = Labels.Part(MainWindow, "USB3.2_TypeA_TypeC", 25, 320, 61, 45)

        #USB2.0 port on motherboard (no image and no Labels.DragLabel)
        self.lan_usb20_port = Labels.Part(MainWindow, "LAN_USB2.0", 25, 380, 81, 65)

        #Audio jack port on motherboard (no image and no Labels.DragLabel)
        self.audio_jacks_port = Labels.Part(MainWindow, "AUDIO-JACKS", 25, 450, 71, 45)

        #3 small PCIe x1 at y=500, 700, 890 (no image and no Labels.DragLabel)
        self.pcie1 = Labels.Part(MainWindow, "PCIe_x1", 170, 500, 80, 30)
        self.pcie2 = Labels.Part(MainWindow, "PCIe_x1", 170, 700, 80, 30)
        self.pcie3 = Labels.Part(MainWindow, "PCIe_x1", 170, 890, 80, 30)

        #CMOS battery on motherboard (no image and no Labels.DragLabel)
        self.cmos = Labels.Part(MainWindow, "CMOS", 430, 616, 60, 60)

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