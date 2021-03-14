import sys
import urllib.request
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
import home_window

# mysql ##################################
cnx = mysql.connector.connect(
    user = "root",
    password = "sori0927",
    host = "127.0.0.1",
    port = 3306,
    database = "test_zip"
)

cursor = cnx.cursor()

class Result_Window(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('연애세포 생존 테스트')
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resize(1100, 800)

        # 테스트 이름
        self.name_label = QLabel("봉봉", self)
        self.name_label.resize(0, 0)
        self.name_label.move(0, 0)

        # 테스트 결과 이미지
        self.result_img = QLabel("", self)
        self.result_img.resize(1100, 800)
        self.result_img.move(0, 0)

        # 로고
        logo = QPushButton("", self)
        logo.resize(100, 50)
        logo.move(30, 10)
        logo.toggle()
        logo.setToolTip("Home")
        logo.setStyleSheet('image:url(./image/logo.png); border:0px;')
        logo.clicked.connect(self.btn_Start)

        #url 경로
        self.url_label = QLabel("", self)
        self.url_label.resize(0, 0)
        self.url_label.move(0, 0)

        #저장하기 버튼 ( 결과 공유 대체 )
        save = QPushButton("result save", self)
        save.resize(150, 50)
        save.move(900, 700)
        save.toggle()
        save.clicked.connect(self.save_result)


        self.deleteData()

    def btn_Start(self):
        self.start = home_window.Home_Window(self)
        self.start.show()
        self.hide()

    def save_result(self):
        url = self.url_label.text()
        urllib.request.urlretrieve(url,'./image_result/' + self.name_label.text() + '_result.png')
        print(self.name_label.text() + "_result.png" + " : 저장")

    def deleteData(self):
        sql = "TRUNCATE TABLE lovesurvival_test;"
        cursor.execute(sql)

        cnx.commit()
