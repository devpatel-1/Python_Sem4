class BankAccount:
    
    total_accounts = 0   # Class variable

    def __init__(self, acc_no, balance):
        self.__account_number = acc_no   # Private attribute
        self.__balance = balance         # Private attribute
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        print("Balance:", self.__balance)

    @staticmethod
    def bank_statistics():
        print("Total accounts:", BankAccount.total_accounts)


# Creating objects
acc1 = BankAccount(101, 5000)
acc2 = BankAccount(102, 3000)

acc1.deposit(1000)
acc1.withdraw(2000)
acc1.get_balance()

# Calling static method
BankAccount.bank_statistics()