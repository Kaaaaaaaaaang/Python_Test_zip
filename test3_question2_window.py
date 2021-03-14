import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
from test3_question3_window import Test3_Question3_Window

# mysql ##################################
cnx = mysql.connector.connect(
    user = "root",
    password = "sori0927",
    host = "127.0.0.1",
    port = 3306,
    database = "test_zip"
)

cursor = cnx.cursor()

class Test3_Question2_Window(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('나와 어울리는 영화는?')
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.resize(880, 700)

        back = QLabel("", self)
        back.resize(880, 700)
        back.move(0, 0)
        back.setStyleSheet('image:url(./image/background2.png); border:0px;')

        # 로고
        logo = QLabel("", self)
        logo.resize(100, 50)
        logo.move(30, 30)
        logo.setStyleSheet('image:url(./image/logo.png); border:0px;')

        # 테스트 이름
        self.name = QLabel("이수빈", self)
        self.name.setFont(QtGui.QFont("맑은 고딕", 13))
        self.name.resize(80, 60)
        self.name.move(40, 100)

        self.label = QLabel("         와(과) 어울리는 영화는?", self)
        self.label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.label.resize(800, 60)
        self.label.move(40, 100)

        #질문
        self.q1 = QLabel("가장 기억에 남는 명대사는?", self)
        self.q1.setFont(QtGui.QFont("맑은 고딕", 26))
        self.q1.resize(800, 60)
        self.q1.move(40, 140)

        #답 버튼
        self.a1 = QPushButton("지금까지 이런 맛은 없었다. 이것은 갈비인가 통닭인가", self)
        self.a1.setFont(QtGui.QFont("맑은 고딕", 16))
        self.a1.resize(800, 100)
        self.a1.move(40, 210)
        self.a1.clicked.connect(self.a_click)

        self.a2 = QPushButton("익스펙토 패트로눔 (… 해리포터)", self)
        self.a2.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a2.resize(800, 100)
        self.a2.move(40, 320)
        self.a2.clicked.connect(self.b_click)

        self.a3 = QPushButton("이거 방탄유리야", self)
        self.a3.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a3.resize(800, 100)
        self.a3.move(40, 430)
        self.a3.clicked.connect(self.c_click)

        self.a4 = QPushButton("나, 너 좋아하냐?", self)
        self.a4.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a4.resize(800, 100)
        self.a4.move(40, 540)
        self.a4.clicked.connect(self.d_click)

        self.test3_question3_window = Test3_Question3_Window(self)
    def a_click(self):
        self.test3_question3_window.show()
        self.test3_question3_window.name.setText(self.name.text())

        sql = "UPDATE my_movie_Test SET comedy = comedy + 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print("점수 추가 완료")

        if self.label.text() == "Which movie suits me?":
            self.test3_question3_window.label.setText("Which movie suits me?")
            self.test3_question3_window.q1.setText("What if I appear in a movie?")
            self.test3_question3_window.a1.setText("The bullet never hits me, and I never die.")
            self.test3_question3_window.a2.setText("I feel like someone's whispering to me all the time.")
            self.test3_question3_window.a3.setText("Are you sick? I'm sick, too.")
            self.test3_question3_window.a4.setText("Tada Tada Tada Tada")
        elif self.label.text() == "私似合う映画は？":
            self.test3_question3_window.label.setText("私似合う映画は？")
            self.test3_question3_window.q1.setText("映画に出たらどうするんですか？")
            self.test3_question3_window.a1.setText("銃弾は決して私に当たらず、私は決して死なない。")
            self.test3_question3_window.a2.setText("私は誰かがいつも私にささやいているような気がする。")
            self.test3_question3_window.a3.setText("痛いのか、僕も痛い。")
            self.test3_question3_window.a4.setText("タタタタタタタタ")
        self.hide()

    def b_click(self):
        self.test3_question3_window.show()
        self.test3_question3_window.name.setText(self.name.text())

        sql = "UPDATE my_movie_Test SET fantasy = fantasy + 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print("점수 추가 완료")

        if self.label.text() == "Which movie suits me?":
            self.test3_question3_window.label.setText("Which movie suits me?")
            self.test3_question3_window.q1.setText("What if I appear in a movie?")
            self.test3_question3_window.a1.setText("The bullet never hits me, and I never die.")
            self.test3_question3_window.a2.setText("I feel like someone's whispering to me all the time.")
            self.test3_question3_window.a3.setText("Are you sick? I'm sick, too.")
            self.test3_question3_window.a4.setText("Tada Tada Tada Tada")
        elif self.label.text() == "私似合う映画は？":
            self.test3_question3_window.label.setText("私似合う映画は？")
            self.test3_question3_window.q1.setText("映画に出たらどうするんですか？")
            self.test3_question3_window.a1.setText("銃弾は決して私に当たらず、私は決して死なない。")
            self.test3_question3_window.a2.setText("私は誰かがいつも私にささやいているような気がする。")
            self.test3_question3_window.a3.setText("痛いのか、僕も痛い。")
            self.test3_question3_window.a4.setText("タタタタタタタタ")
        self.hide()

    def c_click(self):
        self.test3_question3_window.show()
        self.test3_question3_window.name.setText(self.name.text())

        sql = "UPDATE my_movie_Test SET action = action + 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print("점수 추가 완료")

        if self.label.text() == "Which movie suits me?":
            self.test3_question3_window.label.setText("Which movie suits me?")
            self.test3_question3_window.q1.setText("What if I appear in a movie?")
            self.test3_question3_window.a1.setText("The bullet never hits me, and I never die.")
            self.test3_question3_window.a2.setText("I feel like someone's whispering to me all the time.")
            self.test3_question3_window.a3.setText("Are you sick? I'm sick, too.")
            self.test3_question3_window.a4.setText("Tada Tada Tada Tada")
        elif self.label.text() == "私似合う映画は？":
            self.test3_question3_window.label.setText("私似合う映画は？")
            self.test3_question3_window.q1.setText("映画に出たらどうするんですか？")
            self.test3_question3_window.a1.setText("銃弾は決して私に当たらず、私は決して死なない。")
            self.test3_question3_window.a2.setText("私は誰かがいつも私にささやいているような気がする。")
            self.test3_question3_window.a3.setText("痛いのか、僕も痛い。")
            self.test3_question3_window.a4.setText("タタタタタタタタ")
        self.hide()

    def d_click(self):
        self.test3_question3_window.show()
        self.test3_question3_window.name.setText(self.name.text())

        sql = "UPDATE my_movie_Test SET romance = romance + 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print("점수 추가 완료")

        if self.label.text() == "Which movie suits me?":
            self.test3_question3_window.label.setText("Which movie suits me?")
            self.test3_question3_window.q1.setText("What if I appear in a movie?")
            self.test3_question3_window.a1.setText("The bullet never hits me, and I never die.")
            self.test3_question3_window.a2.setText("I feel like someone's whispering to me all the time.")
            self.test3_question3_window.a3.setText("Are you sick? I'm sick, too.")
            self.test3_question3_window.a4.setText("Tada Tada Tada Tada")
        elif self.label.text() == "私似合う映画は？":
            self.test3_question3_window.label.setText("私似合う映画は？")
            self.test3_question3_window.q1.setText("映画に出たらどうするんですか？")
            self.test3_question3_window.a1.setText("銃弾は決して私に当たらず、私は決して死なない。")
            self.test3_question3_window.a2.setText("私は誰かがいつも私にささやいているような気がする。")
            self.test3_question3_window.a3.setText("痛いのか、僕も痛い。")
            self.test3_question3_window.a4.setText("タタタタタタタタ")
        self.hide()
