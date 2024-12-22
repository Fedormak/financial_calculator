import sys
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QMainWindow, QPushButton, QSlider, QLabel, QGridLayout

from stuff.annuity_payment import annuity_payment


class WindowsCredit(QMainWindow):
    def __init__(self, main_link, *args):
        super().__init__()
        self.month = 1
        self.sumCredit = 500
        self.main_link = main_link


        self.initUI()
        self.number = annuity_payment()

    def initUI(self):
        uic.loadUi("./ui/windowsCredit.ui", self)

        self.monthSlider.valueChanged.connect(self.monthSliderChenge)

        self.sumCreditSlider.valueChanged.connect(self.sumCreditSliderChenge)
        self.sumCreditSlider.setSingleStep(500)
        self.sumCreditSlider.setPageStep(500)
        self.sumCreditSlider.setMaximum(100000)

        self.reload()

        self.calculate.clicked.connect(self.Calculate)
        self.backToMainbtn.clicked.connect(self.ReturnToMain)

    def reload(self):
        self.monthSlider.setValue(self.month)
        self.sumCreditSlider.setValue(self.sumCredit)

    def monthSliderChenge(self):
        self.monthSliderNum.setText(f"{self.monthSlider.value()}")

    def sumCreditSliderChenge(self):
        self.sumCreditSliderNum.setText(f"{self.sumCreditSlider.value()}")

    def ReturnToMain(self):
        WindowsCredit.close(self)
        self.main_link.show()

    def Calculate(self):
        payment = self.number.payment(sumCredit=self.sumCreditSlider.value(), month=self.monthSlider.value(),
                            percent=self.percent.value())

        self.payment.display(payment)


