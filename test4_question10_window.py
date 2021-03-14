import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
from result4_window import Result_Window

# mysql ##################################
cnx = mysql.connector.connect(
    user = "root",
    password = "sori0927",
    host = "127.0.0.1",
    port = 3306,
    database = "test_zip"
)

cursor = cnx.cursor()

class Test4_Question10_Window(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('신조어 테스트')
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
        self.name_label = QLabel("봉봉", self)
        self.name_label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.name_label.resize(80, 60)
        self.name_label.move(40, 100)

        self.label = QLabel("         은(는) 요즘 시대를 잘 따라가고 있는가?", self)
        self.label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.label.resize(800, 60)
        self.label.move(40, 100)

        #질문
        self.q1 = QLabel("고독하고만", self)
        self.q1.setFont(QtGui.QFont("맑은 고딕", 26))
        self.q1.resize(800, 60)
        self.q1.move(30, 140)

        #답 버튼
        self.a1 = QPushButton("무슨 뜻인지 안다.", self)
        self.a1.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a1.resize(800, 100)
        self.a1.move(40, 210)
        self.a1.clicked.connect(self.a_click)

        self.a2 = QPushButton("무슨 뜻인지 모른다.", self)
        self.a2.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a2.resize(800, 100)
        self.a2.move(40, 320)
        self.a2.clicked.connect(self.b_click)

        self.result4_window = Result_Window(self)

    def a_click(self):
        self.result4_window.show()
        user_name = self.name_label.text()
        self.result4_window.name_label.setText(user_name)

        sql = "UPDATE my_neologism_test SET calculate = calculate + 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print(user_name, ">>>점수 추가 완료")
        # print(self.name_label.text() + " : b 선택")

        sql = "SELECT calculate from my_neologism_test WHERE result = 0;"
        cursor.execute(sql)
        calculate = cursor.fetchmany(1)

        sum = str(calculate)
        print(sum[2:-3])

        cnx.commit()

        cal = int(sum[2:-3])

        result_save = "update my_neologism_test set result = %s where calculate>=%s and calculate<=%s"

        if cal >= 71 and cal <= 100 :
            result = "급식충"
        elif cal >= 41 and cal <= 70 :
            result = "일반인"
        elif cal >= 21 and cal <= 40:
            result = "아재"
        elif cal >= 0 and cal <= 20 :
            result = "고인물"

        print("결과>>>", result)

        if result == "급식충":
            cursor.execute(result_save, ("급식충", 71, 100))
            self.result4_window.url_label.setText('https://ifh.cc/g/j32VEo.jpg')
            self.result4_window.result_img.setStyleSheet('image:url(./image/급식충.png); border:0px;')
        elif result == "일반인":
            cursor.execute(result_save, ("일반인", 41, 70))
            self.result4_window.url_label.setText('https://ifh.cc/g/kPgcup.jpg')
            self.result4_window.result_img.setStyleSheet('image:url(./image/일반인.png); border:0px;')
        elif result == "아재":
            cursor.execute(result_save, ("아재", 21, 40))
            self.result4_window.url_label.setText('https://ifh.cc/g/LKd1eQ.jpg')
            self.result4_window.result_img.setStyleSheet('image:url(./image/아재.png); border:0px;')
        elif result == "고인물":
            cursor.execute(result_save, ("고인물", 0, 20))
            self.result4_window.url_label.setText('https://ifh.cc/g/VDgFKO.jpg')
            self.result4_window.result_img.setStyleSheet('image:url(./image/고인물.png); border:0px;')

        cnx.commit()
        self.hide()


    def b_click(self):
        self.result4_window.show()
        user_name = self.name_label.text()
        self.result4_window.name_label.setText(user_name)

        print(user_name, ">>>점수 추가 완료")
        # print(self.name_label.text() + " : b 선택")

        sql = "SELECT calculate from my_neologism_test WHERE result = 0;"
        cursor.execute(sql)
        calculate = cursor.fetchmany(1)

        sum = str(calculate)
        print(sum[2:-3])

        cnx.commit()

        cal = int(sum[2:-3])

        result_save = "update my_neologism_test set result = %s where calculate>=%s and calculate<=%s"

        if cal >= 71 and cal <= 100 :
            result = "급식충"
        elif cal >= 41 and cal <= 70 :
            result = "일반인"
        elif cal >= 21 and cal <= 40:
            result = "아재"
        elif cal >= 0 and cal <= 20 :
            result = "고인물"

        print("결과>>>", result)

        if result == "급식충":
            cursor.execute(result_save, ("급식충", 71, 100))
            self.result4_window.url_label.setText('https://ifh.cc/g/j32VEo.jpg')
            self.result4_window.result_img.setStyleSheet('image:url(./image/급식충.png); border:0px;')
        elif result == "일반인":
            cursor.execute(result_save, ("일반인", 41, 70))
            self.result4_window.url_label.setText('https://ifh.cc/g/kPgcup.jpg')
            self.result4_window.result_img.setStyleSheet('image:url(./image/일반인.png); border:0px;')
        elif result == "아재":
            cursor.execute(result_save, ("아재", 21, 40))
            self.result4_window.url_label.setText('https://ifh.cc/g/LKd1eQ.jpg')
            self.result4_window.result_img.setStyleSheet('image:url(./image/아재.png); border:0px;')
        elif result == "고인물":
            cursor.execute(result_save, ("고인물", 0, 20))
            self.result4_window.url_label.setText('https://ifh.cc/g/VDgFKO.jpg')
            self.result4_window.result_img.setStyleSheet('image:url(./image/고인물.png); border:0px;')

        cnx.commit()
        self.hide()