import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtGui
from result1_window import Result_Window

# mysql ##################################
cnx = mysql.connector.connect(
    user = "root",
    password = "sori0927",
    host = "127.0.0.1",
    port = 3306,
    database = "test_zip"
)

cursor = cnx.cursor()

class Test1_Question5_Window(QtWidgets.QMainWindow, QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('당신은 프론트엔드인가? 백엔드인가?')
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

        self.label = QLabel("         은(는) 프론트엔드인가? 백엔드인가?", self)
        self.label.setFont(QtGui.QFont("맑은 고딕", 13))
        self.label.resize(800, 60)
        self.label.move(40, 100)

        #질문
        self.q1 = QLabel("사람들이 나에게 주목할 때", self)
        self.q1.setFont(QtGui.QFont("맑은 고딕", 26))
        self.q1.resize(800, 60)
        self.q1.move(30, 140)

        #답 버튼
        self.a1 = QPushButton("솔직히 즐긴다. 짜릿해", self)
        self.a1.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a1.resize(800, 100)
        self.a1.move(30, 210)
        self.a1.clicked.connect(self.a_click)

        self.a2 = QPushButton("으으 부담스러워~~", self)
        self.a2.setFont(QtGui.QFont("맑은 고딕", 20))
        self.a2.resize(800, 100)
        self.a2.move(30, 320)
        self.a2.clicked.connect(self.b_click)

        self.result_window = Result_Window(self)

    def a_click(self):
        self.result_window.show()
        user_name = self.name_label.text()
        self.result_window.name_label.setText(user_name)

        sql = "UPDATE programmer_Test SET calculate = calculate + 10 WHERE result = 0;"
        cursor.execute(sql)
        cnx.commit()

        print(user_name, ">>>점수 추가 완료")
        # print(self.name_label.text() + " : b 선택")

        sql = "SELECT calculate from programmer_Test WHERE result = 0;"
        cursor.execute(sql)
        calculate = cursor.fetchmany(1)

        sum = str(calculate)
        print(sum[2:-3])

        cnx.commit()

        cal = int(sum[2:-3])

        #result_save = "update programmer_Test set result = %s where calculate>=%s and calculate<=%s"

        if cal >= 41 and cal <= 50 :
            result = "프론트엔드 공주님"
            if self.label.text() == "Are you the frontend? Is it the backend?":
                result = "Frontend princess"
            elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
                result = "フロントエンドお姫様"
            #cursor.execute(result_save, ("프론트엔드 공주님", 41, 50))
        elif cal >= 31 and cal <= 40 :
            result = "100% 프론트엔드"
            if self.label.text() == "Are you the frontend? Is it the backend?":
                result = "100% frontend"
            elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
                result = "100％フロントエンド"
            #cursor.execute(result_save, ("100% 프론트엔드", 31, 40))
        elif cal >= 21 and cal <= 30:
            result = "뼈개 풀스택"
            if self.label.text() == "Are you the frontend? Is it the backend?":
                result = "Bone Full Stack"
            elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
                result = "ピョゲフルスタック"
            #cursor.execute(result_save, ("뼈개 풀스택", 21, 30))
        elif cal >= 11 and cal <= 20:
            result = "노감성 백엔드"
            if self.label.text() == "Are you the frontend? Is it the backend?":
                result = "Sensitive backend"
            elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
                result = "ノー感性バックエンド"
            #cursor.execute(result_save, ("노감성 백엔드", 11, 20))
        elif cal >= 0 and cal <= 10 :
            result = "100% 백엔드"
            if self.label.text() == "Are you the frontend? Is it the backend?":
                result = "100% backend"
            elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
                result = "100％のバックエンド"
            #cursor.execute(result_save, ("100% 백엔드", 0, 10))

        print("결과>>>", result)
        self.result_window.result_name.setText(result)
        if result == "프론트엔드 공주님":
            self.result_window.result_img.setStyleSheet('image:url(./image/Frontend_1.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/쉬운 백엔드.png); border:0px;')
            self.result_window.result_text.setText("답은 정해져 있어 너는 잘했다고 말만 해.\n"
                                                   + "내가 짠 코드가 화면에 나타났어 자랑하고 싶다\n"
                                                   + "자랑하고 싶어! 공주님처럼 너무 예쁘잖아!!"
                                                   + "\n뭐든지 다 예뻐야 하는 당신은 프론트 공주님!"
                                                   + "\n항상 밝고 쾌활한 이미지의 당신은 분위기 메이커!!"
                                                   + "\n하지만 속은 공주님처럼 여리다는 걸 알랑가 몰라~~")
        elif result == "Frontend princess" :
            self.result_window.result_img.setStyleSheet('image:url(./image/Frontend_1.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/쉬운 백엔드.png); border:0px;')
            self.result_window.result_text.setText("The answer is fixed, just say you did a good job.\n"
                                                   + "My code appeared on the screen and I want to show off\n"
                                                   + "I want to show off! You're so pretty like a princess!!"
                                                   + "\nYou must be pretty, the Front Princess!"
                                                   + "\nAlways bright and cheerful, you are the mood maker!!"
                                                   + "\nBut I don't know that the inside is soft like a princess~~")
        elif result == "フロントエンドお姫様" :
            self.result_window.result_img.setStyleSheet('image:url(./image/Frontend_1.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/쉬운 백엔드.png); border:0px;')
            self.result_window.result_text.setText("答えは決まっており、あなたはよくやったとばかりしてた。\ n "
                                                   + "私の効いたコードが画面に現れ自慢したい\ n"
                                                   + "自慢したい！お姫様のように、あまりにもきれいじゃない！」"
                                                   + "\ n何でも美しくてこそあなたは、フロントお姫様！」"
                                                   + "\ n常に明るく陽気なイメージの場合は、ムードメーカー！」"
                                                   + "\ nが騙さお姫様のようにヨリダということアルランガ知らない~~")

        elif result == "100% 프론트엔드":
            self.result_window.result_img.setStyleSheet('image:url(./image/Frontend_2.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/천사 백엔드.png); border:0px;')
            self.result_window.result_text.setText("1px에 집착하고 자간에 집착하는 당신.\n"
                                                   + "완벽한 레이아웃이 아니면 개발을 시작할 수 없어!\n"
                                                   + "대칭 딱딱 맞는 사이트를 완벽하게 구현해야만 해."
                                                   + "\n프론트는 당신의 데스티니~ 누구보다 미적 감각이"
                                                   + "\n뛰어난 당신!! 혹시 전생에 예술가는 아니셨는지?"
                                                   + "\n100% 프론트엔드 기질을 가진 당신은 혼자서도"
                                                   + "\n잘하지만, 가끔은 당신의 도움을 바라는 친구는"
                                                   + "\n없는지 주변을 둘러봐 주세요. ㅠㅠ")
        elif result == "100% frontend":
            self.result_window.result_img.setStyleSheet('image:url(./image/Frontend_2.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/천사 백엔드.png); border:0px;')
            self.result_window.result_text.setText("You obsessed with 1px and space between characters.\n"
                                                   + "You can't start developing without a perfect layout!\n"
                                                   + "You have to make a perfect symmetrical fit site."
                                                   + "\nThe front is your Destiny~ More aesthetic than anyone else"
                                                   + "\nExcellent you!! Wasn't you an artist in your previous life?"
                                                   + "\nYou have a 100% frontend temperament, even by yourself"
                                                   + "\nGood, but sometimes a friend who wants your help"
                                                   + "\nPlease look around for it.")
        elif result == "100％フロントエンド":
            self.result_window.result_img.setStyleSheet('image:url(./image/Frontend_2.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/천사 백엔드.png); border:0px;')
            self.result_window.result_text.setText("1pxに執着して間にこだわるあなた\ n "
                                                   + "完璧なレイアウトがなければ、開発を開始することができない！\ n"
                                                   + "対称硬く合うサイトを完全に実装しなければして」"
                                                   + "\ nフロントはあなたのデスティニー〜誰よりも美的感覚が"
                                                   + "\ n優れたあなた!!もしかしたら前世の芸術家ではないたのか？」"
                                                   + "\ n100％フロントエンド気質を持つ場合は、一人でも"
                                                   + "\ n良いが、時にはあなたの助けを望む友人は"
                                                   + "\ nない周辺を見回してください。〓〓")

        elif result == "뼈개 풀스택":
            self.result_window.result_img.setStyleSheet('image:url(./image/FullStack.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/만능 풀스택.png); border:0px;')
            self.result_window.result_text.setText("디자인이랑도 놀고 싶고 데이터랑도 놀고 싶은\n"
                                                   + "당신은 욕심쟁이 우후훗!~.\n"
                                                   + "어차피 다 하는데 좀 더 끌리는 걸 먼저 배워볼까?"
                                                   + "\n뭘 해도 다 잘할 당신!! 무수히 많은 매력이 있어~~"
                                                   + "\n그치만 조심해! 욕심부리다 다 놓칠 수가 있다구~"
                                                   + "\n지금은 내면의 목소리에 조금 더 귀를 기울여보면"
                                                   + "\n어떨까요?")
        elif result == "Bone Full Stack":
            self.result_window.result_img.setStyleSheet('image:url(./image/FullStack.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/만능 풀스택.png); border:0px;')
            self.result_window.result_text.setText("I want to play with design and data.\n"
                                                   + "You are a greedy man!~.\n"
                                                   + "I'm done anyway, but shall I learn something more attracted?"
                                                   + "\nYou can do everything well! You have so many charms~~"
                                                   + "\nBut be careful! I can miss everything because I'm greedy~"
                                                   + "\nIf you listen a little more to your inner voice"
                                                   + "\nWhat about?")
        elif result == "ピョゲフルスタック":
            self.result_window.result_img.setStyleSheet('image:url(./image/FullStack.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/만능 풀스택.png); border:0px;')
            self.result_window.result_text.setText("デザインやらも遊びたいデータラングも遊びたい\ n "
                                                   + "あなたは欲張りウフフッ！〜\ n"
                                                   + "どうせだのに、より惹かれることを先に学んでみようかな」"
                                                   + "\ n何も多上手に!!無数の魅力があり~~"
                                                   + "\ nでも気をつけて！欲ブリーダーだ見逃すことができている旧〜"
                                                   + "\ n今は内面の声にもう少し耳を傾けてみると、"
                                                   + "\ nいかがでしょうか")

        elif result == "노감성 백엔드":
            self.result_window.result_img.setStyleSheet('image:url(./image/Backend_1.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/쉬운 프론트엔드.png); border:0px;')
            self.result_window.result_text.setText("ㄴㅇㄱ 갬성?? 그게 뭐지? 먹는 건가요?\n"
                                                   + "디자인이라곤 1도 모르는 노감성 백엔드 체질인 당신!\n"
                                                   + "하지만 DB천재!! 내가 바로 이 시대 백엔드 개발자..?"
                                                   + "\n데이터라면 다 긁어오는 당신,"
                                                   + "\n하지만 내 속을 들키긴 싫어 ~~.."
                                                   + "\n내 감성을 채워주기 위한 파트너가 필요해~~~"
                                                   + "\n100% 프론트엔드와 함께라면 우린 천하무적")
        elif result == "Sensitive backend":
            self.result_window.result_img.setStyleSheet('image:url(./image/Backend_1.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/쉬운 프론트엔드.png); border:0px;')
            self.result_window.result_text.setText("ㄴㅇㄱ Emotion?? What is that? Are you eating?\n"
                                                   + "You are a sensitive back-end constitution who knows nothing about design!\n"
                                                   + "But a DB genius!! I am a backend developer in this era...?"
                                                   + "\nYou are raking all data,"
                                                   + "\nBut I don't want to get caught up in me ~~.."
                                                   + "\nI need a partner to fill my emotions~~~"
                                                   + "\nWith a 100% front end, we are invincible")
        elif result == "ノー感性バックエンド":
            self.result_window.result_img.setStyleSheet('image:url(./image/Backend_1.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/쉬운 프론트엔드.png); border:0px;')
            self.result_window.result_text.setText("ㄴㅇㄱ 感性？それ何？食べるんですか？\ n "
                                                   + "デザインといえば、1度知らないノー感性バックエンド体質のあなた！\ n"
                                                   + "しかし、DB天才！私はすぐにこの時代のバックエンドの開発者..？"
                                                   + "\ nデータであれば、多傷のあなた、"
                                                   + "\ nしかし、私の中が挙げキギン嫌い~~。」"
                                                   + "\ n私の感性を満たして与えるためのパートナーが必要~~~"
                                                   + "\ n100％フロントエンドと一緒なら私たちは天下無敵")

        elif result == "100% 백엔드":
            self.result_window.result_img.setStyleSheet('image:url(./image/Backend_2.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/프론트엔드 공주님.png); border:0px;')
            self.result_window.result_text.setText("오잉?????? 애니메이션은 먹는 건가요?\n"
                                                   + "디자인은 알 바 아니고 나는 내가 생각한 게 맞는지가 중요해.\n"
                                                   + "인풋. 아웃풋. 효율. 삐빅. 터미널 접속. 짠다 로직."
                                                   + "\n보낸다. 빠르게. 데이터. 삐빅. 이런 안되잖아?"
                                                   + "\n삐빅. 임무 완료. 로봇 같은 100% 백엔드 기질을 가진 당신!"
                                                   + "\n그렇지만 마음은 따뜻해~~ 당신이 바로 겉바속촉??"
                                                   + "\n무심한 당신과 활기찬 공주님이 만나면 그것이 바로"
                                                   + "\n환상의 조합 ♥")
        elif result == "100% backend":
            self.result_window.result_img.setStyleSheet('image:url(./image/Backend_2.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/프론트엔드 공주님.png); border:0px;')
            self.result_window.result_text.setText("Oing?????? Are you eating anime?\n"
                                                   + "I don't know the design, it's important that I think it's right.\n"
                                                   + "Input. Output. Efficiency. Pivik. Terminal connection. Squeeze logic."
                                                   + "\nSend. Quickly. Data. Pibig. This doesn't work?"
                                                   + "\nBeep. Complete mission. You have 100% backend temperament like a robot!"
                                                   + "\nBut my heart is warm~~ Are you right on the outside?"
                                                   + "\nIf you and a lively princess meet, that's it"
                                                   + "\nA fantasy combination ♥")
        elif result == "100％のバックエンド":
            self.result_window.result_img.setStyleSheet('image:url(./image/Backend_2.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/프론트엔드 공주님.png); border:0px;')
            self.result_window.result_text.setText("オイン??????アニメーションは食べるんですか？\ n "
                                                   + "のデザインは、アルバーではなく、私は私考えたのが正しいが重要。\ n"
                                                   + "インプット。アウトプット。効率。ピビクターミナル接続。絞るロジック」"
                                                   + "\ n送る。高速データ。ピビクこんなダメじゃない？」"
                                                   + "\ nピビク。任務完了。ロボットのような100％のバックエンド気質のあなた！"
                                                   + "\ nでも心は暖かく~~あなたがすぐにゴトバソクチョク？"
                                                   + "\ n無関心なあなたと活気に満ちたお姫様が会えば、それがまさに"
                                                   + "\ n幻の組み合わせ♥")
        cnx.commit()
        self.hide()


    def b_click(self):
        self.result_window.show()
        user_name = self.name_label.text()
        self.result_window.name_label.setText(user_name)

        print(user_name, ">>>점수 추가 완료")
        # print(self.name_label.text() + " : b 선택")

        sql = "SELECT calculate from programmer_Test WHERE result = 0;"
        cursor.execute(sql)
        calculate = cursor.fetchmany(1)

        sum = str(calculate)
        print(sum[2:-3])

        cnx.commit()

        cal = int(sum[2:-3])

        #result_save = "update programmer_Test set result = %s where calculate>=%s and calculate<=%s"

        if cal >= 41 and cal <= 50 :
            result = "프론트엔드 공주님"
            if self.label.text() == "Are you the frontend? Is it the backend?":
                result = "Frontend princess"
            elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
                result = "フロントエンドお姫様"
            #cursor.execute(result_save, ("프론트엔드 공주님", 41, 50))
        elif cal >= 31 and cal <= 40 :
            result = "100% 프론트엔드"
            if self.label.text() == "Are you the frontend? Is it the backend?":
                result = "100% frontend"
            elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
                result = "100％フロントエンド"
            #cursor.execute(result_save, ("100% 프론트엔드", 31, 40))
        elif cal >= 21 and cal <= 30:
            result = "뼈개 풀스택"
            if self.label.text() == "Are you the frontend? Is it the backend?":
                result = "Bone Full Stack"
            elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
                result = "ピョゲフルスタック"
            #cursor.execute(result_save, ("뼈개 풀스택", 21, 30))
        elif cal >= 11 and cal <= 20:
            result = "노감성 백엔드"
            if self.label.text() == "Are you the frontend? Is it the backend?":
                result = "Sensitive backend"
            elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
                result = "ノー感性バックエンド"
            #cursor.execute(result_save, ("노감성 백엔드", 11, 20))
        elif cal >= 1 and cal <= 10 :
            result = "100% 백엔드"
            if self.label.text() == "Are you the frontend? Is it the backend?":
                result = "100% backend"
            elif self.label.text() == "あなたはフロントエンドであるかバックエンドのか？":
                result = "100％のバックエンド"
            #cursor.execute(result_save, ("100% 백엔드", 1, 10))

        print("결과>>>", result)
        self.result_window.result_name.setText(result)
        if result == "프론트엔드 공주님":
            self.result_window.url_label.setText("https://ifh.cc/g/fQljkY.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/Frontend_1.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/쉬운 백엔드.png); border:0px;')
            self.result_window.result_text.setText("답은 정해져 있어 너는 잘했다고 말만 해.\n"
                                                   + "내가 짠 코드가 화면에 나타났어 자랑하고 싶다\n"
                                                   + "자랑하고 싶어! 공주님처럼 너무 예쁘잖아!!"
                                                   + "\n뭐든지 다 예뻐야 하는 당신은 프론트 공주님!"
                                                   + "\n항상 밝고 쾌활한 이미지의 당신은 분위기 메이커!!"
                                                   + "\n하지만 속은 공주님처럼 여리다는 걸 알랑가 몰라~~")
        elif result == "Frontend princess" :
            self.result_window.url_label.setText("https://ifh.cc/g/fQljkY.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/Frontend_1.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/쉬운 백엔드.png); border:0px;')
            self.result_window.result_text.setText("The answer is fixed, just say you did a good job.\n"
                                                   + "My code appeared on the screen and I want to show off\n"
                                                   + "I want to show off! You're so pretty like a princess!!"
                                                   + "\nYou must be pretty, the Front Princess!"
                                                   + "\nAlways bright and cheerful, you are the mood maker!!"
                                                   + "\nBut I don't know that the inside is soft like a princess~~")
        elif result == "フロントエンドお姫様" :
            self.result_window.url_label.setText("https://ifh.cc/g/fQljkY.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/Frontend_1.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/쉬운 백엔드.png); border:0px;')
            self.result_window.result_text.setText("答えは決まっており、あなたはよくやったとばかりしてた。\ n "
                                                   + "私の効いたコードが画面に現れ自慢したい\ n"
                                                   + "自慢したい！お姫様のように、あまりにもきれいじゃない！」"
                                                   + "\ n何でも美しくてこそあなたは、フロントお姫様！」"
                                                   + "\ n常に明るく陽気なイメージの場合は、ムードメーカー！」"
                                                   + "\ nが騙さお姫様のようにヨリダということアルランガ知らない~~")

        elif result == "100% 프론트엔드":
            self.result_window.url_label.setText("https://ifh.cc/g/T2mLIe.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/Frontend_2.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/천사 백엔드.png); border:0px;')
            self.result_window.result_text.setText("1px에 집착하고 자간에 집착하는 당신.\n"
                                                   + "완벽한 레이아웃이 아니면 개발을 시작할 수 없어!\n"
                                                   + "대칭 딱딱 맞는 사이트를 완벽하게 구현해야만 해."
                                                   + "\n프론트는 당신의 데스티니~ 누구보다 미적 감각이"
                                                   + "\n뛰어난 당신!! 혹시 전생에 예술가는 아니셨는지?"
                                                   + "\n100% 프론트엔드 기질을 가진 당신은 혼자서도"
                                                   + "\n잘하지만, 가끔은 당신의 도움을 바라는 친구는"
                                                   + "\n없는지 주변을 둘러봐 주세요. ㅠㅠ")
        elif result == "100% frontend":
            self.result_window.url_label.setText("https://ifh.cc/g/T2mLIe.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/Frontend_2.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/천사 백엔드.png); border:0px;')
            self.result_window.result_text.setText("You obsessed with 1px and space between characters.\n"
                                                   + "You can't start developing without a perfect layout!\n"
                                                   + "You have to make a perfect symmetrical fit site."
                                                   + "\nThe front is your Destiny~ More aesthetic than anyone else"
                                                   + "\nExcellent you!! Wasn't you an artist in your previous life?"
                                                   + "\nYou have a 100% frontend temperament, even by yourself"
                                                   + "\nGood, but sometimes a friend who wants your help"
                                                   + "\nPlease look around for it.")
        elif result == "100％フロントエンド":
            self.result_window.url_label.setText("https://ifh.cc/g/T2mLIe.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/Frontend_2.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/천사 백엔드.png); border:0px;')
            self.result_window.result_text.setText("1pxに執着して間にこだわるあなた\ n "
                                                   + "完璧なレイアウトがなければ、開発を開始することができない！\ n"
                                                   + "対称硬く合うサイトを完全に実装しなければして」"
                                                   + "\ nフロントはあなたのデスティニー〜誰よりも美的感覚が"
                                                   + "\ n優れたあなた!!もしかしたら前世の芸術家ではないたのか？」"
                                                   + "\ n100％フロントエンド気質を持つ場合は、一人でも"
                                                   + "\ n良いが、時にはあなたの助けを望む友人は"
                                                   + "\ nない周辺を見回してください。〓〓")

        elif result == "뼈개 풀스택":
            self.result_window.url_label.setText("https://ifh.cc/g/0vRYUl.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/FullStack.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/만능 풀스택.png); border:0px;')
            self.result_window.result_text.setText("디자인이랑도 놀고 싶고 데이터랑도 놀고 싶은\n"
                                                   + "당신은 욕심쟁이 우후훗!~.\n"
                                                   + "어차피 다 하는데 좀 더 끌리는 걸 먼저 배워볼까?"
                                                   + "\n뭘 해도 다 잘할 당신!! 무수히 많은 매력이 있어~~"
                                                   + "\n그치만 조심해! 욕심부리다 다 놓칠 수가 있다구~"
                                                   + "\n지금은 내면의 목소리에 조금 더 귀를 기울여보면"
                                                   + "\n어떨까요?")
        elif result == "Bone Full Stack":
            self.result_window.url_label.setText("https://ifh.cc/g/0vRYUl.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/FullStack.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/만능 풀스택.png); border:0px;')
            self.result_window.result_text.setText("I want to play with design and data.\n"
                                                   + "You are a greedy man!~.\n"
                                                   + "I'm done anyway, but shall I learn something more attracted?"
                                                   + "\nYou can do everything well! You have so many charms~~"
                                                   + "\nBut be careful! I can miss everything because I'm greedy~"
                                                   + "\nIf you listen a little more to your inner voice"
                                                   + "\nWhat about?")
        elif result == "ピョゲフルスタック":
            self.result_window.url_label.setText("https://ifh.cc/g/0vRYUl.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/FullStack.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/만능 풀스택.png); border:0px;')
            self.result_window.result_text.setText("デザインやらも遊びたいデータラングも遊びたい\ n "
                                                   + "あなたは欲張りウフフッ！〜\ n"
                                                   + "どうせだのに、より惹かれることを先に学んでみようかな」"
                                                   + "\ n何も多上手に!!無数の魅力があり~~"
                                                   + "\ nでも気をつけて！欲ブリーダーだ見逃すことができている旧〜"
                                                   + "\ n今は内面の声にもう少し耳を傾けてみると、"
                                                   + "\ nいかがでしょうか")

        elif result == "노감성 백엔드":
            self.result_window.url_label.setText("https://ifh.cc/g/vL7wuO.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/Backend_1.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/쉬운 프론트엔드.png); border:0px;')
            self.result_window.result_text.setText("ㄴㅇㄱ 갬성?? 그게 뭐지? 먹는 건가요?\n"
                                                   + "디자인이라곤 1도 모르는 노감성 백엔드 체질인 당신!\n"
                                                   + "하지만 DB천재!! 내가 바로 이 시대 백엔드 개발자..?"
                                                   + "\n데이터라면 다 긁어오는 당신,"
                                                   + "\n하지만 내 속을 들키긴 싫어 ~~.."
                                                   + "\n내 감성을 채워주기 위한 파트너가 필요해~~~"
                                                   + "\n100% 프론트엔드와 함께라면 우린 천하무적")
        elif result == "Sensitive backend":
            self.result_window.url_label.setText("https://ifh.cc/g/vL7wuO.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/Backend_1.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/쉬운 프론트엔드.png); border:0px;')
            self.result_window.result_text.setText("ㄴㅇㄱ Emotion?? What is that? Are you eating?\n"
                                                   + "You are a sensitive back-end constitution who knows nothing about design!\n"
                                                   + "But a DB genius!! I am a backend developer in this era...?"
                                                   + "\nYou are raking all data,"
                                                   + "\nBut I don't want to get caught up in me ~~.."
                                                   + "\nI need a partner to fill my emotions~~~"
                                                   + "\nWith a 100% front end, we are invincible")
        elif result == "ノー感性バックエンド":
            self.result_window.url_label.setText("https://ifh.cc/g/vL7wuO.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/Backend_1.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/쉬운 프론트엔드.png); border:0px;')
            self.result_window.result_text.setText("ㄴㅇㄱ 感性？それ何？食べるんですか？\ n "
                                                   + "デザインといえば、1度知らないノー感性バックエンド体質のあなた！\ n"
                                                   + "しかし、DB天才！私はすぐにこの時代のバックエンドの開発者..？"
                                                   + "\ nデータであれば、多傷のあなた、"
                                                   + "\ nしかし、私の中が挙げキギン嫌い~~。」"
                                                   + "\ n私の感性を満たして与えるためのパートナーが必要~~~"
                                                   + "\ n100％フロントエンドと一緒なら私たちは天下無敵")

        elif result == "100% 백엔드":
            self.result_window.url_label.setText("https://ifh.cc/g/cCif4i.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/Backend_2.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/프론트엔드 공주님.png); border:0px;')
            self.result_window.result_text.setText("오잉?????? 애니메이션은 먹는 건가요?\n"
                                                   + "디자인은 알 바 아니고 나는 내가 생각한 게 맞는지가 중요해.\n"
                                                   + "인풋. 아웃풋. 효율. 삐빅. 터미널 접속. 짠다 로직."
                                                   + "\n보낸다. 빠르게. 데이터. 삐빅. 이런 안되잖아?"
                                                   + "\n삐빅. 임무 완료. 로봇 같은 100% 백엔드 기질을 가진 당신!"
                                                   + "\n그렇지만 마음은 따뜻해~~ 당신이 바로 겉바속촉??"
                                                   + "\n무심한 당신과 활기찬 공주님이 만나면 그것이 바로"
                                                   + "\n환상의 조합 ♥")
        elif result == "100% backend":
            self.result_window.url_label.setText("https://ifh.cc/g/cCif4i.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/Backend_2.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/프론트엔드 공주님.png); border:0px;')
            self.result_window.result_text.setText("Oing?????? Are you eating anime?\n"
                                                   + "I don't know the design, it's important that I think it's right.\n"
                                                   + "Input. Output. Efficiency. Pivik. Terminal connection. Squeeze logic."
                                                   + "\nSend. Quickly. Data. Pibig. This doesn't work?"
                                                   + "\nBeep. Complete mission. You have 100% backend temperament like a robot!"
                                                   + "\nBut my heart is warm~~ Are you right on the outside?"
                                                   + "\nIf you and a lively princess meet, that's it"
                                                   + "\nA fantasy combination ♥")
        elif result == "100％のバックエンド":
            self.result_window.url_label.setText("https://ifh.cc/g/cCif4i.png")
            self.result_window.result_img.setStyleSheet('image:url(./image/Backend_2.png); border:0px;')
            self.result_window.best_friend.setStyleSheet('image:url(./image/프론트엔드 공주님.png); border:0px;')
            self.result_window.result_text.setText("オイン??????アニメーションは食べるんですか？\ n "
                                                   + "のデザインは、アルバーではなく、私は私考えたのが正しいが重要。\ n"
                                                   + "インプット。アウトプット。効率。ピビクターミナル接続。絞るロジック」"
                                                   + "\ n送る。高速データ。ピビクこんなダメじゃない？」"
                                                   + "\ nピビク。任務完了。ロボットのような100％のバックエンド気質のあなた！"
                                                   + "\ nでも心は暖かく~~あなたがすぐにゴトバソクチョク？"
                                                   + "\ n無関心なあなたと活気に満ちたお姫様が会えば、それがまさに"
                                                   + "\ n幻の組み合わせ♥")
        cnx.commit()
        self.hide()