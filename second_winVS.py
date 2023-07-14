from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
from instrVS import *
from final_winVS import *

class Experiment():
    def __init__(self, age , t1, t2, t3):
        self.age = age
        self.t1 = t1
        self.t2 = t2 
        self.t3 = t3
        
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.txt_name_label = QLabel(txt_name)
        self.inp_name_qline = QLineEdit(txt_hintname)
        self.txt_age_label = QLabel(txt_age)
        self.inp_age_qline = QLineEdit(txt_hintage)
        self.txt_test1_label = QLabel(txt_test1)
        self.btn_test1_qbtn = QPushButton(txt_starttest1)
        self.reslut_test1_qline = QLineEdit(txt_hinttest1)
        self.txt_test2_label = QLabel(txt_test2)
        self.btn_test2_qbtn = QPushButton(txt_starttest2)
        self.reslut_test2_qline = QLineEdit(txt_hinttest2)
        self.txt_test3_label = QLabel(txt_test3)
        self.btn_test3_qbtn = QPushButton(txt_starttest3)
        self.reslut_test3_qline = QLineEdit(txt_hinttest3)
        self.btn_next_qbtn = QPushButton(txt_sendresults)
        self.timer_label = QLabel(txt_timer)


        self.l_line.addWidget(self.txt_name_label, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.inp_name_qline, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_age_label, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.inp_age_qline, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test1_label, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1_qbtn, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.reslut_test1_qline, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test2_label, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2_qbtn, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.reslut_test2_qline, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test3_label, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3_qbtn, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.reslut_test3_qline, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next_qbtn, alignment = Qt.AlignCenter)

        self.r_line.addWidget(self.timer_label, alignment = Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def timer_test1(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_label.setText(time.toString('hh:mm:ss'))
        self.timer_label.setFont(QFont("Times", 36, QFont.Bold))
        self.timer_label.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    
    def timer_test2(self):
        global time
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_label.setText(time.toString('hh:mm:ss')[6:8])
        self.timer_label.setFont(QFont("Times", 36, QFont.Bold))
        self.timer_label.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_test3(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_label.setText(time.toString('hh:mm:ss'))
        self.timer_label.setFont(QFont("Times", 36, QFont.Bold))
        self.timer_label.setStyleSheet('color: rgb(0,0,0)')
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.timer_label.setStyleSheet('color: rgb(0,255,0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.timer_label.setStyleSheet('color: rgb(0,255,0)')
        else:
            self.timer_label.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.inp_age_qline.text()), int(self.reslut_test1_qline.text()), 
        int(self.reslut_test2_qline.text()), int(self.reslut_test3_qline.text()))
        self.tw = FinalWin(self.exp)
        
    def connects(self):
        self.btn_next_qbtn.clicked.connect(self.next_click)
        self.btn_test1_qbtn.clicked.connect(self.timer_test1)
        self.btn_test2_qbtn.clicked.connect(self.timer_test2)
        self.btn_test3_qbtn.clicked.connect(self.timer_test3)