import sys
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QSlider, QAbstractSlider, QLabel


class WindowsCredit(QMainWindow):
    def __init__(self, main_link, *args):
        super().__init__()
        self.initUI()
        self.year = 2024
        self.main_link = main_link

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Кредит')

        self.count = QLabel()
        self.slider = QSlider(QtCore.Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.setCentralWidget(self.count)
        self.setCentralWidget(self.slider)

        self.backToMainbtn = QPushButton(self)
        self.backToMainbtn.setText("return")
        self.backToMainbtn.clicked.connect(self.ReturnToMain)

    def ReturnToMain(self):
        WindowsCredit.close(self)
        self.main_link.show()

    def slider_change(self):
        self.year += 1
        self.count.setText(f"{self.year}")

