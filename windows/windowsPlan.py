import sys
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QSlider, QAbstractSlider, QLabel



class WindowsPlan(QMainWindow):
    def __init__(self, main_link,*args):
        super().__init__()
        self.initUI()
        self.main_link = main_link

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Вклад')

        self.backToMainbtn = QPushButton(self)
        self.backToMainbtn.setText("return")
        self.backToMainbtn.clicked.connect(self.ReturnToMain)

    def ReturnToMain(self):
        WindowsPlan.close(self)
        self.main_link.show()
