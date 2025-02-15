from decimal import Decimal, InvalidOperation

class User:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.transactions = []

    def check_balance(self):
        return f'{self.balance:.2f}' 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"+ ${amount:.2f}")
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if self.balance > amount:
                self.balance -= amount
                self.transactions.append(f"- ${amount:.2f}")
                return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
            else:
                return "Insufficient funds."
            
        else:
            return "Amount must be positive."
    
    def history(self):
        return "\n".join(self.transactions) if self.transactions else "No transactions found."
    
    def __str__(self):
        return f'User: {self.name}, balance: ${self.balance:.2f}'
    
class ATM:
    def __init__(self):
        self.users = {}

    def create_user(self, name, initial_balance):
        if not name in self.users:
            self.users[name] = User(name, initial_balance)
            return f"User {name} with initial balance ${initial_balance} created successfully!"
        else:
            return f"User {name} is already created."
        
    def get_user(self, name):
        return self.users.get(name, None)
    
    def __str__(self):
        return "\n".join([str(user) for user in self.users.values()])
    
atm = ATM()
print("Select operation:\n 1 - Create user\n 2 - Check balance\n 3 - Deposit money\n 4 - Withdraw money\n 5 - Transaction history\n 0 - Exit\n(Type number only)")

while True:
    try:
        choice = int(input("\nSelect operation: "))
    except ValueError:
        print("Enter a number value!")

    if choice == 1:
        name = str(input("Enter username: "))
        try:
            initial_balance = Decimal(input("Enter initial balance: $"))
            print(atm.create_user(name, initial_balance))
        except InvalidOperation:
            print("Error: Enter a number.")

    elif choice == 2:
        name = str(input("Enter username: "))
        user = atm.get_user(name)
        if user:
            print(f"Current balance: ${User.check_balance(user)}")
        else:
            print("No user found.")

    elif choice == 3:
        name = str(input("Enter username: "))
        user = atm.get_user(name)
        if user:
            try:
                amount = Decimal(input("Enter amount: $"))
                print(user.deposit(amount))
            except InvalidOperation:
                print("Error: Enter a number.")
        else:
            print("No user found.")

    elif choice == 4:
        name = str(input("Enter username: "))
        user = atm.get_user(name)
        if user:
            try:
                amount = Decimal(input("Enter amount: $"))
                print(user.withdraw(amount))
            except InvalidOperation:
                print("Error: Enter a number.")
        else:
            print("No user found.")

    elif choice == 5:
        name = str(input("Enter username: "))
        user = atm.get_user(name)
        if user:
            print(user.history())
        else:
            print("No user found.")

    elif choice == 0:
        print(f"ATM closed with:\n{atm}")
        break

    else:
        print("Error: no operation found. Try to enter a number from 0-5.")
