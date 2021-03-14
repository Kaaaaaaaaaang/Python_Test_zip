import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from stop import Stop_Window
from test1_start_window import Test1_StartWindow
from test2_start_window import Test2_StartWindow
from test3_start_window import Test3_StartWindow
from test4_start_window import Test4_StartWindow
from test5_start_window import Test5_StartWindow

class Home_Window(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Test.zip')
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resize(1100, 800)

        # 로고
        logo = QLabel("", self)
        logo.resize(100, 50)
        logo.move(30, 30)
        logo.setStyleSheet('image:url(./image/logo.png); border:0px;')

        # 번역 기능#########################################
        self.language = QComboBox(self)
        self.language.addItem('한국어')
        self.language.addItem('English')
        self.language.addItem('日本語')
        self.language.resize(100, 30)
        self.language.move(948, 65)
        self.language.setToolTip("Translate")
        ###############################################

        # 테스트 시작 버튼##############################
        btn_test1 = QPushButton("", self)
        btn_test1.resize(500, 350)
        btn_test1.move(50, 100)
        btn_test1.toggle()
        btn_test1.clicked.connect(self.btn_test1_click)
        btn_test1.setToolTip("BF_Test")
        btn_test1.setStyleSheet('image:url(./image/Front-end Back-end Test.png); border:0px;')

        btn_test2 = QPushButton("", self)
        btn_test2.resize(500, 300)
        btn_test2.move(548, 100)
        btn_test2.toggle()
        btn_test2.clicked.connect(self.btn_test2_click)
        btn_test2.setToolTip("My_mental_state_test")
        btn_test2.setStyleSheet('image:url(./image/사람에 관한 당신의 심리 상태.png); border:0px;')

        btn_test3 = QPushButton("", self)
        btn_test3.resize(250, 250)
        btn_test3.move(50, 448)
        btn_test3.toggle()
        btn_test3.clicked.connect(self.btn_test3_click)
        btn_test3.setToolTip("My_movie_Test")
        btn_test3.setStyleSheet('image:url(./image/My movie.png); border:0px;')

        btn_test4 = QPushButton("", self)
        btn_test4.resize(250, 250)
        btn_test4.move(300, 448)
        btn_test4.toggle()
        btn_test4.clicked.connect(self.btn_test4_click)
        btn_test4.setToolTip("New_Words_Test")
        btn_test4.setStyleSheet('image:url(./image/new_words_test.png); border:0px;')

        btn_test5 = QPushButton("", self)
        btn_test5.resize(500, 300)
        btn_test5.move(548, 398)
        btn_test5.toggle()
        btn_test5.clicked.connect(self.btn_test5_click)
        btn_test5.setToolTip("Love_Cell_Test")
        btn_test5.setStyleSheet('image:url(./image/Love cell survival.png); border:0px;')
        #########################################

        # 개발자 정보##################################
        subin = QLabel("Lee Su Bin   s2019s15@e-mirim.hs.kr", self)
        subin.resize(800, 30)
        subin.move(800, 740)

        sori = QLabel("Kang So Ri   s2019s01@e-mirim.hs.kr", self)
        sori.resize(800, 30)
        sori.move(800, 720)
        #####################################################
        self.test1_start_window = Test1_StartWindow(self)
        self.test2_start_window = Test2_StartWindow(self)
        self.test3_start_window = Test3_StartWindow(self)
        self.test4_start_window = Test4_StartWindow(self)
        self.test5_start_window = Test5_StartWindow(self)
        self.stop = Stop_Window(self)

    def btn_test1_click(self):
        self.test1_start_window.show()
        if self.language.currentText() == "English":
            self.test1_start_window.label.setText("the front end? Is it the backend?")
        elif self.language.currentText() == "日本語":
            self.test1_start_window.label.setText("はフロントエンドであるかバックエンドのか？")
        self.hide()

    def btn_test2_click(self):
        self.test2_start_window.show()
        if self.language.currentText() == "English":
            self.test2_start_window.label.setText("is state of mind these days")
        elif self.language.currentText() == "日本語":
            self.test2_start_window.label.setText("最近の僕の心理状態。")
        self.hide()

    def btn_test3_click(self):
        self.test3_start_window.show()
        if self.language.currentText() == "English":
            self.test3_start_window.label.setText("What movie goes well with()")
        elif self.language.currentText() == "日本語":
            self.test3_start_window.label.setText("はと合って映画は？")
        self.hide()

    def btn_test4_click(self):
        self.test4_start_window.show()
        self.hide()

    def btn_test5_click(self):
        self.test5_start_window.show()
        if self.language.currentText() == "English":
            self.test5_start_window.label.setText("'s Love Cell Survival Test")
        elif self.language.currentText() == "日本語":
            self.test5_start_window.label.setText("恋愛細胞生存テスト")
        self.hide()