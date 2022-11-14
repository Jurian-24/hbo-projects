class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            return False

        self.balance += amount
        return True

    def withdraw(self, amount):
        if self.balance < amount:
            return False

        self.balance -= amount
        return True
