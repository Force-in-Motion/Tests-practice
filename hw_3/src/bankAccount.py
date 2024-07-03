class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError('Получен не верный тип данных, ожидалось целое или дробное число')

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError('Получен не верный тип данных, ожидалось целое или дробное число')

        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance