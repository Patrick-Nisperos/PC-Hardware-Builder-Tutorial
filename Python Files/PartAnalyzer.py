# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PartaAnalyzer.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QImage
from PyQt5.QtCore import *

partNames = ["CPU", "GPU", "CPU-COOLER", "RAM", "SSD", "MotherBoard", "CMOS", "PCIe x1", "PCIe x16"]
io_partNames = ["ANTENNA", "HDMI", "USB3.2_PS2", "USB3.2_TypeA_TypeC", "LAN_USB2.0", "AUDIO-JACKS"]

#Index is CPU as 0, GPU, RAM, CPU-COOLER, SSD
descriptions = ["The CPU or Central Processing Unit is the brain of a computer,"
                " containing all the circuitry needed to process input,"
                " store data, and output results. The CPU is constantly following"
                " instructions of computer programs that tell it which data to process"
                " and how to process it.",

                "The GPU or Graphics processing unit, is a specialized"
                " processor originally designed to accelerate graphics rendering"
                " i.e. it displays the picture onto your screen",

                "The CPU cooler is a device designed to draw heat away from the system's"
                " CPU and other components in the enclosure.",

                "Ram or random-access memory is where the computer stores data that is needed for short term memory."
                " The ram holds all the data you are currently using.",

                "The SSD or Solid-State drive is a new generation of storage device"
                " used in computers. An SSD is much faster than a tradition mechanical"
                " hard disk as it uses flash-based memory instead of a physical disk",

                "The motherboard comes in many form factors and is one of the most essential piece of hardware in a computer. "
                "The motherboard comes in three main sizes that the user can choose from: ATX, micro-atx, and mini-ITX."
                "The user also has the option to choose a motherboard with an AMD or an intel socket in order to support the CPU. ",

                "Complementary metal-oxide-semiconductor (CMOS), is the term usually used to"
                " describe the small amount of memory on a computer motherboard that stores the BIOS settings.",

                "PCIe (peripheral component interconnect express) is an interface standard for "
                "connecting high-speed components. The types of PCIe slots come in different physical"
                "configurations: x1, x4, x8, x16, and x32."]

descriptions2 = ["The CPU acts as the brain of the computer and performs calculations, actions and runs the program"
                "The cpu fetches instructions that are represented as series of numbers from the ram."
                 "It then decodes the instructions and executes the instructions.",

                "The GPU or Graphics processing unit, specializes in rendering graphics in order to be displayed"
                "Basic processing of OS graphics can be handled by the CPU, but more intense graphical rendering of games or animation requires more horsepower.",

                "The CPU coolers job is to transfer heat away from the CPU in order for it to run as cool as possible. "
                "If the CPU gets too hot, it can lead to a system failure or crashes.",

                "The short-term memory allows fast access and transfer of data in order to handle active applications and task that the user is working on.",

                "The SSD is another component used for storage where the user is able to store much more data for long term use. "
                " SSDs are much slower than RAM, but gives a significant amount of storage and is able to retain that data even when the computer is off unlike RAM",

                "The motherboard allows the connections of various hardware components.",

                "The CMOS battery powers your computers BIOS firmware, which is responsible for booting up"
                " your computer and configuring data flow.",

                "The PCIe x1 slot is used to plug in low demanding PCIe expansion cards that do not have a very"
                "high throughput(transfer data) such as Network adapters, and Port Expansion Cards.",

                "The PCIe x16 slot is used to plug in high bandwidth like grapgics cards. However, these x16 slots"
                "could be used by any of the devices that would instead go in a smaller slot.="]

io_descriptions1 = ["Antenna Ports", "Hdmi", "PS/2 Ports and USB 3.2 ports",
                    "USB 3.2 Type-A port and USB 3.2 Type-C port", "LAN/Ethernet port and USB 2.0 port",
                    "Audio jacks port"]
io_descriptions2 = ["Gets signal", "Transfers data"]

class Ui_PartAnalyzer(object):
    def setupUi(self, PartAnalyzer, name, description, description2, image1, image2, width, height, width2, height2):
        PartAnalyzer.setObjectName("PartAnalyzer")
        PartAnalyzer.resize(800, 600)
        PartAnalyzer.setAutoFillBackground(False)
        self.background = QtWidgets.QLabel(PartAnalyzer)
        self.background.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap('../images/partback.png'))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.background.lower()

        self.centralwidget = QtWidgets.QWidget(PartAnalyzer)
        self.centralwidget.setObjectName("centralwidget")
        self.PartImage = QtWidgets.QLabel(self.centralwidget)
        self.PartImage.setGeometry(QtCore.QRect(50, 100, width, height))
        self.PartImage.clear()
        self.PartImage.setObjectName("PartImage")
        self.PartImage.setPixmap(QtGui.QPixmap(image1))
        self.PartImage.setScaledContents(True)
        self.partImage2 = QtWidgets.QLabel(self.centralwidget)
        self.partImage2.setGeometry(QtCore.QRect(50, 300, width2, height2))
        self.partImage2.clear()
        self.partImage2.setObjectName("PartImage2")
        self.partImage2.setPixmap(QtGui.QPixmap(image2))
        self.partImage2.resize(width2, height2)
        self.partImage2.setScaledContents(True)
        self.partImage2.raise_()

        self.PartName = QtWidgets.QLabel(self.centralwidget)
        self.PartName.setGeometry(QtCore.QRect(300, 20, 251, 51))
        self.PartName.setObjectName("PartName")
        self.PartName.setText(name)
        self.PartName.setStyleSheet(("font-size: 16pt; color: white;"))

        self.Parttitle = QtWidgets.QLabel(self.centralwidget)
        self.Parttitle.setGeometry(QtCore.QRect(480, 110, 251, 51))
        self.Parttitle.setObjectName("PartName")
        self.Parttitle.setText("What is it?")
        self.Parttitle.setStyleSheet(("font-size: 16pt; color: white;"))

        self.Parttitle = QtWidgets.QLabel(self.centralwidget)
        self.Parttitle.setGeometry(QtCore.QRect(480, 350, 251, 51))
        self.Parttitle.setObjectName("PartName")
        self.Parttitle.setText("What Does it do?")
        self.Parttitle.setStyleSheet(("font-size: 16pt; color: white;"))


        self.PartDescription = QtWidgets.QLabel(self.centralwidget)
        self.PartDescription.setGeometry(QtCore.QRect(480, 150, 250, 200))
        self.PartDescription.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.PartDescription.setObjectName("PartDescription")
        self.PartDescription.setText(description)
        self.PartDescription.setWordWrap(True)
        self.PartDescription.setStyleSheet(("font-size: 12pt; color: white;"))

        self.PartDescription2 = QtWidgets.QLabel(self.centralwidget)
        self.PartDescription2.setGeometry(QtCore.QRect(480, 390, 250, 200))
        self.PartDescription2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.PartDescription2.setObjectName("PartDescription")
        self.PartDescription2.setText(description2)
        self.PartDescription2.setWordWrap(True)
        self.PartDescription2.setStyleSheet(("font-size: 12pt; color: white;"))


        PartAnalyzer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PartAnalyzer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        PartAnalyzer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PartAnalyzer)
        self.statusbar.setObjectName("statusbar")
        PartAnalyzer.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(PartAnalyzer)
#Test
def window2():
    app1 = QtWidgets.QApplication(sys.argv)
    PartAnalyzer1 = QtWidgets.QMainWindow()
    ui1 = Ui_PartAnalyzer()
    #width height of first image, width height of second image
    ui1.setupUi(PartAnalyzer1, "Graphics Processing Unit", descriptions[1], "../images/gpu.png", "../images/gpu2.png", 300, 200, 400, 200)
    PartAnalyzer1.show()
    sys.exit(app1.exec_())
    #print(Ui_PartAnalyzer.partDescriptions(0))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PartAnalyzer = QtWidgets.QMainWindow()
    ui = Ui_PartAnalyzer()
    ui.setupUi(PartAnalyzer, "Central Processing Unit", descriptions[0], "../images/i7_cpu.jpg", "../images/ryzen9.JPG", 200, 200, 200, 200)
    PartAnalyzer.show()
    window2()

    sys.exit(app.exec_())
