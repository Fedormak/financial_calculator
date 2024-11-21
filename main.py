import sys


from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QGridLayout

from dataBD import dataBD
from windows.windowsCredit import WindowsCredit
from windows.windowsPercent import WindowsPercent
from windows.windowsPlan import WindowsPlan


class mainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user = None
        self.bd = dataBD()

        self.initUI()

    def initUI(self):
        if self.user is None:
            self.label = QLabel(self)
            self.label.setText("Ваше имя сэр?")
            self.user_registr = QLineEdit(self)
            self.user_registr.textChanged.connect(self.regiserName)
            self.user_registr.move(100, 100)

            self.setFixedSize(300, 300)
            self.setWindowTitle('Log in')

        else:
            uic.loadUi("./ui/mainWindows.ui", self)
            self.MoveCredit.clicked.connect(self.MoveCreditfunc)
            self.MovePercent.clicked.connect(self.MovePercentfunc)
            self.MovePlan.clicked.connect(self.MovePlanfunc)

    def regiserName(self, text):
        if self.bd.searchUser(text):
            self.user = text


    def MoveCreditfunc(self):
        main_link = Windows.hide()
        self.WindowsCredit = WindowsCredit(self, main_link)
        self.WindowsCredit.show()

    def MovePercentfunc(self):
        main_link = Windows.hide()
        self.WindowsPercent = WindowsPercent(self, main_link)
        self.WindowsPercent.show()

    def MovePlanfunc(self):
        main_link = Windows.hide()
        self.WindowsPlan = WindowsPlan(self, main_link)
        self.WindowsPlan.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Windows = mainWindows()
    Windows.show()
    sys.exit(app.exec())