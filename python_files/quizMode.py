# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quiz.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer

import mainMenu

class Ui_Quiz(object):
    def contents(self):
        self.questions = ["What is the CPU for computers?", "What is the GPU for computers?", "What is the RAM for computers?", "What is an SSD for computers?", "What is the CMOS for computers?"]
        
        self.question_images = ["../images/ryzen9.JPG", "../images/gpu.png", "../images/ram stick.jpg", "../images/m.2_ssd.jpg", "../images/cmos.jpg"]

        self.question_images_sizes = [[690,180,200,200], [590,180,400,200], [590,180,400,100], [590,180,400,100], [720,180,200,200]] # 1st - x pos, 2nd - y pos, 3rd - width, 4th - height

        self.answers = [["Central Processing Unit - Computes all basic arithmetic and other operations", "Computer Power User - A person who can utilize all the computer's power", "Critical Patch Update - A crucial update in software to fix major issues", "Central Policy Unit - The policy that is central for software to run"], 
                    ["Ground Power Unit - Allows the pc's components flow of electricity to ground", "Graphics Processing Unit - speciailzed processor designed to accelerate graphics rendering", "General Public Utilities - Necessary processes that all pc needs to run", "General Processing Unit - Similar to a central procesing unit but more general"],
                    ["Rational Asset Manager - Software that manages different assets", "Remote Application Management - The BIOS management of applications", "Random Access Memory - Memory that computer stores for short term data", "Random Access Machine - Processor that is granted access to storage"],
                    ["Signed Sealed Delivered - Stevie wonder song that plays after your pc parts ship", "Switching Sequence Detection - Processor detecting a switch from binary to decimal", "Structured Self Development - The computer's boot up process before OS loads", "Solid State Drive - Flash-based memory"],
                    ["Cellular Management Operation System - The BIOS system to communicate with the processor", "Configuration Memory Operating System - Allows communication between processor and memory" , "Cargo Movement Operations System - The gpu system to move large data", "Complementary Metal-Oxide Semiconductor - Small piece of memory that stores the BIOS settings"]]

        self.answer_indexes = [0,1,2,3,3]

        self.question_num = 0
        self.total_question_num = 5
        self.questions_answered_correct = [] # list of the question numbers (0 to n)

    def setupQuiz(self, MainWindow):
        self.contents()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 576)



        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_image = QtWidgets.QLabel(self.centralwidget)
        self.background_image.setGeometry(QtCore.QRect(0, 0, 1031, 561))
        self.background_image.setText("")
        self.background_image.setPixmap(QtGui.QPixmap("../images/quiz_background.PNG"))
        self.background_image.setScaledContents(True)
        self.background_image.setObjectName("background_image")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(420, 40, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(255, 255, 255);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(370, 490, 291, 21))
        self.progress_bar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progressBar")
        self.progress_bar.setValue(0)
        self.question_text = QtWidgets.QLabel(self.centralwidget)
        self.question_text.setGeometry(QtCore.QRect(40, 100, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.question_text.setFont(font)
        self.question_text.setStyleSheet("color:rgb(255, 255, 255)")
        self.question_text.setAlignment(QtCore.Qt.AlignCenter)
        self.question_text.setObjectName("question_text")
        self.question_image = QtWidgets.QLabel(self.centralwidget)
        self.question_image.setGeometry(QtCore.QRect(690, 180, 221, 201))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.question_image.setFont(font)
        self.question_image.setText("")
        self.question_image.setPixmap(QtGui.QPixmap("../images/ryzen9.JPG"))
        self.question_image.setScaledContents(True)
        self.question_image.setAlignment(QtCore.Qt.AlignCenter)
        self.question_image.setObjectName("question_image")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(840, 470, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.next_button.setFont(font)
        self.next_button.setStyleSheet("color:rgb(0, 255, 255);\n"
                                        "background-color: rgb(33, 33, 33);")
        self.next_button.setObjectName("next_button")
        self.previous_button = QtWidgets.QPushButton(self.centralwidget)
        self.previous_button.setGeometry(QtCore.QRect(50, 470, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.previous_button.setFont(font)
        self.previous_button.setStyleSheet("color:rgb(0, 255, 255);\n"
                                        "background-color: rgb(33, 33, 33);")
        self.previous_button.setObjectName("previous_button")
        self.question_status_text = QtWidgets.QLabel(self.centralwidget)
        self.question_status_text.setGeometry(QtCore.QRect(730, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.question_status_text.setFont(font)
        self.question_status_text.setStyleSheet("color: rgb(0, 255, 0);")
        self.question_status_text.setAlignment(QtCore.Qt.AlignCenter)
        self.question_status_text.setObjectName("question_status_text")
        self.progress_text = QtWidgets.QLabel(self.centralwidget)
        self.progress_text.setGeometry(QtCore.QRect(440, 460, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.progress_text.setFont(font)
        self.progress_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.progress_text.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_text.setObjectName("progress_text")
        self.answer_button1 = QtWidgets.QRadioButton(self.centralwidget)
        self.answer_button1.setGeometry(QtCore.QRect(30, 180, 610, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.answer_button1.setFont(font)
        self.answer_button1.setStyleSheet("QRadioButton{color:rgb(255, 255, 255)"
                                        "}QRadioButton::indicator {width: 40px;"
                                        "}")
        self.answer_button1.setObjectName("answer_button1")
        self.answer_button2 = QtWidgets.QRadioButton(self.centralwidget)
        self.answer_button2.setGeometry(QtCore.QRect(30, 230, 610, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.answer_button2.setFont(font)
        self.answer_button2.setStyleSheet("QRadioButton{color:rgb(255, 255, 255)"
                                        "}QRadioButton::indicator {width: 40px;"
                                        "}")
        self.answer_button2.setObjectName("answer_button2")
        self.answer_button3 = QtWidgets.QRadioButton(self.centralwidget)
        self.answer_button3.setGeometry(QtCore.QRect(30, 280, 610, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.answer_button3.setFont(font)
        self.answer_button3.setStyleSheet("QRadioButton{color:rgb(255, 255, 255)"
                                        "}QRadioButton::indicator {width: 40px;"
                                        "}")
        self.answer_button3.setObjectName("answer_button3")
        self.answer_button4 = QtWidgets.QRadioButton(self.centralwidget)
        self.answer_button4.setGeometry(QtCore.QRect(30, 330, 610, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.answer_button4.setFont(font)
        self.answer_button4.setStyleSheet("QRadioButton{color:rgb(255, 255, 255)"
                                        "}QRadioButton::indicator {width: 40px;"
                                        "}")
        self.answer_button4.setObjectName("answer_button4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.backButton = QtWidgets.QPushButton(MainWindow)
        self.backButton.setGeometry(QtCore.QRect(900, 25, 70, 31))
        self.backButton.setText("Back")
        self.backButton.setObjectName("")
        self.backButton.clicked.connect(lambda: self.openMain())
        self.backButton.clicked.connect(MainWindow.close)

        self.audioButton = QtWidgets.QPushButton(MainWindow)
        self.audioButton.setGeometry(QtCore.QRect(820, 25, 70, 31))
        self.audioButton.setText("Toggle Music")
        self.audioButton.setObjectName("audioButton")

        # Other events called here
        self.click_events()

        self.retranslateQuiz(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.set_questions_answers(self.question_num)

    
    def retranslateQuiz(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Hardware Quiz"))
        self.question_text.setText(_translate("MainWindow", "What is the CPU for computers?"))
        self.next_button.setText(_translate("MainWindow", "Next Question"))
        self.previous_button.setText(_translate("MainWindow", "Previous Question"))
        self.question_status_text.setText(_translate("MainWindow", ""))
        self.answer_button1.setText(_translate("MainWindow", "Central Processing Unit - Computes all basic arithmetic and other operations"))
        self.answer_button2.setText(_translate("MainWindow", "Computer Power User"))
        self.answer_button3.setText(_translate("MainWindow", "Critical Patch Update"))
        self.answer_button4.setText(_translate("MainWindow", "Central Policy Unit"))
        self.progress_text.setText(_translate("MainWindow", "Quiz Progress"))

    def update_progress_bar(self):
        value = (float(len(self.questions_answered_correct)) / self.total_question_num) * 100 # Value in percentage
        self.progress_bar.setValue(value)

    def check_answer(self, answer):
        correct_answer = self.answer_indexes[self.question_num]
        if (answer == correct_answer):
            self.question_status_text.setText("Correct!")
            self.question_status_text.setStyleSheet("color: rgb(0, 255, 0);")
            if (self.question_num in self.questions_answered_correct):
                return
            self.questions_answered_correct.append(self.question_num)
            self.update_progress_bar()
            self.playsoundCorrect()
        elif (not self.answer_button1.isChecked() and not self.answer_button2.isChecked() 
        and not self.answer_button3.isChecked() and not self.answer_button4.isChecked()):
            self.question_status_text.setText("")
        else:
            self.question_status_text.setText("Incorrect!")
            self.question_status_text.setStyleSheet("color: rgb(255, 0, 0);")
            self.playSoundWrong()

    def next_question(self):
        self.question_num = self.question_num + 1
        self.deselect_buttons()
        self.set_questions_answers(self.question_num)

    def prev_question(self):
        if (self.question_num > 0):
            self.question_num = self.question_num - 1
            self.set_questions_answers(self.question_num)
            self.deselect_buttons()

    def click_events(self):
        self.answer_button1.toggled.connect(lambda: self.check_answer(0))
        self.answer_button2.toggled.connect(lambda: self.check_answer(1))
        self.answer_button3.toggled.connect(lambda: self.check_answer(2))
        self.answer_button4.toggled.connect(lambda: self.check_answer(3))

        self.next_button.clicked.connect(lambda: self.next_question())
        self.previous_button.clicked.connect(lambda: self.prev_question())

    def set_questions_answers(self, question_num):
        self.question_text.setText(self.questions[question_num])
        self.question_status_text.setText("")
        self.question_image.setPixmap(QtGui.QPixmap(self.question_images[question_num]))
        self.question_image.setGeometry(self.question_images_sizes[question_num][0],
         self.question_images_sizes[question_num][1], self.question_images_sizes[question_num][2], self.question_images_sizes[question_num][3])

        self.answer_button1.setText(self.answers[question_num][0])
        self.answer_button2.setText(self.answers[question_num][1])
        self.answer_button3.setText(self.answers[question_num][2])
        self.answer_button4.setText(self.answers[question_num][3])

    def deselect_buttons(self):
        # deselect boxes
        self.answer_buttons = [self.answer_button1, self.answer_button2, self.answer_button3, self.answer_button4]
        for button in self.answer_buttons:
            button.setAutoExclusive(False)
            button.setChecked(False)
            button.setAutoExclusive(True)

    def playsoundCorrect(self):
        self.music_player = QMediaPlayer()
        self.full_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sounds/correct.wav')
        self.url = QUrl.fromLocalFile(self.full_file_path)
        self.music_player.setMedia(QMediaContent(self.url))
        self.music_player.play()

    def playSoundWrong(self):
        self.music_player = QMediaPlayer()
        self.full_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sounds/wrong.mp3')
        self.url = QUrl.fromLocalFile(self.full_file_path)
        self.music_player.setMedia(QMediaContent(self.url))
        self.music_player.play()

    def openMain(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = mainMenu.Ui_MainMenu()
        self.ui.setupUi(self.window)
        self.window.show()




    




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Quiz()
    ui.setupQuiz(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
