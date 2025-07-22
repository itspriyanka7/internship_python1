from abc import ABC, abstractmethod
import os
import json


# ---------------- Abstract Class ----------------
class Account(ABC):
    def __init__(self, account_number, name, balance):
        self.__account_number = account_number
        self.__name = name
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass


# ---------------- SavingsAccount Class ----------------
class SavingsAccount(Account):
    MIN_BALANCE = 1000

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance - self.MIN_BALANCE:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance


# ---------------- Bank Class ----------------
class Bank:
    def __init__(self):
        self.accounts = {}  # key = account_number, value = SavingsAccount
        self.filename = "accounts.txt"
        self.load_accounts()

    def load_accounts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                for acc in data:
                    account = SavingsAccount(acc["account_number"], acc["name"], acc["balance"])
                    self.accounts[account.account_number] = account

    def save_accounts(self):
        with open(self.filename, "w") as f:
            data = [{"account_number": acc.account_number, "name": acc.name, "balance": acc.balance}
                    for acc in self.accounts.values()]
            json.dump(data, f)

    def generate_account_number(self):
        return 1001 + len(self.accounts)

    def create_account(self, name, opening_balance):
        if opening_balance >= SavingsAccount.MIN_BALANCE:
            acc_num = self.generate_account_number()
            new_acc = SavingsAccount(acc_num, name, opening_balance)
            self.accounts[acc_num] = new_acc
            self.save_accounts()
            return acc_num
        else:
            raise ValueError(f"Opening balance must be at least {SavingsAccount.MIN_BALANCE}")

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer_money(self, from_acc_num, to_acc_num, amount):
        from_acc = self.find_account(from_acc_num)
        to_acc = self.find_account(to_acc_num)
        if from_acc and to_acc and from_acc.withdraw(amount):
            to_acc.deposit(amount)
            self.save_accounts()
            return True
        return False


# ---------------- Main Program ----------------
def main():
    bank = Bank()
    while True:
        print("\n--- Welcome to Python Bank ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                name = input("Enter name: ")
                balance = float(input("Enter opening balance: "))
                acc_num = bank.create_account(name, balance)
                print(f"Account created successfully! Account No: {acc_num}")

            elif choice == '2':
                acc_num = int(input("Enter account number: "))
                acc = bank.find_account(acc_num)
                if acc:
                    amt = float(input("Enter amount to deposit: "))
                    if acc.deposit(amt):
                        bank.save_accounts()
                        print("Deposit successful!")
                    else:
                        print("Invalid amount.")
                else:
                    print("Account not found.")

            elif choice == '3':
                acc_num = int(input("Enter account number: "))
                acc = bank.find_account(acc_num)
                if acc:
                    amt = float(input("Enter amount to withdraw: "))
                    if acc.withdraw(amt):
                        bank.save_accounts()
                        print("Withdrawal successful!")
                    else:
                        print("Insufficient balance or invalid amount.")
                else:
                    print("Account not found.")

            elif choice == '4':
                acc_num = int(input("Enter account number: "))
                acc = bank.find_account(acc_num)
                if acc:
                    print(f"Current balance: ₹{acc.get_balance():.2f}")
                else:
                    print("Account not found.")

            elif choice == '5':
                from_acc = int(input("From account number: "))
                to_acc = int(input("To account number: "))
                amt = float(input("Amount to transfer: "))
                if bank.transfer_money(from_acc, to_acc, amt):
                    print("Transfer successful!")
                else:
                    print("Transfer failed. Check account numbers or balance.")

            elif choice == '6':
                print("Thank you for using Python Bank!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError as ve:
            print("Error:", ve)
        except Exception as e:
            print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()
