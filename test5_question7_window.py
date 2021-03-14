import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
from result5_window import Result_Window

# mysql ##################################
cnx = mysql.connector.connect(
    user="root",
    password="sori0927",
    host="127.0.0.1",
    port=3306,
    database="test_zip"
)

cursor = cnx.cursor()


class Test5_Question7_Window(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('연애세포 생존 테스트')
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

        self.label = QLabel("         의 연애세포는 살아있는가?", self)
        self.label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.label.resize(800, 60)
        self.label.move(40, 100)

        # 질문
        self.q1 = QLabel("아무 약속 없이 집에 있는 날이 가장 좋다. ", self)
        self.q1.setFont(QtGui.QFont("맑은 고딕", 22))
        self.q1.resize(800, 60)
        self.q1.move(30, 140)

        # 답 버튼
        self.a1 = QPushButton("O", self)
        self.a1.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a1.resize(800, 100)
        self.a1.move(40, 210)
        self.a1.clicked.connect(self.a_click)

        self.a2 = QPushButton("X", self)
        self.a2.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a2.resize(800, 100)
        self.a2.move(40, 320)
        self.a2.clicked.connect(self.b_click)

        self.result5_window = Result_Window(self)

    def a_click(self):
        self.result5_window.show()
        user_name = self.name_label.text()
        self.result5_window.name_label.setText(user_name)

        print(user_name, ">>>점수 추가 완료")
        # print(self.name_label.text() + " : b 선택")

        sql = "SELECT calculate from lovesurvival_test WHERE result = 0;"
        cursor.execute(sql)
        calculate = cursor.fetchmany(1)

        sum = str(calculate)
        print(sum[2:-3])

        cnx.commit()

        cal = int(sum[2:-3])

        result_save = "update lovesurvival_test set result = %s where calculate>=%s and calculate<=%s"

        if cal >= 51 and cal <= 70:
            result = "연애 세포 생존"
            if self.label.text() == "         's Love Cell Survival Test":
                result = "생존영어"
            elif self.label.text() == "         恋愛細胞生存テスト":
                result = "생존일본어"
            cursor.execute(result_save, ("연애 세포 생존", 51, 70))
        elif cal >= 31 and cal <= 50:
            result = "연애 세포 위험"
            if self.label.text() == "         's Love Cell Survival Test":
                result = "위험영어"
            elif self.label.text() == "         恋愛細胞生存テスト":
                result = "위험일본어"
            cursor.execute(result_save, ("연애 세포 위험", 31, 50))
        elif cal >= 0 and cal <= 30:
            result = "연애 세포 소멸"
            if self.label.text() == "         's Love Cell Survival Test":
                result = "소멸영어"
            elif self.label.text() == "         恋愛細胞生存テスト":
                result = "소멸일본어"
            cursor.execute(result_save, ("연애 세포 소멸", 0, 30))

        print("결과>>>", result)
        if result == "연애 세포 생존" :
            self.result5_window.url_label.setText('https://ifh.cc/g/gNc6PA.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/연애세포생존.png); border:0px;')
        elif result == "생존영어" :
            self.result5_window.url_label.setText('https://ifh.cc/g/OeWIJ6.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/survival.png); border:0px;')
        elif result == "생존일본어" :
            self.result5_window.url_label.setText('https://ifh.cc/g/Jp64Jd.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/연애세포생존_일본어.png); border:0px;')

        elif result == "연애 세포 위험" :
            self.result5_window.url_label.setText('https://ifh.cc/g/7WqmQp.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/연애세포위험.png); border:0px;')
        elif result == "위험영어" :
            self.result5_window.url_label.setText('https://ifh.cc/g/X4HzIU.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/danger.png); border:0px;')
        elif result == "위험일본어" :
            self.result5_window.url_label.setText('https://ifh.cc/g/i4t579.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/연애세포위험_일본어.png); border:0px;')

        elif result == "연애 세포 소멸" :
            self.result5_window.url_label.setText('https://ifh.cc/g/F2xynj.png')
            self.result5_window.result_img.setStyleSheet('image:url(./image/연애세포소멸.png); border:0px;')
        elif result == "소멸영어" :
            self.result5_window.url_label.setText('https://ifh.cc/g/rKOrvz.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/extinction.png); border:0px;')
        elif result == "소멸일본어" :
            self.result5_window.url_label.setText('https://ifh.cc/g/AkSbAY.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/연애세포소멸_일본어.png); border:0px;')

        cnx.commit()

        self.hide()


    def b_click(self):
        self.result5_window.show()
        user_name = self.name_label.text()
        self.result5_window.name_label.setText(user_name)

        sql = "UPDATE lovesurvival_test SET calculate = calculate + 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print(user_name, ">>>점수 추가 완료")
        # print(self.name_label.text() + " : b 선택")

        sql = "SELECT calculate from lovesurvival_test WHERE result = 0;"
        cursor.execute(sql)
        calculate = cursor.fetchmany(1)

        sum = str(calculate)
        print(sum[2:-3])

        cnx.commit()

        cal = int(sum[2:-3])

        result_save = "update lovesurvival_test set result = %s where calculate>=%s and calculate<=%s"

        if cal >= 51 and cal <= 70:
            result = "연애 세포 생존"
            if self.label.text() == "         's Love Cell Survival Test":
                result = "생존영어"
            elif self.label.text() == "         恋愛細胞生存テスト":
                result = "생존일본어"
            cursor.execute(result_save, ("연애 세포 생존", 51, 70))
        elif cal >= 31 and cal <= 50:
            result = "연애 세포 위험"
            if self.label.text() == "         's Love Cell Survival Test":
                result = "위험영어"
            elif self.label.text() == "         恋愛細胞生存テスト":
                result = "위험일본어"
            cursor.execute(result_save, ("연애 세포 위험", 31, 50))
        elif cal >= 0 and cal <= 30:
            result = "연애 세포 소멸"
            if self.label.text() == "         's Love Cell Survival Test":
                result = "소멸영어"
            elif self.label.text() == "         恋愛細胞生存テスト":
                result = "소멸일본어"
            cursor.execute(result_save, ("연애 세포 소멸", 0, 30))

        cnx.commit()

        print("결과>>>", result)

        if result == "연애 세포 생존" :
            self.result5_window.url_label.setText('https://ifh.cc/g/gNc6PA.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/연애세포생존.png); border:0px;')
        elif result == "생존영어" :
            self.result5_window.url_label.setText('https://ifh.cc/g/OeWIJ6.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/survival.png); border:0px;')
        elif result == "생존일본어" :
            self.result5_window.url_label.setText('https://ifh.cc/g/Jp64Jd.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/연애세포생존_일본어.png); border:0px;')

        elif result == "연애 세포 위험" :
            self.result5_window.url_label.setText('https://ifh.cc/g/7WqmQp.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/연애세포위험.png); border:0px;')
        elif result == "위험영어" :
            self.result5_window.url_label.setText('https://ifh.cc/g/X4HzIU.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/danger.png); border:0px;')
        elif result == "위험일본어" :
            self.result5_window.url_label.setText('https://ifh.cc/g/i4t579.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/연애세포위험_일본어.png); border:0px;')

        elif result == "연애 세포 소멸" :
            self.result5_window.url_label.setText('https://ifh.cc/g/F2xynj.png')
            self.result5_window.result_img.setStyleSheet('image:url(./image/연애세포소멸.png); border:0px;')
        elif result == "소멸영어" :
            self.result5_window.url_label.setText('https://ifh.cc/g/rKOrvz.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/extinction.png); border:0px;')
        elif result == "소멸일본어" :
            self.result5_window.url_label.setText('https://ifh.cc/g/AkSbAY.jpg')
            self.result5_window.result_img.setStyleSheet('image:url(./image/연애세포소멸_일본어.png); border:0px;')
        # print(self.name_label.text() + " : b 선택")

        self.hide()