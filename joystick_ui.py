import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import QtCore, QtGui
import json
import csv
import os
from os.path import exists
import pandas as pd
import numpy as np

import time

# import read_joystick_test as read_joystick
import read_joystick

import move_robot

class myGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Joystick User Interface')

        # setup the layout parameters
        win_w = 800
        win_h = 600
        title_w = 400
        title_h = 50
        label_w = 150
        label_h = 40
        blank_w = 30
        blank_h = 10
        btn_w = 150
        btn_h = 50

        # setup the global parameters
        self.robot_conn = False
        self.joystick_conn = False
        self.init_pose = read_joystick.init_angle()
        self.index = 1

        # set the title
        self.title_angle = QLabel('Joint Angle', self)
        self.title_angle.move(0, 0)
        self.title_angle.resize(title_w, title_h)
        self.title_angle.setFont(QFont('Ubuntu', 20, QFont.Medium))
        self.title_angle.setStyleSheet('color: white; background-color: black')
        self.title_angle.setAlignment(QtCore.Qt.AlignCenter)

        # set the label and angle
        self.background_angle = QLabel(' ', self)
        self.background_angle.move(0, title_h)
        self.background_angle.resize(title_w, label_h*6+blank_h*7)
        self.background_angle.setStyleSheet('background-color: white')

        self.label1 = QLabel('Joint 1: ', self)
        self.label1.move(0, blank_h+title_h)
        self.label1.resize(label_w, label_h)
        self.label1.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.label1.setStyleSheet('color: black; background-color: white')
        self.label1.setAlignment(QtCore.Qt.AlignCenter)

        self.angle1 = QLabel('0', self)
        self.angle1.move(0+label_w, self.label1.y())
        self.angle1.resize(label_w, label_h)
        self.angle1.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.angle1.setStyleSheet('color: black; background-color: white')
        self.angle1.setAlignment(QtCore.Qt.AlignCenter)

        self.label2 = QLabel('Joint 2: ', self)
        self.label2.move(0, blank_h*2+title_h+label_h)
        self.label2.resize(label_w, label_h)
        self.label2.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.label2.setStyleSheet('color: black; background-color: white')
        self.label2.setAlignment(QtCore.Qt.AlignCenter)

        self.angle2 = QLabel('0', self)
        self.angle2.move(0+label_w, self.label2.y())
        self.angle2.resize(label_w, label_h)
        self.angle2.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.angle2.setStyleSheet('color: black; background-color: white')
        self.angle2.setAlignment(QtCore.Qt.AlignCenter)

        self.label3 = QLabel('Joint 3: ', self)
        self.label3.move(0, blank_h*3+title_h+label_h*2)
        self.label3.resize(label_w, label_h)
        self.label3.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.label3.setStyleSheet('color: black; background-color: white')
        self.label3.setAlignment(QtCore.Qt.AlignCenter)

        self.angle3 = QLabel('0', self)
        self.angle3.move(0+label_w, self.label3.y())
        self.angle3.resize(label_w, label_h)
        self.angle3.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.angle3.setStyleSheet('color: black; background-color: white')
        self.angle3.setAlignment(QtCore.Qt.AlignCenter)

        self.label4 = QLabel('Joint 4: ', self)
        self.label4.move(0, blank_h*4+title_h+label_h*3)
        self.label4.resize(label_w, label_h)
        self.label4.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.label4.setStyleSheet('color: black; background-color: white')
        self.label4.setAlignment(QtCore.Qt.AlignCenter)

        self.angle4 = QLabel('0', self)
        self.angle4.move(0+label_w, self.label4.y())
        self.angle4.resize(label_w, label_h)
        self.angle4.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.angle4.setStyleSheet('color: black; background-color: white')
        self.angle4.setAlignment(QtCore.Qt.AlignCenter)

        self.label5 = QLabel('Joint 5: ', self)
        self.label5.move(0, blank_h*5+title_h+label_h*4)
        self.label5.resize(label_w, label_h)
        self.label5.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.label5.setStyleSheet('color: black; background-color: white')
        self.label5.setAlignment(QtCore.Qt.AlignCenter)

        self.angle5 = QLabel('0', self)
        self.angle5.move(0+label_w, self.label5.y())
        self.angle5.resize(label_w, label_h)
        self.angle5.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.angle5.setStyleSheet('color: black; background-color: white')
        self.angle5.setAlignment(QtCore.Qt.AlignCenter)

        self.label6 = QLabel('Joint 6: ', self)
        self.label6.move(0, blank_h*6+title_h+label_h*5)
        self.label6.resize(label_w, label_h)
        self.label6.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.label6.setStyleSheet('color: black; background-color: white')
        self.label6.setAlignment(QtCore.Qt.AlignCenter)

        self.angle6 = QLabel('0', self)
        self.angle6.move(0+label_w, self.label6.y())
        self.angle6.resize(label_w, label_h)
        self.angle6.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.angle6.setStyleSheet('color: black; background-color: white')
        self.angle6.setAlignment(QtCore.Qt.AlignCenter)

        # set the title
        self.title_end = QLabel('End Effector Mode', self)
        self.title_end.move(0, label_h*6+blank_h*7+title_h)
        self.title_end.resize(title_w, title_h)
        self.title_end.setFont(QFont('Ubuntu', 20, QFont.Medium))
        self.title_end.setStyleSheet('color: white; background-color: black')
        self.title_end.setAlignment(QtCore.Qt.AlignCenter)

        # set the label and angle
        self.background_end = QLabel(' ', self)
        self.background_end.move(0, label_h*6+blank_h*7+title_h*2)
        self.background_end.resize(title_w, label_h*4+blank_h*3)
        self.background_end.setStyleSheet('background-color: white')

        self.label7 = QLabel('Label: ', self)
        self.label7.move(0, label_h*6+blank_h*8+title_h*2)
        self.label7.resize(label_w, label_h)
        self.label7.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.label7.setStyleSheet('color: black; background-color: white')
        self.label7.setAlignment(QtCore.Qt.AlignCenter)

        self.end1 = QLabel('Value', self)
        self.end1.move(label_w, self.label7.y())
        self.end1.resize(label_w, label_h)
        self.end1.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.end1.setStyleSheet('color: black; background-color: white')
        self.end1.setAlignment(QtCore.Qt.AlignCenter)

        self.label8 = QLabel('Label: ', self)
        self.label8.move(0, label_h*7+blank_h*9+title_h*2)
        self.label8.resize(label_w, label_h)
        self.label8.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.label8.setStyleSheet('color: black; background-color: white')
        self.label8.setAlignment(QtCore.Qt.AlignCenter)

        self.end2 = QLabel('Value', self)
        self.end2.move(label_w, self.label8.y())
        self.end2.resize(label_w, label_h)
        self.end2.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.end2.setStyleSheet('color: black; background-color: white')
        self.end2.setAlignment(QtCore.Qt.AlignCenter)

        self.label9 = QLabel('Label: ', self)
        self.label9.move(0, label_h*8+blank_h*10+title_h*2)
        self.label9.resize(label_w, label_h)
        self.label9.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.label9.setStyleSheet('color: black; background-color: white')
        self.label9.setAlignment(QtCore.Qt.AlignCenter)

        self.end3 = QLabel('Value', self)
        self.end3.move(label_w, self.label9.y())
        self.end3.resize(label_w, label_h)
        self.end3.setFont(QFont('Ubuntu', 16, QFont.Medium))
        self.end3.setStyleSheet('color: black; background-color: white')
        self.end3.setAlignment(QtCore.Qt.AlignCenter)

        # set the title
        self.title_setting = QLabel('Initial Setting', self)
        self.title_setting.move(title_w+blank_w, btn_h+blank_h)
        self.title_setting.resize(title_w, title_h)
        self.title_setting.setFont(QFont('Sans', 16, QFont.Bold))
        self.title_setting.setStyleSheet('color: black')
        self.title_setting.setAlignment(QtCore.Qt.AlignLeft)

        # set the label and angle
        self.label10 = QLabel('Joint1: ', self)
        self.label10.move(title_w+blank_w, btn_h+title_h+blank_h)
        self.label10.resize(label_w, label_h)
        self.label10.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.label10.setStyleSheet('color: black')
        self.label10.setAlignment(QtCore.Qt.AlignLeft)

        self.text_init1 = QLineEdit('0', self)
        self.text_init1.move(title_w+blank_w+int(label_w/2), self.label10.y())
        self.text_init1.resize(int(label_w/2), int(label_h*2/3))
        self.text_init1.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.text_init1.setStyleSheet('color: black; background-color: white')
        self.text_init1.setAlignment(QtCore.Qt.AlignCenter)

        self.label11 = QLabel('Joint2: ', self)
        self.label11.move(title_w+blank_w, btn_h+title_h+blank_h+label_h)
        self.label11.resize(label_w, label_h)
        self.label11.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.label11.setStyleSheet('color: black')
        self.label11.setAlignment(QtCore.Qt.AlignLeft)

        self.text_init2 = QLineEdit('0', self)
        self.text_init2.move(title_w+blank_w+int(label_w/2), self.label11.y())
        self.text_init2.resize(int(label_w/2), int(label_h*2/3))
        self.text_init2.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.text_init2.setStyleSheet('color: black; background-color: white')
        self.text_init2.setAlignment(QtCore.Qt.AlignCenter)

        self.label12 = QLabel('Joint3: ', self)
        self.label12.move(title_w+blank_w, btn_h+title_h+blank_h+label_h*2)
        self.label12.resize(label_w, label_h)
        self.label12.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.label12.setStyleSheet('color: black')
        self.label12.setAlignment(QtCore.Qt.AlignLeft)

        self.text_init3 = QLineEdit('0', self)
        self.text_init3.move(title_w+blank_w+int(label_w/2), self.label12.y())
        self.text_init3.resize(int(label_w/2), int(label_h*2/3))
        self.text_init3.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.text_init3.setStyleSheet('color: black; background-color: white')
        self.text_init3.setAlignment(QtCore.Qt.AlignCenter)

        self.label13 = QLabel('Joint4: ', self)
        self.label13.move(title_w+blank_w, btn_h+title_h+blank_h+label_h*3)
        self.label13.resize(label_w, label_h)
        self.label13.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.label13.setStyleSheet('color: black')
        self.label13.setAlignment(QtCore.Qt.AlignLeft)

        self.text_init4 = QLineEdit('0', self)
        self.text_init4.move(title_w+blank_w+int(label_w/2), self.label13.y())
        self.text_init4.resize(int(label_w/2), int(label_h*2/3))
        self.text_init4.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.text_init4.setStyleSheet('color: black; background-color: white')
        self.text_init4.setAlignment(QtCore.Qt.AlignCenter)

        self.label14 = QLabel('Joint5: ', self)
        self.label14.move(title_w+blank_w, btn_h+title_h+blank_h+label_h*4)
        self.label14.resize(label_w, label_h)
        self.label14.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.label14.setStyleSheet('color: black')
        self.label14.setAlignment(QtCore.Qt.AlignLeft)

        self.text_init5 = QLineEdit('0', self)
        self.text_init5.move(title_w+blank_w+int(label_w/2), self.label14.y())
        self.text_init5.resize(int(label_w/2), int(label_h*2/3))
        self.text_init5.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.text_init5.setStyleSheet('color: black; background-color: white')
        self.text_init5.setAlignment(QtCore.Qt.AlignCenter)

        self.label15 = QLabel('Joint6: ', self)
        self.label15.move(title_w+blank_w, btn_h+title_h+blank_h+label_h*5)
        self.label15.resize(label_w, label_h)
        self.label15.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.label15.setStyleSheet('color: black')
        self.label15.setAlignment(QtCore.Qt.AlignLeft)

        self.text_init6 = QLineEdit('0', self)
        self.text_init6.move(title_w+blank_w+int(label_w/2), self.label15.y())
        self.text_init6.resize(int(label_w/2), int(label_h*2/3))
        self.text_init6.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.text_init6.setStyleSheet('color: black; background-color: white')
        self.text_init6.setAlignment(QtCore.Qt.AlignCenter)

        self.label16 = QLabel('Kp: ', self)
        self.label16.move(title_w+blank_w*2+label_w, btn_h+title_h+blank_h)
        self.label16.resize(label_w, label_h)
        self.label16.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.label16.setStyleSheet('color: black')
        self.label16.setAlignment(QtCore.Qt.AlignLeft)

        self.text_init7 = QLineEdit('0', self)
        self.text_init7.move(title_w+blank_w*2+int(label_w*3/2), self.label16.y())
        self.text_init7.resize(int(label_w/2), int(label_h*2/3))
        self.text_init7.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.text_init7.setStyleSheet('color: black; background-color: white')
        self.text_init7.setAlignment(QtCore.Qt.AlignCenter)

        self.label17 = QLabel('Ki: ', self)
        self.label17.move(title_w+blank_w*2+label_w, btn_h+title_h+blank_h+label_h)
        self.label17.resize(label_w, label_h)
        self.label17.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.label17.setStyleSheet('color: black')
        self.label17.setAlignment(QtCore.Qt.AlignLeft)

        self.text_init8 = QLineEdit('0', self)
        self.text_init8.move(title_w+blank_w*2+int(label_w*3/2), self.label17.y())
        self.text_init8.resize(int(label_w/2), int(label_h*2/3))
        self.text_init8.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.text_init8.setStyleSheet('color: black; background-color: white')
        self.text_init8.setAlignment(QtCore.Qt.AlignCenter)

        self.label18 = QLabel('Kd: ', self)
        self.label18.move(title_w+blank_w*2+label_w, btn_h+title_h+blank_h+label_h*2)
        self.label18.resize(label_w, label_h)
        self.label18.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.label18.setStyleSheet('color: black')
        self.label18.setAlignment(QtCore.Qt.AlignLeft)

        self.text_init9 = QLineEdit('0', self)
        self.text_init9.move(title_w+blank_w*2+int(label_w*3/2), self.label18.y())
        self.text_init9.resize(int(label_w/2), int(label_h*2/3))
        self.text_init9.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.text_init9.setStyleSheet('color: black; background-color: white')
        self.text_init9.setAlignment(QtCore.Qt.AlignCenter)

        self.label19 = QLabel('Speed: ', self)
        self.label19.move(title_w+blank_w*2+label_w, btn_h+title_h+blank_h+label_h*3)
        self.label19.resize(label_w, label_h)
        self.label19.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.label19.setStyleSheet('color: black')
        self.label19.setAlignment(QtCore.Qt.AlignLeft)

        self.text_init10 = QLineEdit('0', self)
        self.text_init10.move(title_w+blank_w*2+int(label_w*3/2), self.label19.y())
        self.text_init10.resize(int(label_w/2), int(label_h*2/3))
        self.text_init10.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.text_init10.setStyleSheet('color: black; background-color: white')
        self.text_init10.setAlignment(QtCore.Qt.AlignCenter)

        # set the title
        self.title_info = QLabel('Information', self)
        self.title_info.move(title_w+blank_w, btn_h*2+blank_h*2+title_h+label_h*6)
        self.title_info.resize(title_w, title_h)
        self.title_info.setFont(QFont('Sans', 16, QFont.Bold))
        self.title_info.setStyleSheet('color: black')
        self.title_info.setAlignment(QtCore.Qt.AlignLeft)

        # set the label and angle
        self.label20 = QLabel('Information is written here ...', self)
        self.label20.move(title_w+blank_w, btn_h*2+blank_h*2+title_h*2+label_h*6)
        self.label20.resize(label_w*2, label_h*40)
        self.label20.setFont(QFont('Ubuntu', 10))
        self.label20.setStyleSheet('color: black')
        self.label20.setAlignment(QtCore.Qt.AlignLeft)


        # set button
        self.btn_robot_conn = QPushButton('Robot Connect', self)
        self.btn_robot_conn.move(title_w+blank_w, 0)
        self.btn_robot_conn.resize(btn_w, btn_h)
        self.btn_robot_conn.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.btn_robot_conn.setStyleSheet('background-color: Pink;')
        self.btn_robot_conn.clicked.connect(self.robot_connect)

        self.btn_joystick_conn = QPushButton('Joystick Connect', self)
        self.btn_joystick_conn.move(title_w+blank_w*2+btn_w, 0)
        self.btn_joystick_conn.resize(btn_w, btn_h)
        self.btn_joystick_conn.setFont(QFont('Ubuntu', 11, QFont.Medium))
        self.btn_joystick_conn.setStyleSheet('background-color: Pink;')
        self.btn_joystick_conn.clicked.connect(self.joystick_connect)

        self.btn_angle1 = QPushButton('Reset', self)
        self.btn_angle1.move(label_w*2+int(blank_w/2), self.label1.y())
        self.btn_angle1.resize(int(label_w/2), label_h)
        self.btn_angle1.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.btn_angle1.setStyleSheet('color: black; background-color: ash gray')
        self.btn_angle1.clicked.connect(lambda: self.reset_angle(1))

        self.btn_angle2 = QPushButton('Reset', self)
        self.btn_angle2.move(label_w*2+int(blank_w/2), self.label2.y())
        self.btn_angle2.resize(int(label_w/2), label_h)
        self.btn_angle2.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.btn_angle2.setStyleSheet('color: black; background-color: ash gray')
        self.btn_angle2.clicked.connect(lambda: self.reset_angle(2))

        self.btn_angle3 = QPushButton('Reset', self)
        self.btn_angle3.move(label_w*2+int(blank_w/2), self.label3.y())
        self.btn_angle3.resize(int(label_w/2), label_h)
        self.btn_angle3.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.btn_angle3.setStyleSheet('color: black; background-color: ash gray')
        self.btn_angle3.clicked.connect(lambda: self.reset_angle(3))

        self.btn_angle4 = QPushButton('Reset', self)
        self.btn_angle4.move(label_w*2+int(blank_w/2), self.label4.y())
        self.btn_angle4.resize(int(label_w/2), label_h)
        self.btn_angle4.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.btn_angle4.setStyleSheet('color: black; background-color: ash gray')
        self.btn_angle4.clicked.connect(lambda: self.reset_angle(4))

        self.btn_angle5 = QPushButton('Reset', self)
        self.btn_angle5.move(label_w*2+int(blank_w/2), self.label5.y())
        self.btn_angle5.resize(int(label_w/2), label_h)
        self.btn_angle5.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.btn_angle5.setStyleSheet('color: black; background-color: ash gray')
        self.btn_angle5.clicked.connect(lambda: self.reset_angle(5))

        self.btn_angle6 = QPushButton('Reset', self)
        self.btn_angle6.move(label_w*2+int(blank_w/2), self.label6.y())
        self.btn_angle6.resize(int(label_w/2), label_h)
        self.btn_angle6.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.btn_angle6.setStyleSheet('color: black; background-color: ash gray')
        self.btn_angle6.clicked.connect(lambda: self.reset_angle(6))

        self.btn_save = QPushButton('Save', self)
        self.btn_save.move(title_w+blank_w, btn_h+blank_h+title_h+label_h*6)
        self.btn_save.resize(int(btn_w*2/3), btn_h)
        self.btn_save.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.btn_save.setStyleSheet('background-color: Skyblue;')
        self.btn_save.clicked.connect(self.save_setting)

        self.btn_load = QPushButton('Load', self)
        self.btn_load.move(title_w+int(blank_w*3/2)+int(btn_w*2/3), btn_h+blank_h+title_h+label_h*6)
        self.btn_load.resize(int(btn_w*2/3), btn_h)
        self.btn_load.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.btn_load.setStyleSheet('background-color: Skyblue;')
        self.btn_load.clicked.connect(self.load_setting)

        self.btn_clean = QPushButton('Clean', self)
        self.btn_clean.move(title_w+blank_w*2+int(btn_w*4/3), btn_h+blank_h+title_h+label_h*6)
        self.btn_clean.resize(int(btn_w*2/3), btn_h)
        self.btn_clean.setFont(QFont('Ubuntu', 12, QFont.Medium))
        self.btn_clean.setStyleSheet('background-color: Skyblue;')
        self.btn_clean.clicked.connect(self.clean_setting)

        # set timers to update
        self.timer_read = QtCore.QTimer()
        self.timer_read.timeout.connect(self.read_joystick)
        self.timer_read.start(80)
        self.timer_move = QtCore.QTimer()
        self.timer_move.timeout.connect(self.move_robot)
        self.timer_move.start(200)
        self.timer_recieve = QtCore.QTimer()
        self.timer_recieve.timeout.connect(self.recieve_robot)
        self.timer_recieve.start(1)

        # create the window
        self.setStyleSheet("background-color: Lightgray;")
        self.setGeometry(200, 200, win_w, win_h)
        self.show()

    def robot_connect(self):
        if self.robot_conn == False:
            move_robot.connect()
            self.btn_robot_conn.setText('Robot Connected')
            self.btn_robot_conn.setFont(QFont('Ubuntu', 11, QFont.Medium))
            self.btn_robot_conn.setStyleSheet('color: black; background-color: Lightgreen')
            self.robot_conn = True
            time.sleep(0.5)

        else:
            move_robot.disconnect()
            self.btn_robot_conn.setText('Robot Connect')
            self.btn_robot_conn.setFont(QFont('Ubuntu', 12, QFont.Medium))
            self.btn_robot_conn.setStyleSheet('color: black; background-color: pink')
            self.robot_conn = False
            time.sleep(0.5)

    def joystick_connect(self):
        if self.joystick_conn == False:
            self.btn_joystick_conn.setText('Joystick Connected')
            self.btn_joystick_conn.setFont(QFont('Ubuntu', 10, QFont.Medium))

            conn = read_joystick.connect()
            if conn == True:
                self.btn_joystick_conn.setStyleSheet('color: black; background-color: Lightgreen')
                self.btn_joystick_conn.setFont(QFont('Ubuntu', 10, QFont.Medium))
                self.joystick_conn = True
                time.sleep(0.5)

        else:
            self.btn_joystick_conn.setText('Joystick Connect')
            self.btn_joystick_conn.setFont(QFont('Ubuntu', 11, QFont.Medium))

            disconn = read_joystick.disconnect()
            if disconn == True:
                self.btn_joystick_conn.setStyleSheet('color: black; background-color: pink')
                self.btn_joystick_conn.setFont(QFont('Ubuntu', 10, QFont.Medium))
                self.joystick_conn = False
                time.sleep(0.5)

    def reset_angle(self, n):
        if self.joystick_conn == True and self.robot_conn == False:
            self.init_pose[n-1] = read_joystick.init_angle()[n-1]

    def read_joystick(self):
        if self.joystick_conn == True:
            angle_list = read_joystick.read_angle(self, self.init_pose)
            if len(angle_list) == 9:
                self.angle1.setText(str(angle_list[0]))
                self.angle2.setText(str(angle_list[1]))
                self.angle3.setText(str(angle_list[2]))
                self.angle4.setText(str(angle_list[3]))
                self.angle5.setText(str(angle_list[4]))
                self.angle6.setText(str(angle_list[5]))
                
    def recieve_robot(self):
        if self.robot_conn == True:
            s_ = move_robot.s_
            s_r = s_.recv(2048).decode().split(',')
            try:
                self.label20.setText('joint1: {}\njoint2: {}\njoint3: {}\njoint4: {}\njoint5: {}\njoint6: {}\n'\
                    .format(s_r[4].split('{')[1], s_r[5], s_r[6], s_r[7], s_r[8], s_r[9].split('}')[0]))            
            except:
                pass



    def move_robot(self):
        if self.joystick_conn == True and self.robot_conn == True:
            n1 = -float(self.angle1.text())+float(self.text_init1.text())
            n2 = float(self.angle2.text())+float(self.text_init2.text())
            n3 = -float(self.angle3.text())+float(self.text_init3.text())
            n4 = -float(self.angle5.text())+float(self.text_init4.text())
            n5 = float(self.angle4.text())+float(self.text_init5.text())
            n6 = -float(self.angle6.text())+float(self.text_init6.text())
            index = self.index
            self.index += 1
            s = move_robot.s
            

            cmd_str = move_robot.cmd_ptp(n1,n2,n3,n4,n5,n6,index)
            cmd = bytes(cmd_str,"utf-8")
            print(cmd_str)
            s.send(cmd)
            # print(s.recv(2048))


    def save_setting(self):
        input_data = {
            self.label10.text().rstrip(": "): self.text_init1.text(),
            self.label11.text().rstrip(": "): self.text_init2.text(),
            self.label12.text().rstrip(": "): self.text_init3.text(),
            self.label13.text().rstrip(": "): self.text_init4.text(),
            self.label14.text().rstrip(": "): self.text_init5.text(),
            self.label15.text().rstrip(": "): self.text_init6.text(),
            self.label16.text().rstrip(": "): self.text_init7.text(),
            self.label17.text().rstrip(": "): self.text_init8.text(),
            self.label18.text().rstrip(": "): self.text_init9.text(),
            self.label19.text().rstrip(": "): self.text_init10.text(),
        }

        f_name = QFileDialog.getSaveFileName(self, 'Save File', "Initial_pose", "JSON (*.json)")
        if '.json' not in f_name[0]:
            f_name = f_name[0] + '.json'
        else:
            f_name = f_name[0]
        with open(f_name, 'w') as outfile:
            json.dump(input_data, outfile)
            outfile.close()    

    def load_setting(self):
        global f
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        f_name, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","JSON Files (*.json)", options=options)
        if f_name:
            f = open(str(f_name))
        data = json.load(f)   

        self.text_init1.setText(data[self.label10.text().rstrip(": ")])
        self.text_init2.setText(data[self.label11.text().rstrip(": ")])
        self.text_init3.setText(data[self.label12.text().rstrip(": ")])
        self.text_init4.setText(data[self.label13.text().rstrip(": ")])
        self.text_init5.setText(data[self.label14.text().rstrip(": ")])
        self.text_init6.setText(data[self.label15.text().rstrip(": ")])
        self.text_init7.setText(data[self.label16.text().rstrip(": ")])
        self.text_init8.setText(data[self.label17.text().rstrip(": ")])
        self.text_init9.setText(data[self.label18.text().rstrip(": ")])
        self.text_init10.setText(data[self.label19.text().rstrip(": ")])

    def clean_setting(self):
        self.text_init1.setText('0')
        self.text_init2.setText('0')
        self.text_init3.setText('0')
        self.text_init4.setText('0')
        self.text_init5.setText('0')
        self.text_init6.setText('0')
        self.text_init7.setText('0')
        self.text_init8.setText('0')
        self.text_init9.setText('0')
        self.text_init10.setText('0')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myGUI()
    sys.exit(app.exec_())