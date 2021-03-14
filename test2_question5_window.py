import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
from result2_window import Result_Window

class Test2_Question5_Window(QtWidgets.QMainWindow, QPushButton):
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
        self.t.resize(0, 0)
        self.t.move(0, 0)

        # 질문 2 답 저장
        self.t2 = QLabel("", self)
        self.t2.resize(0, 0)
        self.t2.move(0, 0)

        # 질문 3 답 저장
        self.t3 = QLabel("", self)
        self.t3.resize(0, 0)
        self.t3.move(0, 0)

        # 질문 4 답 저장
        self.t4 = QLabel("", self)
        self.t4.resize(0, 0)
        self.t4.move(0, 0)

        # 로고
        logo = QLabel("", self)
        logo.resize(100, 50)
        logo.move(30, 30)
        logo.setStyleSheet('image:url(./image/logo.png); border:0px;')

        # 테스트 이름
        self.name_label = QLabel("봉봉", self)
        self.name_label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.name_label.resize(80, 60)
        self.name_label.move(40, 100)

        self.label = QLabel("         의 사람에 관한 심리 상태는?", self)
        self.label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.label.resize(800, 60)
        self.label.move(40, 100)

        #질문
        self.q1 = QLabel("온통 검은색인 방을 보았을 때 당신의 첫 느낌은?", self)
        self.q1.setFont(QtGui.QFont("맑은 고딕", 18))
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

        self.result2_window = Result_Window(self)

    def a_click(self):
        self.result2_window.show()
        user_name = self.name_label.text()
        self.result2_window.name_label.setText(user_name)
        self.result2_window.answer1.setText(self.t.text())
        self.result2_window.answer2.setText(self.t2.text())
        self.result2_window.answer3.setText(self.t3.text())
        self.result2_window.answer4.setText(self.t4.text())
        self.result2_window.answer5.setText(self.answer.text())

        print(user_name, ">>> 온통 검은색인 방을 보았을 때 당신의 첫 느낌은? >>> ", self.answer.text())
        # print(self.name_label.text() + " : b 선택")
        self.hide()