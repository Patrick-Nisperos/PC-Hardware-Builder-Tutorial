# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quiz.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Quiz(object):
    def contents(self):
        self.questions = ["What is the CPU for computers?", "What is the GPU for computers?"]
        
        self.question_images = ["../images/ryzen9.JPG", "../images/gpu.png"]

        self.answers = [["Central Processing Unit - Computes all basic arithmetic and other operations", "Computer Power User", "Critical Patch Update", "Central Policy Unit"], 
                    ["Ground Power Unit", "Graphics Processing Unit", "General Public Utilities", "General Processing Unit"]]

        self.answer_indexes = [0,1]

        self.question_num = 0

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
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(370, 490, 291, 21))
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.answer_box1 = QtWidgets.QCheckBox(self.centralwidget)
        self.answer_box1.setGeometry(QtCore.QRect(30, 170, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.answer_box1.setFont(font)
        self.answer_box1.setStyleSheet("QCheckBox {\n"
                                        "    spacing: 5px;\n"
                                        "    color:rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QCheckBox::indicator {\n"
                                        "    width: 40px;\n"
                                        "}\n"
                                        "")
        self.answer_box1.setIconSize(QtCore.QSize(20, 20))
        self.answer_box1.setChecked(False)
        self.answer_box1.setObjectName("answer_box1")
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
        self.answer_box2 = QtWidgets.QCheckBox(self.centralwidget)
        self.answer_box2.setGeometry(QtCore.QRect(30, 220, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.answer_box2.setFont(font)
        self.answer_box2.setStyleSheet("QCheckBox {\n"
                                        "    spacing: 5px;\n"
                                        "    color:rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QCheckBox::indicator {\n"
                                        "    width: 40px;\n"
                                        "}\n"
                                        "")
        self.answer_box2.setIconSize(QtCore.QSize(20, 20))
        self.answer_box2.setChecked(False)
        self.answer_box2.setObjectName("answer_box2")
        self.answer_box3 = QtWidgets.QCheckBox(self.centralwidget)
        self.answer_box3.setGeometry(QtCore.QRect(30, 270, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.answer_box3.setFont(font)
        self.answer_box3.setStyleSheet("QCheckBox {\n"
                                        "    spacing: 5px;\n"
                                        "    color:rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QCheckBox::indicator {\n"
                                        "    width: 40px;\n"
                                        "}\n"
                                        "")
        self.answer_box3.setIconSize(QtCore.QSize(20, 20))
        self.answer_box3.setChecked(False)
        self.answer_box3.setObjectName("answer_box3")
        self.answer_box4 = QtWidgets.QCheckBox(self.centralwidget)
        self.answer_box4.setGeometry(QtCore.QRect(30, 320, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.answer_box4.setFont(font)
        self.answer_box4.setStyleSheet("QCheckBox {\n"
                                        "    spacing: 5px;\n"
                                        "    color:rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QCheckBox::indicator {\n"
                                        "    width: 40px;\n"
                                        "}\n"
                                        "")
        self.answer_box4.setIconSize(QtCore.QSize(20, 20))
        self.answer_box4.setChecked(False)
        self.answer_box4.setObjectName("answer_box4")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # Other events called here
        self.set_questions_answers(self.question_num)
        self.click_events()

        self.retranslateQuiz(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def retranslateQuiz(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Hardware Quiz"))
        self.answer_box1.setText(_translate("MainWindow", "Central Processing Unit - Computes all basic arithmetic and other operations"))
        self.question_text.setText(_translate("MainWindow", "What is the CPU for computers?"))
        self.next_button.setText(_translate("MainWindow", "Next Question"))
        self.previous_button.setText(_translate("MainWindow", "Previous Question"))
        self.question_status_text.setText(_translate("MainWindow", ""))
        self.answer_box2.setText(_translate("MainWindow", "Computer Power User"))
        self.answer_box3.setText(_translate("MainWindow", "Critical Patch Update"))
        self.answer_box4.setText(_translate("MainWindow", "Central Policy Unit"))
        self.progress_text.setText(_translate("MainWindow", "Quiz Progress"))

    def check_answer(self, answer):
        correct_answer = self.answer_indexes[self.question_num]
        if (answer == correct_answer):
            self.question_status_text.setText("Correct!")
            self.question_status_text.setStyleSheet("color: rgb(0, 255, 0);")
        elif (not self.answer_box1.isChecked() and not self.answer_box2.isChecked() and not self.answer_box3.isChecked() and not self.answer_box4.isChecked()):
            self.question_status_text.setText("")
        else:
            self.question_status_text.setText("Incorrect!")
            self.question_status_text.setStyleSheet("color: rgb(255, 0, 0);")

    def next_question(self):
        self.question_num = self.question_num + 1
        self.set_questions_answers(self.question_num)

    def prev_question(self):
        if (self.question_num > 0):
            self.question_num = self.question_num - 1
            self.set_questions_answers(self.question_num)

    def click_events(self):
        self.answer_box1.toggled.connect(lambda: self.check_answer(0))
        self.answer_box2.toggled.connect(lambda: self.check_answer(1))
        self.answer_box3.toggled.connect(lambda: self.check_answer(2))
        self.answer_box4.toggled.connect(lambda: self.check_answer(3))
        self.next_button.clicked.connect(lambda: self.next_question())
        self.previous_button.clicked.connect(lambda: self.prev_question())

    def set_questions_answers(self, question_num):

        self.question_text.setText(self.questions[question_num])
        self.question_status_text.setText("")
        self.question_image.setPixmap(QtGui.QPixmap(self.question_images[question_num]))

        self.answer_box1.setText(self.answers[question_num][0])
        self.answer_box2.setText(self.answers[question_num][1])
        self.answer_box3.setText(self.answers[question_num][2])
        self.answer_box4.setText(self.answers[question_num][3])
        self.reset_check_boxes()

    def reset_check_boxes(self):
        self.answer_box1.setChecked(False)
        self.answer_box2.setChecked(False)
        self.answer_box3.setChecked(False)
        self.answer_box4.setChecked(False)



    




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Quiz()
    ui.setupQuiz(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
