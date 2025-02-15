from decimal import Decimal

class ATM:
    def __init__(self, balance):
        self.balance = balance
    
    def check_balance(self):
        return self.balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."
        
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdrew ${amount}. New balance: ${self.balance}"
            else:
                return "Insufficient funds."
        else:
            return "Withdraw amount must be positive."
            
        
    def __str__(self):
        return f"${self.balance}"
    
atm = ATM(0)

print("Select operation:\n 1 - Check balance\n 2 - Deposit money\n 3 - Withdraw money\n 4 - Exit\n(Type number only)")

while True:
    try:
        choice = int(input("\nSelect operation: "))
    except ValueError:
        print("Error: enter a number value.")
        continue

    if choice == 1:
        print(f"Current balance: {atm}")
    elif choice == 2:
        try:
            amount = Decimal(input("Enter deposit amount: $"))
            print(atm.deposit(amount))
        except ValueError:
            print("Error: enter a number value.")
    elif choice == 3:
        try:
            amount = Decimal(input("Enter withdraw amount: $"))
            print(atm.withdraw(amount))
        except ValueError:
            print("Error: enter a number value.")
    elif choice == 4:
        print(f"ATM closed with balance {atm}")
        break
    else:
        print("Error: no operation found. Try to enter a number from 1-4.")