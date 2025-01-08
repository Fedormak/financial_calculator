
class annuity_payment:

    def payment(self, sumCredit=None, month=None, percent=None, pay_off=None):
        percent = percent / 12
        percent = percent / 100
        kof = (percent * ((1 + percent) ** month)) / (((1 + percent) ** month) - 1)
        payment = sumCredit * kof
        overpayment = payment * month - sumCredit
        return round(payment * 1000, 2), round(overpayment * 1000, 2)


