class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []  # To track transaction history

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            print(f"Withdrew {amount}. Current balance: {self.balance}")
        else:
            print("Insufficient funds for this withdrawal!")

    def get_balance(self):
        return self.balance

    def __str__(self):
        """
        Returns a string representation of the bank account.
        """
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: {self.balance}"

    def transfer(self, amount, recipient_account, description="Bank Transfer"):

        if amount <= 0:
            print("Transfer amount must be positive!")
            return
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(f"Transferred {amount} to {recipient_account.account_holder}. Description: {description}")
            print(f"Transferred {amount} to {recipient_account.account_holder}. Description: {description}")
        else:
            print("Insufficient funds for this transfer!")

    def multi_deposit(self, *amounts, **details):
        """
        Deposits multiple amounts into the account.
        Parameters:
        *amounts (float): The amounts to deposit.
        **details (dict): Additional information like 'note'.
        """
        for amount in amounts:
            if amount <= 0:
                print(f"Skipping deposit of {amount}, as it is not positive!")
                continue
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}")
            print(f"Deposited {amount}. New balance: {self.balance}")
        
        # if provided
        if "note" in details:
            print(f"Note: {details['note']}")

    def get_transaction_history(self):
        return self.transaction_history





def menu(account):
    """
    Displays a menu for interacting with the bank account.
    Uses break, continue, and pass for control flow.
    """
    while True:
        print("\nBank Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer Money")
        print("5. Get Transaction History")
        print("6. Exit")

        choice = input("Please enter your choice (1/2/3/4/5/6/7): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Your balance is: {account.get_balance()}")
        elif choice == "4":
            recipient_account_number = input("Enter recipient account number: ")
            recipient_account_holder = input("Enter recipient account holder: ")
            recipient_account = BankAccount(recipient_account_number, recipient_account_holder)
            amount = float(input("Enter amount to transfer: "))
            account.transfer(amount, recipient_account)
        elif choice == "5":
            history = account.get_transaction_history()
            print("Transaction History:")
            for transaction in history:
                print(transaction)
        elif choice == "6":
            print("Exiting the system.")
            break  # Exit the loop
        else:
            print("Invalid option! Try again.")
            continue  # Skip this iteration and ask for input again


if __name__ == "__main__":
    # Create an instance of BankAccount
    account1 = BankAccount("12345", "Alice", 1000)
    menu(account1)
