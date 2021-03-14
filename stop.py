import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import home_window

class Stop_Window(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowIcon(QIcon('./image/icon.png'))
        self.resize(1100, 800)

        back = QLabel("", self)
        back.resize(1100, 800)
        back.move(0, 0)
        back.setStyleSheet("background-color: rgb(255, 255, 255);")

        # 로고
        logo = QLabel("", self)
        logo.resize(100, 50)
        logo.move(30, 30)
        logo.setStyleSheet('image:url(./image/logo.png); border:0px;')

        #이미지
        img = QLabel("", self)
        img.resize(1000, 450)
        img.move(50, 150)
        img.setStyleSheet('image:url(./image/stop.png); border:0px;')

        #이전 버튼
        btn_back = QPushButton("", self)
        btn_back.resize(200, 80)
        btn_back.move(450, 660)
        btn_back.setStyleSheet('image:url(./image/back.png); border:0px;')
        btn_back.clicked.connect(self.btn_Start)

    def btn_Start(self):
        self.start = home_window.Home_Window(self)
        self.start.show()
        self.hide()
