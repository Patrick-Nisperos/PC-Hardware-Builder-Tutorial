# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motherBoard2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, motherBoardGUI):

        motherBoardGUI.setObjectName("MotherBoard")
        motherBoardGUI.resize(1210, 986)

            #Format is as follows for all components
        #Add to the GUI
        #Style sheet for hover and color of label
        #Set Coordinates x1 and y1 for placement x2 and y2 for size
        #Set mouse tracking on for dragging later
        #Clear text so we can have just the highlight w/o text
        #Name the label


        self.motherBoard = QtWidgets.QLabel(motherBoardGUI)
        self.motherBoard.setGeometry(QtCore.QRect(400, 0, 801, 971))
        self.motherBoard.setMouseTracking(True)
        self.motherBoard.setPixmap(QtGui.QPixmap("media/IntelMotherBoard.jpg"))
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
        self.cpu = QtWidgets.QLabel(motherBoardGUI)
        self.cpu.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow; }")
        self.cpu.setGeometry(QtCore.QRect(730, 170, 131, 211))
        self.cpu.setMouseTracking(True)
        self.cpu.clear()
        self.cpu.setObjectName("CPU")
        self.cpu.setGraphicsEffect(self.opacityEffect0)


        self.cpuCable = QtWidgets.QLabel(motherBoardGUI)
        self.cpuCable.setStyleSheet("QLabel::hover"
                                   "{ background-color : yellow; }")
        self.cpuCable.setGeometry(QtCore.QRect(570, 19, 50, 25))
        self.cpuCable.setMouseTracking(True)
        self.cpuCable.clear()
        self.cpuCable.setObjectName("CPU-Cable")
        self.cpuCable.setGraphicsEffect(self.opacityEffect1)


        #GPU ON LABEL
        self.gpu = QtWidgets.QLabel(motherBoardGUI)
        self.gpu.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow; }")
        self.gpu.setGeometry(QtCore.QRect(570, 565, 321, 31))
        self.gpu.setMouseTracking(True)
        self.gpu.clear()
        self.gpu.setObjectName("GPU")
        self.gpu.setGraphicsEffect(self.opacityEffect2)
        
        #RAM STICKS ON LABELS
        self.ram1 = QtWidgets.QLabel(motherBoardGUI)
        self.ram1.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow }")
        self.ram1.setGeometry(QtCore.QRect(960, 50, 20, 440))
        self.ram1.setMouseTracking(True)
        self.ram1.clear()
        self.ram1.setObjectName("RamStick1")
        self.ram1.setGraphicsEffect(self.opacityEffect3)
      
        self.ram2 = QtWidgets.QLabel(motherBoardGUI)
        self.ram2.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow }")
        self.ram2.setGeometry(QtCore.QRect(989, 50, 20, 440))
        self.ram2.setMouseTracking(True)
        self.ram2.clear()
        self.ram2.setObjectName("RamStick2")
        self.ram2.setGraphicsEffect(self.opacityEffect4)
     
        self.ram3 = QtWidgets.QLabel(motherBoardGUI)
        self.ram3.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow }")
        self.ram3.setGeometry(QtCore.QRect(1018, 50, 20, 440))
        self.ram3.setMouseTracking(True)
        self.ram3.clear()
        self.ram3.setObjectName("RamStick3")
        self.ram3.setGraphicsEffect(self.opacityEffect5)

        self.ram4 = QtWidgets.QLabel(motherBoardGUI)
        self.ram4.setStyleSheet("QLabel::hover"
                               "{ background-color : yellow }")
        self.ram4.setGeometry(QtCore.QRect(1047, 50, 20, 440))
        self.ram4.setMouseTracking(True)
        self.ram4.clear()
        self.ram4.setObjectName("RamStick4")
        self.ram4.setGraphicsEffect(self.opacityEffect6)


        #label 8 is m.2
        self.m2 = QtWidgets.QLabel(motherBoardGUI)
        self.m2.setStyleSheet("QLabel::hover"
                             "{ background-color : yellow }")
        self.m2.setGeometry(QtCore.QRect(860, 830, 251, 71))
        self.m2.clear()
        self.m2.setObjectName("M.2 SSD")
        self.m2.setGraphicsEffect(self.opacityEffect7)


        self.retranslateUi(motherBoardGUI)
        QtCore.QMetaObject.connectSlotsByName(motherBoardGUI)

    def retranslateUi(self, motherBoardGUI):
        _translate = QtCore.QCoreApplication.translate
        motherBoardGUI.setWindowTitle(_translate("MotherBoard", "MotherBoard"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    motherBoardGUI = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(motherBoardGUI)
    motherBoardGUI.show()
    sys.exit(app.exec_())
