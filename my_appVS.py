from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instrVS import *
from second_winVS import * 


class MainWin(QWidget):
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
        self.hello_txt = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        
        self.screen_size = QLabel(txt_win)

        self.layout.addWidget(self.screen_size, alignment = Qt.AlignRight)
        self.layout.addWidget(self.hello_txt, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.button, alignment = Qt.AlignCenter )
        self.setLayout(self.layout)
        
    def next_click(self):
        self.hide()
        self.tw = TestWin()

    def connects(self):
        self.button.clicked.connect(self.next_click)

app = QApplication([])
mw = MainWin()
app.exec_()



