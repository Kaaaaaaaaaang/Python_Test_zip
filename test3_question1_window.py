import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
from test3_question2_window import Test3_Question2_Window

# mysql ##################################
cnx = mysql.connector.connect(
    user = "root",
    password = "sori0927",
    host = "127.0.0.1",
    port = 3306,
    database = "test_zip"
)

cursor = cnx.cursor()

class Test3_Question1_Window(QtWidgets.QMainWindow, QPushButton):
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
        self.q1 = QLabel("선호하는 장르는?", self)
        self.q1.setFont(QtGui.QFont("맑은 고딕", 26))
        self.q1.resize(800, 60)
        self.q1.move(40, 140)

        #답 버튼
        self.a1 = QPushButton("로맨스", self)
        self.a1.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a1.resize(800, 100)
        self.a1.move(40, 210)
        self.a1.clicked.connect(self.a_click)

        self.a2 = QPushButton("판타지", self)
        self.a2.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a2.resize(800, 100)
        self.a2.move(40, 320)
        self.a2.clicked.connect(self.b_click)

        self.a3 = QPushButton("액션", self)
        self.a3.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a3.resize(800, 100)
        self.a3.move(40, 430)
        self.a3.clicked.connect(self.c_click)

        self.a4 = QPushButton("코미디", self)
        self.a4.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a4.resize(800, 100)
        self.a4.move(40, 540)
        self.a4.clicked.connect(self.d_click)

        self.test3_question2_window = Test3_Question2_Window(self)

    def a_click(self):
        self.test3_question2_window.show()
        self.test3_question2_window.name.setText(self.name.text())

        sql = "UPDATE my_movie_Test SET romance = 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print("점수 추가 완료")

        if self.label.text() == "Which movie suits me?":
            self.test3_question2_window.label.setText("Which movie suits me?")
            self.test3_question2_window.q1.setText("What is the most memorable line?")
            self.test3_question2_window.a1.setText("It has never tasted like this before. Is this galbi or fried chicken?")
            self.test3_question2_window.a2.setText("Expecto Petronum")
            self.test3_question2_window.a3.setText("This is bulletproof glass!!!!!!!!")
            self.test3_question2_window.a4.setText("Do I like you?")
        elif self.label.text() == "私似合う映画は？":
            self.test3_question2_window.label.setText("私似合う映画は？")
            self.test3_question2_window.q1.setText("一番記憶に残ってるセリフは何ですか？")
            self.test3_question2_window.a1.setText("これまでこんな味はなかった。 これはカルビかチキンか")
            self.test3_question2_window.a2.setText("エクスペクト·ペトロヌム")
            self.test3_question2_window.a3.setText("これは防弾ガラスです!!!!!!!")
            self.test3_question2_window.a4.setText("私はあなたが好きですか？")
        self.hide()

    def b_click(self):
        self.test3_question2_window.show()
        self.test3_question2_window.name.setText(self.name.text())

        sql = "UPDATE my_movie_Test SET fantasy = 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print("점수 추가 완료")

        if self.label.text() == "Which movie suits me?":
            self.test3_question2_window.label.setText("Which movie suits me?")
            self.test3_question2_window.q1.setText("What is the most memorable line?")
            self.test3_question2_window.a1.setText("It has never tasted like this before. Is this galbi or fried chicken?")
            self.test3_question2_window.a2.setText("Expecto Petronum")
            self.test3_question2_window.a3.setText("This is bulletproof glass!!!!!!!!")
            self.test3_question2_window.a4.setText("Do I like you?")
        elif self.label.text() == "私似合う映画は？":
            self.test3_question2_window.label.setText("私似合う映画は？")
            self.test3_question2_window.q1.setText("一番記憶に残ってるセリフは何ですか？")
            self.test3_question2_window.a1.setText("これまでこんな味はなかった。 これはカルビかチキンか")
            self.test3_question2_window.a2.setText("エクスペクト·ペトロヌム")
            self.test3_question2_window.a3.setText("これは防弾ガラスです!!!!!!!")
            self.test3_question2_window.a4.setText("私はあなたが好きですか？")
        self.hide()

    def c_click(self):
        self.test3_question2_window.show()
        self.test3_question2_window.name.setText(self.name.text())

        sql = "UPDATE my_movie_Test SET action = 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print("점수 추가 완료")

        if self.label.text() == "Which movie suits me?":
            self.test3_question2_window.label.setText("Which movie suits me?")
            self.test3_question2_window.q1.setText("What is the most memorable line?")
            self.test3_question2_window.a1.setText("It has never tasted like this before. Is this galbi or fried chicken?")
            self.test3_question2_window.a2.setText("Expecto Petronum")
            self.test3_question2_window.a3.setText("This is bulletproof glass!!!!!!!!")
            self.test3_question2_window.a4.setText("Do I like you?")
        elif self.label.text() == "私似合う映画は？":
            self.test3_question2_window.label.setText("私似合う映画は？")
            self.test3_question2_window.q1.setText("一番記憶に残ってるセリフは何ですか？")
            self.test3_question2_window.a1.setText("これまでこんな味はなかった。 これはカルビかチキンか")
            self.test3_question2_window.a2.setText("エクスペクト·ペトロヌム")
            self.test3_question2_window.a3.setText("これは防弾ガラスです!!!!!!!")
            self.test3_question2_window.a4.setText("私はあなたが好きですか？")
        self.hide()

    def d_click(self):
        self.test3_question2_window.show()
        self.test3_question2_window.name.setText(self.name.text())

        sql = "UPDATE my_movie_Test SET comedy = 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print("점수 추가 완료")

        if self.label.text() == "Which movie suits me?":
            self.test3_question2_window.label.setText("Which movie suits me?")
            self.test3_question2_window.q1.setText("What is the most memorable line?")
            self.test3_question2_window.a1.setText("It has never tasted like this before. Is this galbi or fried chicken?")
            self.test3_question2_window.a2.setText("Expecto Petronum")
            self.test3_question2_window.a3.setText("This is bulletproof glass!!!!!!!!")
            self.test3_question2_window.a4.setText("Do I like you?")
        elif self.label.text() == "私似合う映画は？":
            self.test3_question2_window.label.setText("私似合う映画は？")
            self.test3_question2_window.q1.setText("一番記憶に残ってるセリフは何ですか？")
            self.test3_question2_window.a1.setText("これまでこんな味はなかった。 これはカルビかチキンか")
            self.test3_question2_window.a2.setText("エクスペクト·ペトロヌム")
            self.test3_question2_window.a3.setText("これは防弾ガラスです!!!!!!!")
            self.test3_question2_window.a4.setText("私はあなたが好きですか？")
        self.hide()

