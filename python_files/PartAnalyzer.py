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

partNames = ["CPU", "GPU", "CPU-COOLER", "RAM", "SSD", "MotherBoard", "CMOS", "PCIe_x1", "PCIe_x16", "CPU Power ATX", 
             "ANTENNA", "HDMI", "USB3.2_PS2", "USB3.2_TypeA_TypeC", "LAN_USB2.0", "AUDIO-JACKS", "CPU-SOCKET", "M.2 Slot", "RAM Slot",
             "USB 3.2", "Front Panel Audio Header", "Thunderbolt AIC connecter", "Sata connecters", "LED",
             "CPU Fan Header", "ATX Power Connecter", "TPM Header", "Serial Port Header", "GPU Pin",
             "Power ATX", "Case Header", "CHA/Waterpump fan connector"]

partImages = [
                ["../images/i7_cpu.jpg", "../images/ryzen9.jpg"], 
                ["../images/gpu.png", "../images/gpu2.png"],
                ["../images/cpu_cooler2.png", "../images/water_cooled.jpg"],
                ["../images/ramstick.png", "../images/ram.png"],
                ["../images/m.2_ssd.jpg", "../images/ssd.png"],
                ["../images/motherboardReplace.png", "../images/clear_image.png"],
                ["../images/cmos.jpg", "../images/cmos2.png"],
                ["../images/network_adapter.jpg", "../images/port_expansion.jpg"],
                ["../images/port_expansion.jpg", "../images/gpu2.png"],
                ["../images/cpu_cable.jpg", "../images/cpuAtx.jpg"],
                ["../images/antenna_port.jpg", "../images/antenna_port2.png"],
                ["../images/hdmi_port.png", "../images/hdmi_port2.jpg"],
                ["../images/PS2_port.jpg", "../images/usb3.2_port.jpg"],
                ["../images/usb3.2_typeA_port.jpg", "../images/usb3.2_typeC_port.jpg"],
                ["../images/lan_port.jpg", "../images/usb2.0_port.jpg"],
                ["../images/audio_jacks_port.jpg", "../images/audio_jacks_port2.jpg"],
                ["../images/intel_socket.png", "../images/amd_socket.png"],
                ["../images/M.2_slot.jpg", "../images/M.2_slot2.jpg"],
                ["../images/ram_slots.png", "../images/ram_slots2.png"],
                
                ["../images/USB2.0Header.jpg", "../images/USB3.2Header.png"],
                ["../images/FrontPanelAudioHeader.jpg", "../images/FrontPanelAudioHeader2.jpg"],
                ["../images/ThunderBoltCard.jpg", "../images/TBTHeaderCable.jpg"],
                ["../images/sataconnector.jpg", "../images/SataCable.jpg"],
                ["../images/AddHeader.jpg", "../images/RGBHeader2.jpg"],
                ["../images/CPUFanHeader.jpg", "../images/CPUFanHeader2.jpg"],
                ["../images/ATXPower.jpg", "../images/cpuAtx.jpg"],
                ["../images/TPM.jpg", "../images/TPM2.jpg"],
                ["../images/SPI.jpg", "../images/SPI2.jpg"],
                ["../images/gpuConnected.jpg", "../images/GPU16Pin.png"],
                ["../images/24.png", "../images/24pinCable.jpg"],
                ["../images/caseIO.jpg", "../images/caseConnector.jpg"],
                ["../images/CHAFan.jpg", "../images/water_cooled.jpg"]

              ]

partCoordinates = [
                    [200, 200, 200, 200], [400,300,400,200], [200,200,400,200], [300, 100, 300, 200],
                    [300, 100, 300, 250], [300, 400, 200, 200], [200,200,200,200], [200, 200, 200, 200],
                    [200, 200, 400, 200], [200, 150, 300, 240], [350, 80, 300, 240], [350, 80, 350, 240],
                    [350, 80, 350, 80],[350, 80, 350, 80],[350, 80, 350, 80], [350,80,350,100],
                    [200,200,200,200], [200,200,200,200], [200, 200, 300, 200], [200,200,200,200],
                    [200,200,200,200], [200,200,200,200], [200,200,200,200], [200,200,200,200],
                    [200,200,200,200], [200,200,200,200] ,[200,200,200,200], [200,200,200,200],
                    [200,200,200,200], [200, 200, 200, 200], [200,200,200,200], [200,200,200,200]

                  ]

shortDescriptions = ["CPU stands for Central Processing Unit. The CPU is the BRAIN of the computer,"
                    " containing all the circuitry needed to process input, store data, and output results.",
                    "GPU stands for Graphics Processing Unit (Graphics Card. The GPU is a specialized electronic"
                    " circuit that accelerates the creation and rendering of images, video, and animation.",
                    "CPU cooler removes the heat produced from the cpu to keep it from overheating and becoming damaged.",
                    "RAM stands for Random Access Memory. The RAM is short term memory where data is stored as the processor needs it.",
                    "SSD stands for Solid-State Drive. M.2 is a form factor for SSDs. Similiar to a Hard drive, an SSD stores data even when the pc is off."
                    " However it uses flash memory and is much faster.",
                    "MotherBoard",
                    "CMOS battery powers BIOS firmware",
                    "PCIe x1 is a slot for low demanding PCIe expansion card",
                    "PCIe x16 is a slot for expansion card with high bandwith requirements like graphics card",
                    "The CPU Pin Connector powers the CPU and varies in number of pins.",
                    "These are antenna ports for wifi",
                    "This is a port for HDMI connection",
                    "This is a port for USB3.2 and PS/2",
                    "This is a port for USB3.2 type-A and USB3.2 type-C",
                    "This is a port for LAN or local area network ethernet and USB2.0",
                    "This is a port for audio jacks for sound and mic",
                    "CPU Socket",
                    "M.2",
                    "These are slots for RAM sticks",
                    "These are USB 3.2 slots",
                    "Allows audio connection to the case's ports",
                    "Thunderbolt AIC gives users a chance to use one cable to access high-speed and high resolution media",
                    "Powers various hardware components such as drives",
                    "LED Headers just allow connection to led striped and other lighted accessories",
                    "CPU Fan Header is used to mainly power the fan on the CPU.",
                    "The ATX Power Connector powers most of the system",
                    "The TPM Header allows connection to a microchip ",
                    "The COM header allows an extra serial port",
                    "The GPU pins power the GPU which also varies in number of pins",
                    "Power ATX powers most of the system",
                    "The Case header connects the motherboard to the case allowing the case to turn off the system and more.",
                    "The CHA Fan or Waterpump connector allows an extra connection to a case fan."


                    ]

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
                "configurations: x1, x4, x8, x16, and x32.",

                "PCIe (peripheral component interconnect express) is an interface standard for"
                " connecting high-speed components. The types of PCIe slots come in different physical"
                " configurations: x1, x4, x8, x16, and x32.",

                "The CPU-CABLE is simply just a power source for the CPU",

                "These are ports for Antenna's. Only equipped for a motherboard with WI-FI, however "
                "you can always purchase a seperate wifi card and it will come with its own antenna ports",
                
                "This port is for HDMI cables. HDMI stands for High Definition MultiMedia Interface",

                "The top image is the PS/2 port. The bottom image is the USB 3.2 ports.",
                    
                "The top image is the USB 3.2 Type-A port. The bottom impage is the USB 3.2 Type-C port",

                "The top image is the LAN/Ethernet port. The bottom image are the USB 2.0 ports",
                    
                "These are the audio jacks port. The blue is the Line in, the pink is the Mic in, and the green is the Line out.",

                "The socket is the array of pins or pin placeholders and the securing mechanism for the"
                " processor.",

                "The M.2 Slot is a format designed for manufacterurs to replace a variety of specific devices"
                " and do it in a tiny space, and require very little power with just 4 PCIe lanes.",

                "RAM slots are vertical slots, typically numbering from two or four, located"
                " to right of the CPU.",

                "The USB 3.2 Gen1 Header allows the computer to add extra USB ports.",

                "The Front Panel audio header is usually located on the lower left of your motherboard and it basically"
                "connects your audio.",

                "Thunderbolt consists of 4 PCI Expresslanes and a DisplayPort connection. An Add-in card (AIC) gets these from"
                "the PCIe slot and the DisplayPort cable you plug into the card.",

                "Sata ports are generally known as sata connecters, and they are used to power hardware to motherboards.",


                "Used for connecting to LED strips and other accessories to your PC.",

                "CPU Fan Header is the main header used by the motherboard, and the BIOS and any other software.",

                "ATX is a connecter that connects the power supply to an ATX style MotherBoard.",

                "TPM or Trusted Platform Module is a microchip attached to the motherboard that provides hardware-based"
                " cybersecurity.",

                "SPI or Serial Port Header is this COM1 hewader that supports a serial port module.",

                "The GPU Power Pins usually consist from 8 to possibly 24 pin connectors.",

                "The motherboard Power Pins usually consts from 10 to 24 pin connectors",

                "Connects the case buttons and lights to the motherboard",

                "CHA or chassis is another word for a computer case. So CHA Fans are just case fans headers. "

                ]

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

                "The PCIe x16 slot is used to plug in high bandwidth like graphics cards. However, these x16 slots"
                " could be used by any of the devices that would instead go in a smaller slot.",

                "The CPU-CABLE powers the CPU allowing it to have the energy needed to process information."
                " If the CPU does not have enough power, the computer will slow down.",

                "Expands the PC's reach for a wireless internet connection (WIFI).", 

                "It transfers data across devices, usually outputs onto a monitor or tv. Pixel data, and audio data.", 

                "A PS/2 port is a mouse port/keyboard port for "
                "IBM compatible computers. (Old technology not commonly used) Then replaced with USB (universal-serial bus)"
                " USB 3.2 (10 times faster transfer rate than USB 2.0) is Used for any peripherals that utilize USB",
                
                "USB Type-A is primarily used to host controlers in computers and hubs. However it is losing popularity."
                " USB Type-C is becoming increasingly common, it transfers much faster data and power.",
                "LAN or Local Area Network, more commonly known as Ethernet, is a wired internet connection. "
                "USB 2.0 is used for any peripherals that utilize USB, usually for keyboard/mouse since its not as fast as USB 3.0",
                "Mic allows input through a microphone. Line in allows for more data for input. Line out outputs the data for sound through" 
                "speakers or a headset",

                " The socket hold the processor in place and connects the motherboard to the"
                " avaiable processing power. There are different types of socket, the image"
                " above is for Intel CPUs and the image under is for AMD CPUs",

                "The M.2 can support, potentially, any storage or disk drive, GPU or port expansion"
                ", or low-power gadget that uses a USB connection, could all be mounted on a card"
                " pluggewd into the M.2 slot at the same time.",

                "A RAM slot is just a slot for the RAM to be inserted."
                " Ram comes in pairs (apply in odds); two RAM sticks should be inserted in every other slot (Dual Channel mode) which allows the computer to take"
                " full advantage. In addition, make sure these RAM sticks have the same speed.",

                "USB 3.2 is a different from an older generation USB such as 2.0 as it is faster, transferring up to"
                "20Gpbs.",

                "The HD_AUDIO cable connects the front audio/mic jack connecters from your case rto your motherboard, so they"
                " can be used. You can plug there whatever you'd like: speakers, headphones, etc...",

                "You can transmit DisplayPort signals through Thunderbolt, allowing you to re-route an external graphics card"
                " output to the displayport connections.",

                "They are designed to carry data between the motherboard and the drive using a SATA data cable.",

                "Adds lighting to either fans, or other additional devices.",

                "Regulates and controls the CPU's thermals depending on the load by controlling the fan(s) speed.",

                "This connecter is used to supply additional 12V current to he motherboard, which is used to power most devices on it.",

                "You can add TPM to your PC if it doesn't come with one, but you'll need this TPM header to do so as it adds secuity.",

                "This allows a seperate display output specific for older monitors or TVs which support SPI.",

                "The Pins connect directly to the PSU which powers it and if the PSU cannot supply "
                "enough power, then the speed of the GPU and even the entire computer will slow down.",

                "These Pins power most of the motherbaord, including the pcie slots, ram, any storage devices, and any "
                "headers or peripherals.",

                "The cable allows the power button to work and if included, led will power on.",

                "The CHA Fans are optional but they provide air flow for the case"

                ]

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
        self.PartName.adjustSize()

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
    print(len(partNames), " ", len(partCoordinates) ," ",  len(partImages), " ", len(descriptions), " ", len(descriptions2))
