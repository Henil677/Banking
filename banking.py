import random

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append((amount, "Deposit"))
        print(f"Deposited {amount} into account {self.account_number}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance - 5000:
            print(f"Withdrawal amount of {amount} cannot be processed for account {self.account_number}.")
            print(f"The minimum balance required is 5000. Current balance is {self.balance}.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance is {self.balance}.")

    def delete(self):
        print(f"Deleted account {self.account_number}.")
        del self


class Bank:
    def __init__(self):
        self.accounts = []

    def generate_account_number(self):
        while True:
            account_number = str(random.randint(10**15, 10**16 - 1))
            if not self.get_account(account_number):
                return account_number

    def create_account(self, balance=5000):
        account_number = self.generate_account_number()
        account = BankAccount(account_number, balance)
        self.accounts.append(account)
        print(f"Created account {account_number} with balance {balance}.")

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                account.delete()
                self.accounts.remove(account)
                return
        print(f"Account {account_number} not found.")

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print(f"Account {account_number} not found.")

    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print(f"Account {account_number} not found.")

    def view_balance(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(f"Account {account_number} balance is {account.balance}")
        else:
            print(f"Account {account_number} not found.")

    def print_transactions(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(f"Transaction history for account {account_number}:")
            for transaction in account.transactions:
                print(f"{transaction[1]} of {transaction[0]}")
        else:
            print(f"Account {account_number} not found.")



def main():
    bank = Bank()

    while True:
        print("\nWelcome to the bank!")
        print("What would you like to do?")
        print("1. Create an account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. View account balance")
        print("5. View Transactions")
        print("6. Delete an account")
        print("7. Exit")

        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            balance = float(input("Enter initial balance (default is 5000): ") or "5000")
            bank.create_account(balance)

        elif choice == 2:
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_number, amount)

        elif choice == 3:
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(account_number, amount)

        elif choice == 4:
            account_number = input("Enter account number: ")
            bank.view_balance(account_number)

        elif choice == 5:
           account_number = input("Enter account number: ")
           bank.print_transactions(account_number) 
        
        elif choice == 6:
            account_number = input("Enter account number to delete: ")
            bank.delete_account(account_number)
            
        elif choice == 7:
            print("Thank you for banking")
            break
        
        else:
            print("Invalid choice. Please try again.")



if __name__=="__main__":
    main()