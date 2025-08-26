class BankAccount: 
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            err = "cannot deposit zero or negative funds"
            raise ValueError(err)
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if self.__balance <= 0 or self.__balance < amount:
            err = "insufficient funds"
            raise ValueError(err) 
        elif amount <= 0:
            err1 = "cannot withdraw zero or negative funds"            
            raise ValueError(err1)
        else:
            self.__balance -= amount
