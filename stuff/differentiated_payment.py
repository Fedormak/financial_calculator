import datetime
from calendar import monthrange

class differentiated_payment:
    def __init__(self):
        self.monthN = datetime.datetime.now().month
        current_year = datetime.datetime.now().year
        self.beforpayment = 0

        self.daysMonth = monthrange(current_year, self.monthN)
        # self.daysYear = sum(map(lambda x: monthrange(current_year, x), range(1, 13)))
        self.daysYear = (datetime.date(current_year, 12, 31) - datetime.date(current_year, 1, 1)).days + 1

        self.daysMonth = int(self.daysMonth[1])

    def payment(self, sumCredit=None, month=None, percent=None, pay_off=None ):
        percent = percent / 100
        St = sumCredit / month
        if pay_off == 0:
            Ln = (float(sumCredit) * float(percent) * float(self.daysMonth)) / self.daysYear
            payment = St + Ln
            self.beforpayment = payment
        else:
            Ln = ((sumCredit - self.beforpayment * pay_off) * percent * self.daysMonth) / self.daysYear
            payment = St + Ln
            self.beforpayment = payment
        return round(payment, 2)


