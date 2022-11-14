from bankaccount import BankAccount

def test_insufficient_funds_on_withdraw():
    account = BankAccount('Jurian')
    assert account.withdraw(100) == False

def test_sufficient_funds_on_deposit():
    account = BankAccount('Jurian')
    account.deposit(1000)
    assert account.withdraw(50) == True

def test_deposit():
    account = BankAccount('Jurian')
    assert account.deposit(-1000) == False

# test_insufficient_funds_on_withdraw()
# test_sufficient_funds_on_deposit()
# test_deposit()
