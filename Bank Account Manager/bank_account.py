from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, number):
        pass

    @abstractmethod
    def withdraw(self, number):
        pass

    def display_balance(self):
        print(f"Account number: {self.account_number}\nBalance: {self.balance:.2f}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount:.2f} into Checking Account")

    def withdraw(self, amount):
        if self.balance - amount >= self.overdraft_limit and amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount:.2f} from Checking Account")
        else:
            print("Insufficient funds. Cannot withdraw")


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount:.2f} into Savings Account")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount:.2f} from Savings Account")
        else:
            print("Insufficient funds. Cannot withdraw")

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f"Added {interest_amount:.2f} interest to Savings Account")


class BusinessAccount(Account):
    def __init__(self, account_number, balance, transaction_fee=1.5):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount:.2f} into Business Account")

    def withdraw(self, amount):
        if amount + self.transaction_fee <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount:.2f} from Business Account")
        else:
            print("Insufficient funds. Cannot withdraw")


if __name__ == "__main__":
    checking_account = CheckingAccount("C1001", 1000)
    savings_account = SavingsAccount("S2001", 1000)
    business_account = BusinessAccount("B3001", 1000)

    checking_account.deposit(1000)
    checking_account.withdraw(500)

    savings_account.deposit(2000)
    savings_account.add_interest()
    savings_account.withdraw(1000)

    business_account.deposit(1500)
    business_account.withdraw(700)

    checking_account.display_balance()
    savings_account.display_balance()
    business_account.display_balance()
