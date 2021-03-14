import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
from result3_window import Result2_Window

# mysql ##################################
cnx = mysql.connector.connect(
    user = "root",
    password = "sori0927",
    host = "127.0.0.1",
    port = 3306,
    database = "test_zip"
)

cursor = cnx.cursor()


class Test3_Question5_Window(QtWidgets.QMainWindow, QPushButton):
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
        self.name = QLabel("봉봉", self)
        self.name.setFont(QtGui.QFont("맑은 고딕", 13))
        self.name.resize(80, 60)
        self.name.move(40, 100)

        self.label = QLabel("         와(과) 어울리는 영화는?", self)
        self.label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.label.resize(800, 60)
        self.label.move(40, 100)
        #질문
        self.q1 = QLabel("가장 행복한 결말은?", self)
        self.q1.setFont(QtGui.QFont("맑은 고딕", 26))
        self.q1.resize(800, 60)
        self.q1.move(40, 140)

        #답 버튼
        self.a1 = QPushButton("힘든 결투 끝에 살아 돌아가는 뒷모습", self)
        self.a1.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a1.resize(800, 100)
        self.a1.move(40, 210)
        self.a1.clicked.connect(self.a_click)

        self.a2 = QPushButton("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ", self)
        self.a2.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a2.resize(800, 100)
        self.a2.move(40, 320)
        self.a2.clicked.connect(self.b_click)

        self.a3 = QPushButton("오래오래 행복하게 살았답니다.", self)
        self.a3.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a3.resize(800, 100)
        self.a3.move(40, 430)
        self.a3.clicked.connect(self.c_click)

        self.a4 = QPushButton("모든 의문을 풀고 살게 된 새로운 인생", self)
        self.a4.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a4.resize(800, 100)
        self.a4.move(40, 540)
        self.a4.clicked.connect(self.d_click)

        self.result2_window = Result2_Window(self)
    def a_click(self):
        self.result2_window.show()
        self.result2_window.name_label.setText(self.name.text())

        sql = "UPDATE my_movie_Test SET action = action + 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print("점수 추가 완료")

        sql = "SELECT * from my_movie_Test WHERE result = 0;"
        cursor.execute(sql)
        result = cursor.fetchmany(1)

        print("결과 >>>" , result)

        self.result()

        self.hide()

    def b_click(self):
        self.result2_window.show()
        self.result2_window.name_label.setText(self.name.text())

        sql = "UPDATE my_movie_Test SET comedy = comedy + 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print("점수 추가 완료")

        sql = "SELECT * from my_movie_Test WHERE result = 0;"
        cursor.execute(sql)
        result = cursor.fetchmany(1)

        print("결과 >>>", result)

        self.result()

        self.hide()

    def c_click(self):
        self.result2_window.show()
        self.result2_window.name_label.setText(self.name.text())

        sql = "UPDATE my_movie_Test SET romance = romance + 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print("점수 추가 완료")

        sql = "SELECT * from my_movie_Test WHERE result = 0;"
        cursor.execute(sql)
        result = cursor.fetchmany(1)

        print("결과 >>>", result)

        self.result()

        self.hide()

    def d_click(self):
        self.result2_window.show()
        self.result2_window.name_label.setText(self.name.text())

        sql = "UPDATE my_movie_Test SET fantasy = fantasy + 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print("점수 추가 완료")

        self.result()

        self.hide()

    def result(self):
        sql = "SELECT romance from my_movie_Test WHERE result = 0;"
        cursor.execute(sql)
        result = cursor.fetchmany(1)

        romance_sum = str(result)

        romance = int(romance_sum[2:-3])

        print("로맨스>>>", romance)

        sql = "SELECT comedy from my_movie_Test WHERE result = 0;"
        cursor.execute(sql)
        result = cursor.fetchmany(1)

        comedy_sum = str(result)

        comedy = int(comedy_sum[2:-3])

        print("코미디>>>", comedy)

        sql = "SELECT fantasy from my_movie_Test WHERE result = 0;"
        cursor.execute(sql)
        result = cursor.fetchmany(1)

        fantasy_sum = str(result)

        fantasy = int(fantasy_sum[2:-3])

        print("판타지>>>", fantasy)

        sql = "SELECT action from my_movie_Test WHERE result = 0;"
        cursor.execute(sql)
        result = cursor.fetchmany(1)

        action_sum = str(result)

        action = int(action_sum[2:-3])

        print("액션>>>", action)

        if romance >= action and romance >= fantasy and romance >= comedy :
            if romance >= 30 :
                result = "나의 소녀시대"
                if self.label.text() == "Which movie suits me?":
                    result = "My girls' generation"
                elif self.label.text() == "私似合う映画は？":
                    result = "私少女時代"
            else :
                result = "너의 결혼식"
                if self.label.text() == "Which movie suits me?":
                    result = "Your wedding"
                elif self.label.text() == "私似合う映画は？":
                    result = "あなたの結婚式"
        elif action >= romance and action >= fantasy and action >= comedy :
            if action >= 30 :
                result = "어벤져스"
                if self.label.text() == "Which movie suits me?":
                    result = "Avenger's"
                elif self.label.text() == "私似合う映画は？":
                    result = "アベンジャーズ"
            else :
                result = "베테랑"
                if self.label.text() == "Which movie suits me?":
                    result = "veteran"
                elif self.label.text() == "私似合う映画は？":
                    result = "ベテラン"
        elif comedy >= romance and comedy >= action and comedy >= fantasy :
            if comedy >= 30 :
                result = "극한 직업"
                if self.label.text() == "Which movie suits me?":
                    result = "Extreme job"
                elif self.label.text() == "私似合う映画は？":
                    result = "極限の仕事"
            else :
                result = "청년 경찰"
                if self.label.text() == "Which movie suits me?":
                    result = "Youth police"
                elif self.label.text() == "私似合う映画は？":
                    result = "青年警察"
        elif fantasy >= romance and fantasy >= action and fantasy >= comedy :
            if fantasy >= 30 :
                result = "반지의 제왕"
                if self.label.text() == "Which movie suits me?":
                    result = "Lord of the rings"
                elif self.label.text() == "私似合う映画は？":
                    result = "ロードオブザリング"
            else :
                result = "해리포터"
                if self.label.text() == "Which movie suits me?":
                    result = "Harry Potter"
                elif self.label.text() == "私似合う映画は？":
                    result = "ハリー・ポッター"

        print("결과 >>>", result)
        self.result2_window.result_name.setText(result)
        if result == "나의 소녀시대":
            self.result2_window.url_label.setText("https://ifh.cc/g/WSFIBM.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/나의 소녀시대.png); border:0px;')
            self.result2_window.result_text.setText("혹시 감동적이고 슬픈 영화를 보며 눈물을 흘리는\n"
                                                    + "일이 빈번하지 않나요??\n\n"
                                                    + "당신은 타인의 감정에 쉽게 공감해주는 "
                                                    + "\n여린 감성을 가지고 있어요!!\n"
                                                    + "\n항상 타인의 의견을 경청하고, 공감해주는"
                                                    + "\n당신의 모습에 반하는 주변인들이 많답니다.\n"
                                                    + "\n감성이 풍부하고 사랑스러운 당신!"
                                                    + "\n어딜가든 사랑 받을 거에요♥♥\n"
                                                    + "\n당신은 영화 <나의 소녀시대>와 어울려요")
        elif result == "My girls' generation" :
            self.result2_window.url_label.setText("https://ifh.cc/g/WSFIBM.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/나의 소녀시대.png); border:0px;')
            self.result2_window.result_text.setText("Would you like to cry\n while watching a moving and sad movie"
                                                    + "Aren't things infrequent??\n\n"
                                                    + "You easily empathize with the feelings of others"
                                                    + "\nIt has a soft sensibility!!\n"
                                                    + "\nAlways listen to and sympathize with others' opinions"
                                                    + "\nThere are many people around you who fall in love with you.\n"
                                                    + "\nYou are rich and lovely!"
                                                    + "\nYou'll be loved wherever you go♥♥\n"
                                                    + "\nYou hang out with the movie <My Girls' Generation>")
        elif result == "私少女時代" :
            self.result2_window.url_label.setText("https://ifh.cc/g/WSFIBM.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/나의 소녀시대.png); border:0px;')
            self.result2_window.result_text.setText("「もしかしたら感動的、悲しい映画を見て涙を流す\n "
                                                    + "ことが頻繁にありませんか？\n\n"
                                                    + "あなたは他人の感情に簡単に共感してくれる"
                                                    + "\n弱い感性を持っています！\n"
                                                    + "\n常に他人の意見を聞き、共感してくれる"
                                                    + "\nあなたの姿に反する周りの人たちが多いんです。」\n"
                                                    + "\n感性が豊かで美しいあなた！"
                                                    + "\nどこへ行っ愛されるんですよ♥♥\n"
                                                    + "\nあなたは映画<私の少女時代>と似合い")

        elif result == "너의 결혼식":
            self.result2_window.url_label.setText("https://ifh.cc/g/wBB2vY.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/너의 결혼식.png); border:0px;')
            self.result2_window.result_text.setText("혹시 감동적이고 슬픈 영화를 보며 눈물을 흘리는\n"
                                                    + "일이 빈번하지 않나요??\n\n"
                                                    + "당신은 타인의 감정에 쉽게 공감해주는 "
                                                    + "\n여린 감성을 가지고 있어요!!\n"
                                                    + "\n항상 타인의 의견을 경청하고, 공감해주는"
                                                    + "\n당신의 모습에 반하는 주변인들이 많답니다.\n"
                                                    + "\n감성이 풍부하고 사랑스러운 당신!"
                                                    + "\n어딜가든 사랑 받을 거에요♥♥\n"
                                                    + "\n당신은 영화 <너의 결혼식>과 어울려요")
        elif result == "Your wedding":
            self.result2_window.url_label.setText("https://ifh.cc/g/wBB2vY.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/너의 결혼식.png); border:0px;')
            self.result2_window.result_text.setText("Would you like to cry\n while watching a moving and sad movie"
                                                    + "Aren't things infrequent??\n\n"
                                                    + "You easily empathize with the feelings of others"
                                                    + "\nIt has a soft sensibility!!\n"
                                                    + "\nAlways listen to and sympathize with others' opinions"
                                                    + "\nThere are many people around you who fall in love with you.\n"
                                                    + "\nYou are rich and lovely!"
                                                    + "\nYou'll be loved wherever you go♥♥\n"
                                                    + "\nYou hang out with the movie <Your Wedding>")
        elif result == "あなたの結婚式":
            self.result2_window.url_label.setText("https://ifh.cc/g/wBB2vY.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/너의 결혼식.png); border:0px;')
            self.result2_window.result_text.setText("「もしかしたら感動的、悲しい映画を見て涙を流す\n "
                                                    + "ことが頻繁にありませんか？\n\n"
                                                    + "あなたは他人の感情に簡単に共感してくれる"
                                                    + "\n弱い感性を持っています！\n"
                                                    + "\n常に他人の意見を聞き、共感してくれる"
                                                    + "\nあなたの姿に反する周りの人たちが多いんです。」\n"
                                                    + "\n感性が豊かで美しいあなた！"
                                                    + "\nどこへ行っ愛されるんですよ♥♥\n"
                                                    + "\nあなたは映画<あなたの結婚式>と似合い")

        elif result == "어벤져스":
            self.result2_window.url_label.setText("https://ifh.cc/g/ZFNdUh.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/어벤져스.png); border:0px;')
            self.result2_window.result_text.setText("이 유형과 잘 어울리는 영화는 빠밤 어벤져스!!\n"
                                                    + "화려한 액션이나 빠른 전개를 가진 영화를\n"
                                                    + "좋아하는 당신, 무료한 현실 속에서"
                                                    + "\n자극이 필요한가요?\n"
                                                    + "\n이 유형의 사람들은 시원시원하고 활동적인"
                                                    + "\n성격을 가지고 있어요! 세상 쿨한 당신!\n"
                                                    + "\n친구가 실수를 해도 쿨하게 용서해주고"
                                                    + "\n지나가는 대인배랍니다.\n"
                                                    + "\n뒤끝이 없으면서도 화끈한 성향 덕분에 당신의"
                                                    + "\n주변에는 항상 사람들이 모이는 군요!")
        elif result == "Avenger's":
            self.result2_window.url_label.setText("https://ifh.cc/g/ZFNdUh.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/어벤져스.png); border:0px;')
            self.result2_window.result_text.setText("A movie that goes well with this type is the Avengers!\n"
                                                    + "A movie with splendid action or rapid deployment\n"
                                                    + "You like, in a boring reality"
                                                    + "\nDo you need stimulation?\n"
                                                    + "\nthis type of people is cool and active"
                                                    + "\nYou have a personality! You are cool in the world!\n"
                                                    + "\nIf your friend makes a mistake, you coolly forgive it"
                                                    + "\nIt's a passing adult.\n"
                                                    + "\nThanks to your hotness without a back end"
                                                    + "\nPeople always gather around you!")
        elif result == "アベンジャーズ":
            self.result2_window.url_label.setText("https://ifh.cc/g/ZFNdUh.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/어벤져스.png); border:0px;')
            self.result2_window.result_text.setText("「このタイプのよく似合う映画はパバムオベンジョス!! \n "
                                                    + "派手なアクションや、高速展開の映画を\n"
                                                    + "好きなあなた、無料な現実の中で、「"
                                                    + "\n刺激が必要ですか？」\n"
                                                    + "\nこのタイプの人は爽やかで活動的な"
                                                    + "\n性格を持っています！世界クールあなた！\n"
                                                    + "\n友人がミスをしてもクールに許してくれ」"
                                                    + "\n通過デインベなんですよ。\n"
                                                    + "\nドィクトがないのにもホット性向のおかげで、あなたの"
                                                    + "\n周辺には常に人が集まるね！」")

        elif result == "베테랑":
            self.result2_window.url_label.setText("https://ifh.cc/g/8VjAPD.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/베테랑.png); border:0px;')
            self.result2_window.result_text.setText("이 유형과 잘 어울리는 영화는 빠밤 베테랑!!\n"
                                                    + "화려한 액션이나 빠른 전개를 가진 영화를\n"
                                                    + "좋아하는 당신, 무료한 현실 속에서"
                                                    + "\n자극이 필요한가요?\n"
                                                    + "\n이 유형의 사람들은 시원시원하고 활동적인"
                                                    + "\n성격을 가지고 있어요! 세상 쿨한 당신!\n"
                                                    + "\n친구가 실수를 해도 쿨하게 용서해주고"
                                                    + "\n지나가는 대인배랍니다.\n"
                                                    + "\n뒤끝이 없으면서도 화끈한 성향 덕분에 당신의"
                                                    + "\n주변에는 항상 사람들이 모이는 군요!")
        elif result == "veteran":
            self.result2_window.url_label.setText("https://ifh.cc/g/8VjAPD.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/베테랑.png); border:0px;')
            self.result2_window.result_text.setText("A movie that goes well with this type is a Veteran Pabam!!\n"
                                                    + "A movie with splendid action or rapid deployment\n"
                                                    + "You like, in a boring reality"
                                                    + "\nDo you need stimulation?\n"
                                                    + "\nthis type of people is cool and active"
                                                    + "\nYou have a personality! You are cool in the world!\n"
                                                    + "\nIf your friend makes a mistake, you coolly forgive it"
                                                    + "\nIt's a passing adult.\n"
                                                    + "\nThanks to your hotness without a back end"
                                                    + "\nPeople always gather around you!")
        elif result == "ベテラン":
            self.result2_window.url_label.setText("https://ifh.cc/g/8VjAPD.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/베테랑.png); border:0px;')
            self.result2_window.result_text.setText("「このタイプのよく似合う映画はパバムベテラン！\n "
                                                    + "派手なアクションや、高速展開の映画を\n"
                                                    + "好きなあなた、無料な現実の中で、「"
                                                    + "\n刺激が必要ですか？」\n"
                                                    + "\nこのタイプの人は爽やかで活動的な"
                                                    + "\n性格を持っています！世界クールあなた！\n"
                                                    + "\n友人がミスをしてもクールに許してくれ」"
                                                    + "\n通過デインベなんですよ。\n"
                                                    + "\nドィクトがないのにもホット性向のおかげで、あなたの"
                                                    + "\n周辺には常に人が集まるね！」")

        elif result == "극한 직업":
            self.result2_window.url_label.setText("https://ifh.cc/g/WSFIBM.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/극한 직업.png); border:0px;')
            self.result2_window.result_text.setText("일상이 코미디인 당신에게 딱 맞는 영화!!\n"
                                                    + "극한직업을 추천합니다!\n\n"
                                                    + "호기심 많고 언제나 활기찬 당신의 주변에는"
                                                    + "\n언제나 사람들이 모여있어요\n"
                                                    + "\n한 마디로 인싸 기질을 가진 당신!!\n"
                                                    + "\n사람들 사이에서 행복을 느끼기도 하지만"
                                                    + "\n사람들로부터 상처를 많이 받는 타입이에요 ㅠㅠ\n"
                                                    + "\n가끔은 혼자만의 시간을 가지는 것도 나쁘지 않아요"
                                                    + "\n혼자만의 시간을 가지면서 영화를 보는 건 어떨까요?")
        elif result == "Extreme job":
            self.result2_window.url_label.setText("https://ifh.cc/g/WSFIBM.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/극한 직업.png); border:0px;')
            self.result2_window.result_text.setText("A movie that's perfect for you, where everyday is a comedy!!\n"
                                                    + "I recommend an extreme job!\n\n"
                                                    + "Curious and always lively around you"
                                                    + "\nPeople are always gathered\n"
                                                    + "\nIn a word, you have an insider temperament!!\n"
                                                    + "\nAlthough I feel happiness among people"
                                                    + "\nI'm the type that gets hurt a lot from people ㅠㅠ\n"
                                                    + "\nIt's not bad to have time alone sometimes"
                                                    + "\nHow about watching a movie while having your own time?")
        elif result == "極限の仕事":
            self.result2_window.url_label.setText("https://ifh.cc/g/WSFIBM.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/극한 직업.png); border:0px;')
            self.result2_window.result_text.setText("「日常がコメディであるあなたにぴったりの映画！\n "
                                                    + "極限の仕事をお勧めします！\n\n"
                                                    + "好奇心はいつも活気に満ちたあなたの周りには"
                                                    + "\nいつも人が集まっています\n"
                                                    + "\n一言でインサ気質のあなた!!」\n"
                                                    + "\n人々の間で幸せを感じることもあるが、「"
                                                    + "\n人々から多くの傷を受けるタイプです〓〓\n"
                                                    + "\n時には一人だけの時間を持つのも悪くありません"
                                                    + "\n一人だけの時間を持ちながら映画を見るのはいかがでしょう？」")

        elif result == "청년 경찰":
            self.result2_window.url_label.setText("https://ifh.cc/g/q9Egw9.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/청년 경찰.png); border:0px;')
            self.result2_window.result_text.setText("일상이 코미디인 당신에게 딱 맞는 영화!!\n"
                                                    + "청년경찰을 추천합니다!\n\n"
                                                    + "호기심 많고 언제나 활기찬 당신의 주변에는"
                                                    + "\n언제나 사람들이 모여있어요\n"
                                                    + "\n한 마디로 인싸 기질을 가진 당신!!\n"
                                                    + "\n사람들 사이에서 행복을 느끼기도 하지만"
                                                    + "\n사람들로부터 상처를 많이 받는 타입이에요 ㅠㅠ\n"
                                                    + "\n가끔은 혼자만의 시간을 가지는 것도 나쁘지 않아요"
                                                    + "\n혼자만의 시간을 가지면서 영화를 보는 건 어떨까요?")
        elif result == "Youth police":
            self.result2_window.url_label.setText("https://ifh.cc/g/q9Egw9.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/청년 경찰.png); border:0px;')
            self.result2_window.result_text.setText("A movie that's perfect for you, where everyday is a comedy!!\n"
                                                    + "I recommend the youth police!\n\n"
                                                    + "Curious and always lively around you"
                                                    + "\nPeople are always gathered\n"
                                                    + "\nIn a word, you have an insider temperament!!\n"
                                                    + "\nAlthough I feel happiness among people"
                                                    + "\nI'm the type that gets hurt a lot from people ㅠㅠ\n"
                                                    + "\nIt's not bad to have time alone sometimes"
                                                    + "\nHow about watching a movie while having your own time?")
        elif result == "青年警察":
            self.result2_window.url_label.setText("https://ifh.cc/g/q9Egw9.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/청년 경찰.png); border:0px;')
            self.result2_window.result_text.setText("「日常がコメディであるあなたにぴったりの映画！\n "
                                                    + "青年警察をお勧めします！\n\n"
                                                    + "好奇心はいつも活気に満ちたあなたの周りには"
                                                    + "\nいつも人が集まっています\n"
                                                    + "\n一言でインサ気質のあなた!!\n」"
                                                    + "\n人々の間で幸せを感じることもあるが、「"
                                                    + "\n人々から多くの傷を受けるタイプです〓〓\n"
                                                    + "\n時には一人だけの時間を持つのも悪くありません"
                                                    + "\n一人だけの時間を持ちながら映画を見るのはいかがでしょう？」")

        elif result == "반지의 제왕":
            self.result2_window.url_label.setText("https://ifh.cc/g/ggBgQh.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/반지의 제왕.png); border:0px;')
            self.result2_window.result_text.setText("혹시 주변에서 아이디어뱅크와 같이 새로움을\n"
                                                    + "주는 역할을 맡고 있지 않으신가요?\n\n"
                                                    + "톡톡 튀는 특별함을 가지고 있는 당신에게는"
                                                    + "\n소설을 기반으로 한 영화 반지의 제왕이 찰떡!\n"
                                                    + "\n항상 모든 것에 의문을 갖고 행동하는"
                                                    + "\n당신은 주변 사람들에게 도움을 많이 주는"
                                                    + "\n타입이에요! 아무렇지 않게 내 뱉은 말이"
                                                    + "\n상대에겐 힘이 되거나 도움이 된다는 점..!\n"
                                                    + "\n당신,,, 나랑 친구할래..?")
        elif result == "Lord of the rings":
            self.result2_window.url_label.setText("https://ifh.cc/g/ggBgQh.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/반지의 제왕.png); border:0px;')
            self.result2_window.result_text.setText("Is there anything new like an idea bank around you\n"
                                                    + "Aren't you in the role of giving?\n\n"
                                                    + "For you who have the specialness that pops out"
                                                    + "\nA movie based on a novel, The Lord of the Rings!\n"
                                                    + "\nAlways behave with questions about everything"
                                                    + "\nYou give a lot of help to the people around you"
                                                    + "\nIt's a type! I spit out casually"
                                                    + "\nIt's helpful or helpful to your opponent..!\n"
                                                    + "\nYou,,, would you like to be friends with me...?")
        elif result == "ロードオブザリング":
            self.result2_window.url_label.setText("https://ifh.cc/g/ggBgQh.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/반지의 제왕.png); border:0px;')
            self.result2_window.result_text.setText("「もしかしたら周辺でのアイデアバンクのように新しさを\n "
                                                    + "する役割を担っていアンウシンですか？\n\n"
                                                    + "ピョンピョンはねる特別さを持っているあなたには"
                                                    + "\n小説をベースにした映画ロードオブザリングが相性！」\n"
                                                    + "\n常にすべてのことに疑問を持って行動する」"
                                                    + "\nあなたは周りの人に助けをたくさん与える"
                                                    + "\nタイプです！何気なく吐い言葉"
                                                    + "\n相手にとって力になったり助けになるという点。！」\n"
                                                    + "\n ,,,私と友達ファンシー..？")

        elif result == "해리포터":
            self.result2_window.url_label.setText("https://ifh.cc/g/tu2rKN.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/해리포터.png); border:0px;')
            self.result2_window.result_text.setText("혹시 주변에서 아이디어뱅크와 같이 새로움을\n"
                                                    + "주는 역할을 맡고 있지 않으신가요?\n\n"
                                                    + "톡톡 튀는 특별함을 가지고 있는 당신에게는"
                                                    + "\n소설을 기반으로 한 영화 해리포터가 찰떡!\n"
                                                    + "\n항상 모든 것에 의문을 갖고 행동하는"
                                                    + "\n당신은 주변 사람들에게 도움을 많이 주는"
                                                    + "\n타입이에요! 아무렇지 않게 내 뱉은 말이"
                                                    + "\n상대에겐 힘이 되거나 도움이 된다는 점..!\n"
                                                    + "\n당신,,, 나랑 친구할래..?")
        elif result == "Harry Potter":
            self.result2_window.url_label.setText("https://ifh.cc/g/tu2rKN.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/해리포터.png); border:0px;')
            self.result2_window.result_text.setText("Is there anything new like an idea bank around you\n"
                                                    + "Aren't you in the role of giving?\n\n"
                                                    + "For you who have the specialness that pops out"
                                                    + "\nA movie based on a novel is Harry Potter!\n"
                                                    + "\nAlways behave with questions about everything"
                                                    + "\nYou give a lot of help to the people around you"
                                                    + "\nIt's a type! I spit out casually"
                                                    + "\nIt's helpful or helpful to your opponent..!\n"
                                                    + "\nYou,,, would you like to be friends with me...?")
        elif result == "ハリー・ポッター":
            self.result2_window.url_label.setText("https://ifh.cc/g/tu2rKN.png")
            self.result2_window.result_img.setStyleSheet('image:url(./image/해리포터.png); border:0px;')
            self.result2_window.result_text.setText("「もしかしたら周辺でのアイデアバンクのように新しさを\n"
                                                    + "する役割を担っていアンウシンですか？\n\n "
                                                    + "ピョンピョンはねる特別さを持っているあなたには"
                                                    + "\n小説をベースにした映画ハリー・ポッターが相性！」\n"
                                                    + "\n常にすべてのことに疑問を持って行動する」"
                                                    + "\nあなたは周りの人に助けをたくさん与える"
                                                    + "\nタイプです！何気なく吐い言葉"
                                                    + "\n相手にとって力になったり助けになるという点。！」\n"
                                                    + "\n ,,,私と友達ファンシー..？")