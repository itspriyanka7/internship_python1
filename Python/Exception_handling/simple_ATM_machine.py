class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def check_balance(self):
        print(f"Your balance is ₹{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")

def atm_menu():
    atm = ATM()
    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                atm.check_balance()
            elif choice == 2:
                amount = float(input("Enter deposit amount: "))
                atm.deposit(amount)
            elif choice == 3:
                amount = float(input("Enter withdrawal amount: "))
                atm.withdraw(amount)
            elif choice == 4:
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid option.")
        except ValueError as e:
            print("Error:", e)

atm_menu()
