import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
import home_window
from test5_question1_window import Test5_Question1_Window

# mysql ##################################
cnx = mysql.connector.connect(
    user = "root",
    password = "sori0927",
    host = "127.0.0.1",
    port = 3306,
    database = "test_zip"
)

cursor = cnx.cursor()

class Test5_StartWindow(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('연애세포 생존 테스트')
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resize(1100, 800)

        # 로고
        logo = QPushButton("", self)
        logo.resize(100, 50)
        logo.move(30, 30)
        logo.clicked.connect(self.btn_Home)
        logo.setStyleSheet('image:url(./image/logo.png); border:0px;')

        # 이름 입력받기
        self.name = QLineEdit("", self)
        self.name.setFont(QtGui.QFont("맑은 고딕", 20))
        self.name.setStyleSheet("overflow-x:hidden;" "overflow-y:hidden")
        self.name.resize(200, 60)
        self.name.move(50, 100)
        # 엔터키 누르면 실행
        self.name.returnPressed.connect(self.lineEditChanged)

        self.label = QLabel("의 연애세포는 살아있는가?", self)
        self.label.setFont(QtGui.QFont("맑은 고딕", 26))
        self.label.resize(800, 60)
        self.label.move(255, 100)

        #이미지
        img = QLabel("", self)
        img.resize(1000, 450)
        img.move(50, 200)
        img.setStyleSheet('image:url(./image/lc-TEST.png); border:0px;')

        #시작 버튼
        btn_start = QPushButton("", self)
        btn_start.resize(200, 80)
        btn_start.move(450, 670)
        btn_start.clicked.connect(self.start_click)
        btn_start.setStyleSheet('image:url(./image/START.png); border:0px;')

        self.test1_question1_window = Test5_Question1_Window(self)

    def start_click(self):
        self.test1_question1_window.name_label.setText(self.name.text())
        self.test1_question1_window.show()
        if self.label.text() == "'s Love Cell Survival Test":
            self.test1_question1_window.label.setText("         's Love Cell Survival Test")
            self.test1_question1_window.q1.setText("I prefer having a meal and watching a movie alone. ")
        elif self.label.text() == "恋愛細胞生存テスト":
            self.test1_question1_window.label.setText("         恋愛細胞生存テスト")
            self.test1_question1_window.q1.setText("私は一人で食事をして映画を見る方が好きです。")

        self.hide()

    def btn_Home(self):
        self.start = home_window.Home_Window(self)
        self.start.show()
        self.hide()

    def lineEditChanged(self):
        self.user_name = self.name.text()
        print(self.user_name)

        sql = "INSERT INTO lovesurvival_test(name, calculate, result) VALUES(%s, %s, %s);"
        cursor.execute(sql, (self.user_name, 0, 0))
        cnx.commit()
        print(cursor.rowcount, "record inserted")

