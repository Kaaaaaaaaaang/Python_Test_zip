import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui
from home_window import Home_Window

class MainWindow(QtWidgets.QMainWindow, QPushButton):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Test.zip')
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resize(1100,800)

        star = QPushButton("", self)
        star.setFont(QtGui.QFont("맑은 고딕", 40))
        star.resize(1100, 800)
        star.move(0, 0)
        star.clicked.connect(self.btn_Start)
        star.setStyleSheet('image:url(./image/Start2.png); border:0px;')

        self.start = Home_Window(self)

    def btn_Start(self):
        self.start.show()
        self.hide()

    def shows(self):
        super().show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.shows()
    sys.exit(app.exec_())
