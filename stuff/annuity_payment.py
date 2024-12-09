
class annuitypayment:
    def _-

    def kof_annuity(self):

    def monthly_fee(self, sum_credit):
        return sum_credit * self.kof_annuity

    def monthlsdfy_fee(self, loan_amount=None, month=None, percent=None ):
        percent = percent / 12
        monthly_fee = loan_amount * (percent + percent / ((1 + percent) ** month - 1))
        return monthly_fee


d = annuitypayment()
print(d.monthly_fee(float(input()), float(input()), float(input())))