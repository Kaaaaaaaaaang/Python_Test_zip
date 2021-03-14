import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
from test1_question3_window import Test1_Question3_Window
sys.setrecursionlimit(10000)

# mysql ##################################
cnx = mysql.connector.connect(
    user = "root",
    password = "sori0927",
    host = "127.0.0.1",
    port = 3306,
    database = "test_zip"
)

cursor = cnx.cursor()

class Test1_Question2_Window(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('당신은 프론트엔드인가? 백엔드인가?')
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.resize(880, 500)

        back = QLabel("", self)
        back.resize(880, 500)
        back.move(0, 0)
        back.setStyleSheet('image:url(./image/background.png); border:0px;')

        # 로고
        logo = QLabel("", self)
        logo.resize(100, 50)
        logo.move(30, 30)
        logo.setStyleSheet('image:url(./image/logo.png); border:0px;')

        # 테스트 이름
        self.name_label = QLabel("이수빈", self)
        self.name_label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.name_label.resize(80, 60)
        self.name_label.move(40, 100)

        self.label = QLabel("         은(는) 프론트엔드인가? 백엔드인가?", self)
        self.label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.label.resize(800, 60)
        self.label.move(40, 100)

        #질문
        self.q1 = QLabel("둘 중 한가지를 만들 수 있다면?", self)
        self.q1.setFont(QtGui.QFont("맑은 고딕", 26))
        self.q1.resize(800, 60)
        self.q1.move(30, 140)

        #답 버튼
        self.a1 = QPushButton("스티브 잡스 옷 입히기", self)
        self.a1.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a1.resize(800, 100)
        self.a1.move(30, 210)
        self.a1.clicked.connect(self.a_click)

        self.a2 = QPushButton("Siri랑 대화하기", self)
        self.a2.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a2.resize(800, 100)
        self.a2.move(30, 320)
        self.a2.clicked.connect(self.b_click)

        self.test1_question3_window = Test1_Question3_Window(self)
    def a_click(self):
        self.test1_question3_window.show()
        user_name = self.name_label.text()
        self.test1_question3_window.name_label.setText(user_name)

        sql = "UPDATE programmer_Test SET calculate = calculate + 5 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print(user_name, ">>>점수 추가 완료")

        if self.label.text() == "Are you the frontend? Is it the backend?":
            self.test1_question3_window.label.setText("Are you the frontend? Is it the backend?")
            self.test1_question3_window.q1.setText("What’s one plus one?")
            self.test1_question3_window.a2.setText("Cutie")
        elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
            self.test1_question3_window.label.setText("あなたはフロントエンドであるかバックエンドのか？")
            self.test1_question3_window.q1.setText("2つのうちの1つを作れたらどうする？")
            self.test1_question3_window.a2.setText("かわいい子")
        self.hide()

    def b_click(self):
        self.test1_question3_window.show()
        user_name = self.name_label.text()
        self.test1_question3_window.name_label.setText(user_name)

        sql = "UPDATE programmer_Test SET calculate = calculate + 5 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print(user_name, ">>>점수 추가 완료")
        if self.label.text() == "Are you the frontend? Is it the backend?":
            self.test1_question3_window.label.setText("Are you the frontend? Is it the backend?")
            self.test1_question3_window.q1.setText("What’s one plus one?")
            self.test1_question3_window.a2.setText("Cutie")
        elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
            self.test1_question3_window.label.setText("あなたはフロントエンドであるかバックエンドのか？")
            self.test1_question3_window.q1.setText("2つのうちの1つを作れたらどうする？")
            self.test1_question3_window.a2.setText("かわいい子")
        self.hide()

