from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
from instrVS import *
from second_winVS import *


class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def results(self):
        if self.exp.age < 7:
            self.index = 0
            return "Результаты по возрасту младше 7 лет отсутствуют."
        self.index = (4*((self.exp.t1)+(self.exp.t2)+(self.exp.t3))-200)/10        
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age < 15 and self.exp.age > 12:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age <= 12 and self.exp.age >= 11:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age <= 10 and self.exp.age >= 9:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age <= 8 and self.exp.age >= 7:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5

            
    def initUI(self):
        self.v_line = QVBoxLayout()

        self.work_label = QLabel(txt_workheart + self.results())
        self.index_label = QLabel(txt_index + str(self.index))
        self.button1 = QPushButton(txt_win1)

        self.v_line.addWidget(self.index_label, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.work_label, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.button1, alignment = Qt.AlignCenter)

        self.setLayout(self.v_line)

    def next_click(self):
        self.hide()
        self.tw

    def connects(self):
        self.button1.clicked.connect(self.next_click)

            