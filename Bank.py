class Bank:
    def __init__(self, name, account_no, balance):
        self._name = name
        self.__account_no = account_no
        self._balance = balance
    def deposit(self, amount):
        self._balance = self._balance + amount
    def withdraw(self, amount):
        self._balance = self._balance - amount
    def display(self):
        print(self._name, self.__account_no, self._balance)

b = Bank("likku", 123456789, 85000)
print(b._Bank__account_no)
b.deposit(4000)
b.withdraw(5000)
b.display()
    
