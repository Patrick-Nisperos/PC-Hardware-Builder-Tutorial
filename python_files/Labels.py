import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QDrag, QPixmap, QColor

import PartAnalyzer as Analyzer
import buildMode

# Helper file for all parts and labels
# on the motherboard
# Not dragable, No Image, Has Part Analyzer, Has Hover Description
class Part(QLabel):
    def __init__(self, MainWindow, name, x, y, width, height):
        QLabel.__init__(self, MainWindow)
        self.effect = QGraphicsOpacityEffect()
        self.effect.setOpacity(0.3)
        self.name = name
        self.setPixmap(QPixmap("../images/clear_image.png"))
        self.setGeometry(QtCore.QRect(x, y, width, height))
        self.setMouseTracking(True)
        self.clear()
        self.setStyleSheet("QLabel::hover{background-color: yellow;}")

        self.setObjectName(self.name)
        self.setGraphicsEffect(self.effect)
    
    def mousePressEvent(self, event):
        if(event.button() == Qt.RightButton):
            index = 0
            for names in Analyzer.partNames:
                if(self.name == names and index < len(Analyzer.partNames)):
                    buildMode.Ui_MotherBoard.openPartAnalyzer(self, Analyzer.partNames[index],Analyzer.descriptions[index], Analyzer.descriptions2[index],
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
    def __init__(self, MainWindow, image, x, y, width, height, name):
        QLabel.__init__(self, MainWindow)
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
            self.playsound()

    def playsound(self):
        self.music_player = QMediaPlayer()
        self.full_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sounds/correct.wav')
        self.url = QUrl.fromLocalFile(self.full_file_path)
        self.music_player.setMedia(QMediaContent(self.url))
        self.music_player.play()

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