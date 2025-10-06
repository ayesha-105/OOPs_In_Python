'''Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance.'''

class Account:
    def __init__(self, acc_no, balance):
        self.acc_no= acc_no
        self.balance= balance

    def debit(self, amount):
        self.balance-= amount
        print(f"Rs. {amount} was debited from your account.")
        print(f"Your total balance is Rs. {self.balance}")

    def credit(self, amount):
        self.balance+= amount
        print(f"Rs. {amount} was credited to your account.")
        print(f"Your total balance is Rs. {self.balance}")


acc1= Account(12345, 5000)
acc1.debit(2000)
acc1.credit(1000)
acc1.credit(20000)
acc1.debit(15000)