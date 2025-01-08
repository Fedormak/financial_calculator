import sys
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QSlider, QAbstractSlider, QLabel

from dataBD import dataBD



class WindowsCalculator(QMainWindow):
    def __init__(self, main_link,*args):
        super().__init__()
        self.date = dataBD()
        self.initUI()
        self.main_link = main_link

    def initUI(self):
        uic.loadUi("./ui/windowsUsers.ui", self)
        print(self.date.allUser())
        self.Users.addItems(self.date.allUser())

        self.backToMainbtn.clicked.connect(self.ReturnToMain)

    def ReturnToMain(self):
        WindowsCalculator.close(self)
        self.main_link.show()
