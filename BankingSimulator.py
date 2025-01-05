class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. Current balance: ${self.balance}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be greater than zero.")

    def get_balance(self):
        return self.balance


def show_menu():
    print("\nWelcome to the Bank System!")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")


def main():
    name = input("Enter your name: ")
    account = BankAccount(owner=name)
    
    while True:
        show_menu()
        choice = input("Choose an action (1-4): ")

        if choice == '1':
            try:
                amount = float(input("Enter amount to deposit: $"))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: $"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == '3':
            print(f"Your current balance is: ${account.get_balance()}")
        
        elif choice == '4':
            print("Thank you for using the Bank System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

# Possible test output answers:
# Enter your name: Biff

# Welcome to the Bank System!
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Choose an action (1-4): 2
# Enter amount to withdraw: $100
# Insufficient funds for this withdrawal.

# Welcome to the Bank System!
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Choose an action (1-4): 3
# Your current balance is: $0

# Welcome to the Bank System!
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Choose an action (1-4): 4
# Thank you for using the Bank System. Goodbye
