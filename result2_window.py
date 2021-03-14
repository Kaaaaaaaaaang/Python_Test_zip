import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
import home_window

class Result_Window(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('사람에 관한 당신의 심리 상태')
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resize(1100, 800)

        # 테스트 이름
        self.name_label = QLabel("봉봉", self)
        self.name_label.resize(0, 0)
        self.name_label.move(0, 0)

        # 로고
        logo = QPushButton("", self)
        logo.resize(100, 50)
        logo.move(30, 30)
        logo.toggle()
        logo.setToolTip("Home")
        logo.setStyleSheet('image:url(./image/logo.png); border:0px;')
        logo.clicked.connect(self.btn_Start)

        # 테스트 결과
        self.result_name = QLabel("", self)
        self.result_name.setFont(QtGui.QFont("맑은 고딕", 26))
        self.result_name.resize(800, 60)
        self.result_name.move(60, 100)


        # 테스트 결과 이미지
        self.result_img = QLabel("", self)
        self.result_img.resize(400, 500)
        self.result_img.setStyleSheet('image:url(./image/result2.png); border:0px;')
        self.result_img.move(70, 180)
        #self.result_img.setStyleSheet('image:url(./image/FullStack.png); border:0px;')

        # 테스트 결과 내용
        self.result1_text = QLabel("1. TV를 틀었을 때 화면에 나온 사람은?", self)
        self.result1_text.setFont(QtGui.QFont("맑은 고딕", 12))
        self.result1_text.resize(530, 40)
        self.result1_text.move(500, 180)

        self.result1 = QLabel("→ 당신은   _____    (을)를 닮고 싶어 합니다", self)
        self.result1.setFont(QtGui.QFont("맑은 고딕", 12))
        self.result1.resize(530, 40)
        self.result1.move(500, 220)

        self.answer1 = QLabel("강소리", self)
        self.answer1.setFont(QtGui.QFont("맑은 고딕", 12))
        self.answer1.setStyleSheet("color: red;")
        self.answer1.resize(75, 40)
        self.answer1.move(600, 220)


        self.result2_text = QLabel("2. 길을 걷던 도중 당신 앞에 벌레가 나타났습니다.\n   몇 마리일까요?", self)
        self.result2_text.setFont(QtGui.QFont("맑은 고딕", 12))
        self.result2_text.resize(530, 50)
        self.result2_text.move(500, 270)

        self.result2 = QLabel("→ 현재 당신을 화나게 하는 사람 수는  ____  명입니다.", self)
        self.result2.setFont(QtGui.QFont("맑은 고딕", 12))
        self.result2.resize(530, 40)
        self.result2.move(500, 320)

        self.answer2 = QLabel("300", self)
        self.answer2.setFont(QtGui.QFont("맑은 고딕", 12))
        self.answer2.setStyleSheet("color: red;")
        self.answer2.resize(45, 40)
        self.answer2.move(850, 320)


        self.result3_text = QLabel("3. 옷을 사러 옷가게를 들어갔습니다.\n   옷가게에 손님이 몇 명 있을까요?", self)
        self.result3_text.setFont(QtGui.QFont("맑은 고딕", 12))
        self.result3_text.resize(530, 50)
        self.result3_text.move(500, 370)

        self.result3 = QLabel("→ 당신이 결혼 전 사귀게 되는 애인의 수는  ___   명입니다.", self)
        self.result3.setFont(QtGui.QFont("맑은 고딕", 12))
        self.result3.resize(530, 40)
        self.result3.move(500, 420)

        self.answer3 = QLabel("300", self)
        self.answer3.setFont(QtGui.QFont("맑은 고딕", 12))
        self.answer3.setStyleSheet("color: red;")
        self.answer3.resize(45, 40)
        self.answer3.move(900, 420)


        self.result4_text = QLabel("4. 시험을 보러 가기 위해 가방을 싸고 있습니다.\n   연필을 몇 자루 챙겨갈 생각인가요?", self)
        self.result4_text.setFont(QtGui.QFont("맑은 고딕", 12))
        self.result4_text.resize(530, 50)
        self.result4_text.move(500, 470)

        self.result4 = QLabel("→ 당신의 진정한 친구는  ___  명이라고 생각합니다.", self)
        self.result4.setFont(QtGui.QFont("맑은 고딕", 12))
        self.result4.resize(530, 40)
        self.result4.move(500, 520)

        self.answer4 = QLabel("300", self)
        self.answer4.setFont(QtGui.QFont("맑은 고딕", 12))
        self.answer4.setStyleSheet("color: red;")
        self.answer4.resize(45, 40)
        self.answer4.move(725, 520)


        self.result5_text = QLabel("5. 당신은 온통 검은색인 방을 보았을 때\n   당신의 첫 느낌은 무엇인가요?", self)
        self.result5_text.setFont(QtGui.QFont("맑은 고딕", 12))
        self.result5_text.resize(530, 50)
        self.result5_text.move(500, 570)

        self.result5 = QLabel("→ ____       은(는) 당신이 죽을 때 들게 될 느낌입니다.", self)
        self.result5.setFont(QtGui.QFont("맑은 고딕", 12))
        self.result5.resize(530, 40)
        self.result5.move(500, 620)

        self.answer5 = QLabel("깨르륵", self)
        self.answer5.setFont(QtGui.QFont("맑은 고딕", 12))
        self.answer5.setStyleSheet("color: red;")
        self.answer5.resize(75, 40)
        self.answer5.move(525, 620)

        #저장하기 버튼 ( 결과 공유 대체 )
        save = QPushButton("result save", self)
        save.resize(150, 50)
        save.move(900, 100)
        save.toggle()
        save.clicked.connect(self.save_result)

    def btn_Start(self):
        self.start = home_window.Home_Window(self)
        self.start.show()
        self.hide()

    def save_result(self):
        url = self.url_label.text()
        urllib.request.urlretrieve(url,'./image_result/' + self.name_label.text() + '_result.png')
        print(self.name_label.text() + "_result.png" + " : 저장")
