# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtGui, QtCore
import sys
from recognition import landmark_recognition
import random
from pygame import mixer
import time

mixer.init()

def theme_sound():
    mixer.music.load('sound/theme.wav')
    mixer.music.play(-1)


def counting_sound():
    mixer.music.load('sound/count.wav')
    mixer.music.play()


def win_sound():
    mixer.music.load('sound/win.wav')
    mixer.music.play()


def lose_sound():
    mixer.music.load('sound/lose.wav')
    mixer.music.play()


def draw_sound():
    mixer.music.load('sound/draw.wav')
    mixer.music.play()


def click_sound():
    mixer.music.load('sound/click.wav')
    mixer.music.play()


def ready_sound():
    mixer.music.load('sound/ready.wav')
    mixer.music.play()


class App(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.title = 'Rock, Paper, Scissors!'
        self.left = 550
        self.top = 100
        self.width = 800
        self.height = 800
        self.initUI()

    def initUI(self):

        theme_sound()

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Start background image
        self.label = QLabel(self)
        self.pixmap = QPixmap('images/start-background.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())

        # Versus
        self.versus = QLabel(self)
        self.pixmap = QPixmap('images/versus.png')
        self.versus.setPixmap(self.pixmap)
        self.versus.resize(self.pixmap.width(),
                          self.pixmap.height())

        self.versus.move(350,350)
        self.versus.setHidden(True)

        # User result
        self.user = QLabel(self)
        self.pixmap = QPixmap('images/user_result.jpg')
        self.user.setPixmap(self.pixmap)
        self.user.resize(self.pixmap.width(),
                          self.pixmap.height())

        self.user.move(500,500)
        self.user.setHidden(True)

        # Computer 
        self.computer_result = QLabel("", self)
        self.computer_result.setFont(QFont('Times',50))
        self.computer_result.move(450,120)
        self.computer_result.resize(200,100)

        self.computer_result.setHidden(True)

        # User
        self.user_result = QLabel("", self)
        self.user_result.setFont(QFont('Times',50))
        self.user_result.move(200,550)
        self.user_result.resize(200,100)

        self.user_result.setHidden(True)

        # Draw
        self.draw = QLabel("1 - 1", self)
        self.draw.setFont(QFont('Times',50))
        self.draw.move(350,550)
        self.draw.resize(200,100)

        self.draw.setHidden(True)
        
        # Start button
        self.start_button = QPushButton("", self)
        self.start_button.setGeometry(330,620,150,150)
        self.start_button.setStyleSheet("background-image : url(images/start-button.png); border-radius : 75; border : 2px solid black")

        # Click button
        self.start_button.clicked.connect(self.start_game)

        self.setStyleSheet("background-color: lightblue;")

        self.show()

    def start_game(self):
        
        # Hide start page

        click_sound()

        loop = QtCore.QEventLoop()
        
        self.label.setHidden(True)
        self.start_button.setHidden(True)

        QtCore.QTimer.singleShot(1000, loop.quit)
        loop.exec_()

        # Get ready
        self.pixmap = QPixmap('images/get-ready.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.label.move(100,200)
        self.label.setHidden(False)

        ready_sound()

        # Countdown
        # 3
        QtCore.QTimer.singleShot(1000, loop.quit)
        loop.exec_()

        self.label.setHidden(True)

        self.pixmap = QPixmap('images/3.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.label.move(100,200)
        self.label.setHidden(False)

        counting_sound()

        # 2
        QtCore.QTimer.singleShot(1000, loop.quit)
        loop.exec_()

        self.label.setHidden(True)

        self.pixmap = QPixmap('images/2.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.label.move(100,200)
        self.label.setHidden(False)

        counting_sound()

        # 1
        QtCore.QTimer.singleShot(1000, loop.quit)
        loop.exec_()

        self.label.setHidden(True)

        self.pixmap = QPixmap('images/1.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.label.move(100,200)
        self.label.setHidden(False)

        counting_sound()

        QtCore.QTimer.singleShot(1000, loop.quit)
        loop.exec_()

        # from recognition import landmark_recognition
        user_move = landmark_recognition()

        computer = random.randint(1,3)

        if computer == 1:

            computer = "Rock"

            QtCore.QTimer.singleShot(1000, loop.quit)
            loop.exec_()

            self.label.setHidden(True)

            self.pixmap = QPixmap('images/rock.jpg')
            self.label.setPixmap(self.pixmap)
            self.label.resize(self.pixmap.width(),
                            self.pixmap.height())
            self.label.move(25,25)
            self.label.setHidden(False)

            self.computer_result.setText("Rock")
            self.computer_result.setHidden(False)

            self.versus.setHidden(False)

            self.user_result.setText(user_move)
            self.user_result.setHidden(False)

            self.pixmap = QPixmap('images/user_result.jpg')
            self.user.setPixmap(self.pixmap)
            self.user.resize(self.pixmap.width(),
                            self.pixmap.height())

            self.user.move(500,500)
            self.user.setHidden(False)


        elif computer == 2:

            computer = 'Paper'

            QtCore.QTimer.singleShot(1000, loop.quit)
            loop.exec_()

            self.label.setHidden(True)

            self.pixmap = QPixmap('images/paper.jpg')
            self.label.setPixmap(self.pixmap)
            self.label.resize(self.pixmap.width(),
                            self.pixmap.height())
            self.label.move(25,25)
            self.label.setHidden(False)

            self.computer_result.setText("Paper")
            self.computer_result.setHidden(False)

            self.versus.setHidden(False)

            self.user_result.setText(user_move)
            self.user_result.setHidden(False)

            self.pixmap = QPixmap('images/user_result.jpg')
            self.user.setPixmap(self.pixmap)
            self.user.resize(self.pixmap.width(),
                            self.pixmap.height())

            self.user.move(500,500)
            self.user.setHidden(False)


        elif computer == 3:

            computer = "Scissor"

            QtCore.QTimer.singleShot(1000, loop.quit)
            loop.exec_()

            self.label.setHidden(True)

            self.pixmap = QPixmap('images/scissor.jpg')
            self.label.setPixmap(self.pixmap)
            self.label.resize(self.pixmap.width(),
                            self.pixmap.height())
            self.label.move(25,25)
            self.label.setHidden(False)

            self.computer_result.setText("Scissor")
            self.computer_result.setHidden(False)

            self.versus.setHidden(False)

            self.user_result.setText(user_move)
            self.user_result.setHidden(False)

            self.pixmap = QPixmap('images/user_result.jpg')
            self.user.setPixmap(self.pixmap)
            self.user.resize(self.pixmap.width(),
                            self.pixmap.height())

            self.user.move(500,500)
            self.user.setHidden(False)

        QtCore.QTimer.singleShot(3000, loop.quit)
        loop.exec_()

        self.versus.setHidden(True)
        self.label.setHidden(True)
        self.computer_result.setHidden(True)
        self.user.setHidden(True)
        self.user_result.setHidden(True)

        print("Computer: {}".format(computer))
        print("You: {}".format(user_move))

        if computer.lower() == "rock" and user_move.lower() == "scissor":

            self.label = QLabel(self)
            self.pixmap = QPixmap('images/loser.png')
            self.label.setPixmap(self.pixmap)
            self.label.resize(self.pixmap.width(),
                            self.pixmap.height())

            self.label.setHidden(False)
            self.label.move(150,200)

            lose_sound()

        elif computer.lower() == "rock" and user_move.lower() == "paper":

            self.label = QLabel(self)
            self.pixmap = QPixmap('images/winner.png')
            self.label.setPixmap(self.pixmap)
            self.label.resize(self.pixmap.width(),
                            self.pixmap.height())

            self.label.setHidden(False)
            self.label.move(50,50)

            win_sound()

        elif computer.lower() == "paper" and user_move.lower() == "rock":

            self.label = QLabel(self)
            self.pixmap = QPixmap('images/loser.png')
            self.label.setPixmap(self.pixmap)
            self.label.resize(self.pixmap.width(),
                            self.pixmap.height())

            self.label.setHidden(False)
            self.label.move(150,200)

            lose_sound()

        elif computer.lower() == "paper" and user_move.lower() == "scissor":

            self.label = QLabel(self)
            self.pixmap = QPixmap('images/winner.png')
            self.label.setPixmap(self.pixmap)
            self.label.resize(self.pixmap.width(),
                            self.pixmap.height())

            self.label.setHidden(False)
            self.label.move(50,50)

            win_sound()

        elif computer.lower() == "scissor" and user_move.lower() == "paper":

            self.label = QLabel(self)
            self.pixmap = QPixmap('images/loser.png')
            self.label.setPixmap(self.pixmap)
            self.label.resize(self.pixmap.width(),
                            self.pixmap.height())

            self.label.setHidden(False)
            self.label.move(150,200)

            lose_sound()

        elif computer.lower() == "scissor" and user_move.lower() == "rock":

            self.label = QLabel(self)
            self.pixmap = QPixmap('images/winner.png')
            self.label.setPixmap(self.pixmap)
            self.label.resize(self.pixmap.width(),
                            self.pixmap.height())

            self.label.setHidden(False)
            self.label.move(50,50)

            win_sound()

        elif computer.lower() == user_move.lower():

            self.label = QLabel(self)
            self.pixmap = QPixmap('images/draw.png')
            self.label.setPixmap(self.pixmap)
            self.label.resize(self.pixmap.width(),
                            self.pixmap.height())

            self.label.setHidden(False)
            self.label.move(190,120)

            self.draw.setHidden(False)

            draw_sound()

        QtCore.QTimer.singleShot(2000, loop.quit)
        loop.exec_()

        self.label.setHidden(True)
        self.draw.setHidden(True)

        self.label = QLabel(self)
        self.pixmap = QPixmap('images/thanks.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                        self.pixmap.height())

        self.label.setHidden(False)
        self.label.move(130,120)

        self.start_button.setStyleSheet("background-image : url(images/restart-button.png); border-radius : 75; border : 2px solid black")
        self.start_button.setGeometry(330,600,150,150)
        self.start_button.setHidden(False)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())