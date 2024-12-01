import sys
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QMainWindow, QPushButton, QSlider, QLabel, QGridLayout


class WindowsCredit(QMainWindow):
    def __init__(self, main_link, *args):
        super().__init__()
        self.initUI()
        self.year = 2024
        self.main_link = main_link

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Кредит')

        self.grid = QGridLayout()

        # WindowsCredit.setLayout(self.grid)

        self.backToMainbtn = QPushButton()
        self.backToMainbtn.setText("return")
        self.backToMainbtn.clicked.connect(self.ReturnToMain)

        self.slider = QSlider(QtCore.Qt.Orientation.Horizontal)
        self.slider.setRange(-2000000, 2000000)
        # self.slider.setGeometry(70, 70, 100, 30)
        self.slider.setValue(50)
        self.slider.setSingleStep(100)
        self.slider.setPageStep(10)
        self.slider.setTickInterval(10000)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)

        self.grid.addWidget(self.backToMainbtn, 0, 0)
        self.grid.addWidget(self.slider, 1, 0)

        self.show()

    def ReturnToMain(self):
        WindowsCredit.close(self)
        self.main_link.show()

    def slider_change(self):
        self.year += 1
        self.count.setText(f"{self.year}")

