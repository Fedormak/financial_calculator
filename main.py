import sys

from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QGridLayout, QPushButton

from dataBD import dataBD
from windows.windowsCredit import WindowsCredit
from windows.WindowsUsers import WindowsCalculator


class mainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user = "Makarov"
        self.bd = dataBD()

        self.initUI()

    def initUI(self):
        if self.user is None:
            uic.loadUi("./ui/login.ui", self)
            self.logInbut.clicked.connect(self.regiserName)


        else:
            uic.loadUi("./ui/mainWindows.ui", self)
            self.MoveCredit.clicked.connect(self.MoveCreditfunc)
            self.MoveCalculator.clicked.connect(self.MoveCalculatorfunc)

    def regiserName(self):
        if self.bd.searchUser(self.user_registr.text()):
            self.user = self.user_registr.text()

            uic.loadUi("./ui/mainWindows.ui", self)
            
            self.MoveCredit.clicked.connect(self.MoveCreditfunc)
            self.MoveCalculator.clicked.connect(self.MoveCalculatorfunc)
        else:
            self.label.setText("Error")


    def MoveCreditfunc(self):
        main_link = Windows.hide()
        self.WindowsCredit = WindowsCredit(self, main_link)
        self.WindowsCredit.show()

    def MoveCalculatorfunc(self):
        main_link = Windows.hide()
        self.WindowsCalculator = WindowsCalculator(self, main_link)
        self.WindowsCalculator.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Windows = mainWindows()
    Windows.show()
    sys.exit(app.exec())