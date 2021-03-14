import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
from test2_question3_window import Test2_Question3_Window
from result2_window import Result_Window
sys.setrecursionlimit(10000)

class Test2_Question2_Window(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('사람에 관한 당신의 심리 상태')
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.resize(880, 500)

        back = QLabel("", self)
        back.resize(880, 500)
        back.move(0, 0)
        back.setStyleSheet('image:url(./image/background.png); border:0px;')

        # 질문 1 답 저장
        self.t = QLabel("", self)
        self.t.resize(0,0)
        self.t.move(0,0)

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

        self.label = QLabel("         의 사람에 관한 심리 상태는?", self)
        self.label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.label.resize(800, 60)
        self.label.move(40, 100)

        #질문
        self.q1 = QLabel("길을 걷던 도중 당신 앞에 벌레가 나타났습니다. 몇 마리일까요?", self)
        self.q1.setFont(QtGui.QFont("맑은 고딕", 15))
        self.q1.resize(800, 60)
        self.q1.move(30, 140)

        #답 버튼
        # 답 입력받기
        self.answer = QLineEdit("", self)
        self.answer.setFont(QtGui.QFont("맑은 고딕", 20))
        self.answer.setStyleSheet("overflow-x:hidden;" "overflow-y:hidden")
        self.answer.resize(800, 100)
        self.answer.move(40, 210)

        self.a = QPushButton("Next", self)
        self.a.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a.resize(800, 100)
        self.a.move(40, 320)
        self.a.clicked.connect(self.a_click)

        self.test2_question3_window = Test2_Question3_Window(self)
        self.result2_window = Result_Window(self)

    def a_click(self):
        self.test2_question3_window.show()
        user_name = self.name_label.text()

        self.test2_question3_window.name_label.setText(user_name)
        self.test2_question3_window.t.setText(self.t.text())
        self.test2_question3_window.t2.setText(self.answer.text())

        print(user_name, ">>> 길을 걷던 도중 당신 앞에 벌레가 나타났습니다. 몇 마리일까요? >>> ", self.answer.text())

        if self.label.text() == "         is state of mind these days":
            self.test2_question3_window.label.setText("         is state of mind these days")
            self.test2_question3_window.q1.setText("You went into the clothing store to buy clothes. How many customers are there in the store?")
        elif self.label.text() == "最近の僕の心理状態。":
            self.test2_question3_window.label.setText("最近の僕の心理状態。")
            self.test2_question3_window.q1.setText("あなたは服を買いに服屋に入りました。 服屋にお客さんが何人いるでしょうか。")
        self.hide()

