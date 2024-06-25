from collections import namedtuple

accounts = []  # Define accounts globally

Account = namedtuple("Account", ["account_holder", "account_number", "balance"])

def select_account(accounts):
    if not accounts:
        print("No accounts found.")
        return None
    for index, account in enumerate(accounts, start=1):
        print(f"{index}. {account.account_holder} - {account.account_number}")
    while True:
        choice = input("Enter the account number to select (or 'q' to quit): ")
        if choice.lower() == 'q':
            return None
        try:
            index = int(choice) - 1
            if 0 <= index < len(accounts):
                return accounts[index]
            else:
                print("Invalid account number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")

def main():
    accounts = load_accounts()  # Attempt to load accounts (optional)
    while True:
        print("Bank Account Menu")
        print("1. Create Account")
        print("2. Select Account")
        print("3. Exit")
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            account_holder = input("Enter account holder name: ")
            account_number = input("Enter unique account number: ")
            initial_balance = float(input("Enter initial balance (optional, default 0.00): ") or 0.0)
            new_account = Account(account_holder, account_number, initial_balance)
            accounts.append(new_account)
            print(f"Account created successfully for {account_holder}!")

        elif user_choice == '2':
            selected_account = select_account(accounts)
            if selected_account:
                deposit_amount = float(input("Enter amount to deposit: "))
                updated_account = deposit(selected_account, deposit_amount)
                accounts.remove(selected_account)  # Remove old account
                accounts.append(updated_account)  # Add updated account
       
        elif user_choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()