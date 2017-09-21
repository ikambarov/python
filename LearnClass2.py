import datetime


class Banking:

    # Static method, should not be edited from outside of class
    @staticmethod
    def _check_date():
        return datetime.datetime.utcnow()

    # Static variables, should not be edited from outside of class
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdrawal(self, amount):
        if 0 < amount < self._balance:
            self._balance -= amount
        else:
            print("Account cannot be overdrawn")
            self.show_balance()

    def show_balance(self):
        print("Current balance is {}, {}".format(self._balance, self._check_date()))


TCF = Banking("islam", 1000)
TCF.show_balance()

TCF.deposit(1250)
TCF.show_balance()

TCF.withdrawal(250)
TCF.show_balance()

TCF.withdrawal(1000)
TCF.show_balance()

TCF.withdrawal(10000)

