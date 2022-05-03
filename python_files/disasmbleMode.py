import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QDrag, QPixmap, QColor

import PartAnalyzer as Analyzer
import mainMenu
import hover
import Labels

class Ui_MotherBoard(object):
    def openPartAnalyzer(self, name, description, description2,  image, image2, width, height, width2, height2):
        self.PartView = QtWidgets.QMainWindow()
        self.PartView.setWindowTitle("Part Analyzer")
        self.ui2 = Analyzer.Ui_PartAnalyzer()
        self.ui2.setupUi(self.PartView, name, description, description2, image, image2, width, height, width2, height2)
        self.PartView.show()

    def matched_events(self, MainWindow, centralwidget):
        self.cpu_img.matched.connect(lambda: self.cpu.hide())
        self.cpu_cooler_img.matched.connect(lambda: self.cpu_cooler.hide())
        self.gpu_img.matched.connect(lambda: self.gpu.hide())
        self.ram_img1.matched.connect(lambda: self.ram2.hide())
        self.ram_img2.matched.connect(lambda: self.ram4.hide())
        self.ssd_img.matched.connect(lambda: self.m2.hide())

    def HoverEvent(self, drop):
        drop.leaveEvent = lambda e: hover.hoverExit(drop, self.hover_actual_description_label)
        drop.enterEvent = lambda e: hover.hoverEnter(drop, self.hover_actual_description_label)
    
    def hover_events(self, MainWindow):
        # PC COMPONENTS hover events
        self.HoverEvent(self.cpu_img)
        self.HoverEvent(self.cpu)
        self.HoverEvent(self.gpu)
        self.HoverEvent(self.gpu_img)
        self.HoverEvent(self.ram1)
        self.HoverEvent(self.ram2)
        self.HoverEvent(self.ram3)
        self.HoverEvent(self.ram4)
        self.HoverEvent(self.ram_img1)
        self.HoverEvent(self.ram_img2)
        self.HoverEvent(self.cpu_cooler)
        self.HoverEvent(self.cpu_cooler_img)
        self.HoverEvent(self.m2)
        self.HoverEvent(self.ssd_img)
        self.HoverEvent(self.antenna_port)
        self.HoverEvent(self.hdmi_port)
        self.HoverEvent(self.usb32_ps2_port)
        self.HoverEvent(self.usb32_typeA_typeC_port)
        self.HoverEvent(self.lan_usb20_port)
        self.HoverEvent(self.audio_jacks_port)
        self.HoverEvent(self.pcie1)
        self.HoverEvent(self.pcie2)
        self.HoverEvent(self.pcie3)
        self.HoverEvent(self.pcie_x16)
        self.HoverEvent(self.cmos)
        self.HoverEvent(self.USB32P0)
        self.HoverEvent(self.USB32P1)
        self.HoverEvent(self.frontPanelAudio)
        self.HoverEvent(self.thunderBolt)
        self.HoverEvent(self.sataConnector1)
        self.HoverEvent(self.sataConnector2)
        self.HoverEvent(self.sataConnector3)
        self.HoverEvent(self.CPUHeader)
        self.HoverEvent(self.addHeader1)
        self.HoverEvent(self.addHeader2)
        self.HoverEvent(self.RGBHeader3)
        self.HoverEvent(self.RGBHeader4)
        #self.HoverEvent(self.CHA)
        self.HoverEvent(self.ATXPower1)
        self.HoverEvent(self.ATXPower2)
        self.HoverEvent(self.ATXPower3)
        self.HoverEvent(self.ATXPower4)
        self.HoverEvent(self.cpuCable)
        self.HoverEvent(self.TPM)
        self.HoverEvent(self.SPI)
        self.HoverEvent(self.CHAFans0)
        self.HoverEvent(self.CHAFans)
        self.HoverEvent(self.caseHeader)
        self.HoverEvent(self.thunderBolt)



    def io_ports(self, MainWindow):
        # IO PORTS INVISIBLE IMAGES
        self.antenna_port = Labels.Part(MainWindow, "ANTENNA", 15, 10, 81, 51)
        self.hdmi_port = Labels.Part(MainWindow, "HDMI", 25, 70, 61, 51)
        self.usb32_ps2_port = Labels.Part(MainWindow, "USB3.2_PS2", 25, 210, 71, 51)
        self.usb32_typeA_typeC_port = Labels.Part(MainWindow, "USB3.2_TypeA_TypeC", 25, 320, 61, 45)
        self.lan_usb20_port = Labels.Part(MainWindow, "LAN_USB2.0", 25, 380, 81, 65)
        self.audio_jacks_port = Labels.Part(MainWindow, "AUDIO-JACKS", 25, 450, 71, 45)

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
        self.hardware_list_label = Labels.NameLabel(self.centralwidget, 16, True, 75, 1045, 20, 241, 41, "Hardware Components")
        
        self.cpu_label = Labels.NameLabel(self.centralwidget, 12, False, 75, 1040, 70, 151, 31, "CPU")
        
        self.cpu_cooler_label = Labels.NameLabel(self.centralwidget, 12, False, 75, 1220, 70, 151, 31, "CPU Cooler")
       
        self.gpu_label = Labels.NameLabel(self.centralwidget, 12, False, 75, 1130, 210, 151, 31, "GPU")
        
        self.ram_label = Labels.NameLabel(self.centralwidget, 12, False, 75, 1140, 370, 151, 31, "RAM Sticks")
        
        self.ssd_label = Labels.NameLabel(self.centralwidget, 12, False, 75, 1140, 530, 151, 31, "M.2 SSD")

        self.hover_description_label = Labels.NameLabel(self.centralwidget, 14, True, 75, 1092, 650, 250, 31, "Part Description")

        self.hover_actual_description_label = Labels.NameLabel(self.centralwidget, 10, False, 0, 1100, 680, 241, 200, "Hover over a Labels.Part to see description!\nRight click to analyze a Labels.Part!")
        self.hover_actual_description_label.setWordWrap(True)
        self.hover_actual_description_label.setLayoutDirection(QtCore.Qt.LeftToRight)

        #Drop labels on the right
        self.cpu_img = Labels.DropLabel(self.centralwidget, "../images/i7_cpu.jpg", 1070, 110, 91, 81, "CPU")
        
        self.cpu_cooler_img = Labels.DropLabel(self.centralwidget, "../images/cpu_cooler.png", 1240, 100, 111, 111, "CPU-COOLER")
        
        self.gpu_img = Labels.DropLabel(self.centralwidget, "../images/gpu.png", 1030, 190, 350, 250, "GPU")

        self.ssd_img = Labels.DropLabel(self.centralwidget, "../images/m.2_ssd.jpg", 1090, 560, 251, 61, "SSD")
        
        self.ram_img1 = Labels.DropLabel(self.centralwidget, "../images/ramstick.png", 1100, 410, 221, 51, "RAM")

        self.ram_img2 = Labels.DropLabel(self.centralwidget, "../images/ramstick.png", 1100, 470, 221, 51, "RAM")   

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
        self.motherBoard = QtWidgets.QLabel(MainWindow)
        self.motherBoard.setGeometry(QtCore.QRect(0, 0, 801, 971))
        self.motherBoard.setMouseTracking(True)
        self.motherBoard.setPixmap(QtGui.QPixmap("../images/IntelMotherBoard_disassemble_mode.png"))
        self.motherBoard.setObjectName("MotherBoard")



        #CPU on motherboard           
        self.cpu = Labels.DragLabel(MainWindow, "../images/i7_cpu.jpg", "../images/i7_cpu.jpg", 355, 230, 91, 81, 91, 81, "CPU")

        #GPU on motherboard
        self.gpu = Labels.DragLabel(MainWindow, "../images/3070side.png" , "../images/3070side.png",0, 425, 800, 300, 800,300, "GPU")

        #CPU cooler on motherboard on top of CPU
        self.cpu_cooler = Labels.DragLabel(MainWindow, "../images/cpu_fan.jpeg", "../images/cpu_cooler.png", 250, 150, 300, 300, 111, 111, "CPU-COOLER")
        
         #CPU cable on motherboard (no image and no Labels.DragLabel)
        self.cpuCable = Labels.Part(MainWindow, "CPU Power ATX", 170, 19, 80, 40) 

        #3 small PCIe x1 at y=500, 700, 890 (no image and no Labels.DragLabel)
        self.pcie1 = Labels.Part(MainWindow, "PCIe_x1", 170, 500, 80, 30)
        self.pcie2 = Labels.Part(MainWindow, "PCIe_x1", 170, 700, 80, 30)
        self.pcie3 = Labels.Part(MainWindow, "PCIe_x1", 170, 890, 80, 30)



        #PCIe x16 on motherboard (no image and no Labels.DragLabel)
        self.pcie_x16 = Labels.Part(MainWindow, "PCIe_x16", 170, 760, 321, 31)
        
        #2 RAM sticks on motherboard       
        self.ram4 = Labels.DragLabel(MainWindow, "../images/ram_topview.jpg","../images/ramstick.png", 647, 50, 20, 440, 221, 51, "RAM")
        self.ram2 = Labels.DragLabel(MainWindow, "../images/ram_topview.jpg","../images/ramstick.png", 589, 50, 20, 440, 221, 51, "RAM")
        
        #2 RAM slots on motherboard (no image and no Labels.DragLabel)
        self.ram3 = Labels.Part(MainWindow, "RAM Slot", 618, 50, 20, 440)
        self.ram1 = Labels.Part(MainWindow, "RAM Slot", 560, 50, 20, 440)
        
        #SSD on motherboard
        self.m2 = Labels.DragLabel(MainWindow, "../images/m.2_ssd.jpg", "../images/m.2_ssd.jpg", 460, 830, 251, 71, 221, 61, "SSD")

        #CMOS battery on motherboard (no image and no Labels.DragLabel)
        self.cmos = Labels.Part(MainWindow, "CMOS", 430, 616, 60, 60)

        #Newly added headers using Sloans Part Class
        #self.USB20 = Labels.Part(MainWindow, "USB20", 365, 935, 50, 25)
        self.USB32P0 = Labels.Part(MainWindow, "USB 3.2", 420, 930, 75, 25)
        self.USB32P1 = Labels.Part(MainWindow, "USB 3.2", 755, 430, 25, 75)
        self.frontPanelAudio = Labels.Part(MainWindow, "Front Panel Audio Header", 90, 935, 40,20)
        self.thunderBolt = Labels.Part(MainWindow, "Thunderbolt AIC connecter", 165, 845, 50, 30)
        self.sataConnector1 = Labels.Part(MainWindow, "Sata connecters", 580, 940, 50, 20)
        self.sataConnector2 = Labels.Part(MainWindow, "Sata connecters", 630, 940, 50, 20)
        self.sataConnector3 = Labels.Part(MainWindow, "Sata connecters", 750, 550, 40, 60)
        self.caseHeader = Labels.Part(MainWindow, "Case Header", 720, 940, 80, 20)

        self.addHeader1 = Labels.Part(MainWindow, "LED", 715, 18, 40, 20)
        self.addHeader2 = Labels.Part(MainWindow, "LED", 715, 40, 40, 20)
        self.RGBHeader3 = Labels.Part(MainWindow, "LED", 310, 940, 40, 20)
        self.RGBHeader4 = Labels.Part(MainWindow, "LED", 270, 940, 40, 20)
        
        self.CPUHeader = Labels.Part(MainWindow, "CPU Fan Header", 660, 20, 40, 20)
        self.ATXPower1 = Labels.Part(MainWindow, "ATX Power Connecter", 755, 250, 40, 80)
        self.ATXPower2 = Labels.Part(MainWindow, "ATX Power Connecter", 755, 190, 40, 50)
        self.ATXPower3 = Labels.Part(MainWindow, "ATX Power Connecter", 760, 145, 30, 30)
        self.ATXPower4 = Labels.Part(MainWindow, "ATX Power Connecter", 760, 100, 30, 30)
        self.CHAFans0 = Labels.Part(MainWindow, "CHA/Waterpump fan connector", 130, 50, 40, 20)
        self.CHAFans = Labels.Part(MainWindow, "CHA/Waterpump fan connector", 500, 940, 80, 20)
        self.TPM = Labels.Part(MainWindow, "TPM Header", 130, 940, 75, 20)
        self.SPI = Labels.Part(MainWindow, "Serial Port Header", 200, 940, 40, 20)


        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(1500, 25, 70, 31))
        self.startButton.setText("back")
        self.startButton.setObjectName("")

        self.startButton.clicked.connect(self.motherBoard.close)
        self.startButton.clicked.connect(MainWindow.close)
        self.startButton.clicked.connect(lambda : self.openMain())
        self.startButton.clicked.connect(lambda: self.ui.manage_song(self.startButton))


        self.audioButton = QtWidgets.QPushButton(MainWindow)
        self.audioButton.setGeometry(QtCore.QRect(1400, 25, 70, 31))
        self.audioButton.setText("Toggle Audio")
        self.audioButton.setObjectName("audioButton")

        # call io ports
        self.io_ports(MainWindow)


        # call mouse hover events
        self.hover_events(MainWindow)

        # call match events
        self.matched_events(MainWindow, self.centralwidget)
        
        self.retranslateMotherboard(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self.centralwidget)

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