import sys
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QMainWindow, QPushButton, QSlider, QLabel, QGridLayout

from stuff.annuity_payment import annuity_payment
from stuff.differentiated_payment import differentiated_payment


class WindowsCredit(QMainWindow):
    def __init__(self, main_link, *args):
        super().__init__()
        self.month = 1
        self.sumCredit = 500
        self.main_link = main_link
        self.differ = False


        self.initUI()
        self.number = annuity_payment()

    def initUI(self):
        uic.loadUi("./ui/windowsCredit.ui", self)

        self.paid_off_text.setVisible(self.differ)
        self.paid_offHorizontalSlider.setVisible(self.differ)
        self.paid_offCount.setVisible(self.differ)

        self.paid_offHorizontalSlider.setMaximum(36)
        self.paid_offHorizontalSlider.valueChanged.connect(self.paid_offHorizontalSliderChenge)
        self.paid_offHorizontalSlider.setSingleStep(1)
        self.paid_offHorizontalSlider.setPageStep(1)

        self.monthSlider.valueChanged.connect(self.monthSliderChenge)
        self.monthSlider.setSingleStep(3)
        self.monthSlider.setPageStep(3)

        self.sumCreditSlider.valueChanged.connect(self.sumCreditSliderChenge)
        self.sumCreditSlider.setSingleStep(100)
        self.sumCreditSlider.setPageStep(100)
        self.sumCreditSlider.setMaximum(10000)

        self.reload()

        self.comboBox.currentTextChanged.connect(self.ChengeTypeCredit)
        self.calculate.clicked.connect(self.Calculate)
        self.backToMainbtn.clicked.connect(self.ReturnToMain)

    def ChengeTypeCredit(self):
        if self.differ:
            self.differ = False
            self.number = annuity_payment()
        else:
            self.differ = True
            self.number = differentiated_payment()

        self.paid_off_text.setVisible(self.differ)
        self.paid_offHorizontalSlider.setVisible(self.differ)
        self.paid_offCount.setVisible(self.differ)
        self.payment.setText(str(00000))
        self.overpayments.setText(str(00000))


    def reload(self):
        self.monthSlider.setValue(self.month)
        self.sumCreditSlider.setValue(self.sumCredit)

    def paid_offHorizontalSliderChenge(self):
        self.paid_offCount.setText(f"{self.paid_offHorizontalSlider.value()}")

    def monthSliderChenge(self):
        self.monthSliderNum.setText(f"{self.monthSlider.value()}")

    def sumCreditSliderChenge(self):
        self.sumCreditSliderNum.setText(f"{self.sumCreditSlider.value()}")

    def ReturnToMain(self):
        WindowsCredit.close(self)
        self.main_link.show()

    def Calculate(self):
        if self.monthSlider.value() > self.paid_offHorizontalSlider.value():
            payment, overpayment = self.number.payment(sumCredit=self.sumCreditSlider.value(), month=self.monthSlider.value(),
                            percent=self.percent.value(), pay_off=self.paid_offHorizontalSlider.value())

            self.payment.setText(str(payment))

            self.overpayments.setText(f"{overpayment}")
        else:
            self.payment.setText("Error")
            self.overpayments.setText("Error")
