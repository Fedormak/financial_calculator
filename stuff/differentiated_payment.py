import datetime
from calendar import monthrange

class differentiated_payment:
    def __init__(self):
        self.monthN = datetime.datetime.now().month
        current_year = datetime.datetime.now().year

        self.daysMonth = monthrange(current_year, self.monthN)
        self.daysYear = (datetime.date(current_year, 12, 31) - datetime.date(current_year, 1, 1)).days + 1

        self.daysMonth = int(self.daysMonth[1])

    def payment(self, sumCredit=None, month=None, percent=None, pay_off=0 ):
        percent = percent / 100

        history_payment = list()
        St = sumCredit / month
        overpayment = 0
        for i in range(month):
            if i == 0:
                Ln = sumCredit * percent * (30 / self.daysYear)
                overpayment += Ln
                payment = round((St + Ln) * 1000, 2)
                sumCredit = sumCredit - St
                history_payment.append(payment)
            else:

                Ln = sumCredit * percent * (30 / self.daysYear)
                overpayment += Ln

                payment = round((St + Ln) * 1000, 2)
                history_payment.append(payment)
                sumCredit = sumCredit - St

        print(history_payment)

        payment = history_payment[pay_off]
        return payment, round(overpayment * 1000, 2)


