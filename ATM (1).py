import time

# Simulate inserting a card
print("Please insert your card")
time.sleep(2)  # Pause for 2 seconds to simulate card processing time

# Initialize ATM details
password = 1234  # The correct PIN for the ATM
balance = 5000  # Initial balance in the account
transaction_history = []  # To store the history of transactions

# Prompt user to enter the ATM PIN
try:
    pin = int(input("Enter your ATM Pin: "))
except ValueError:
    # Handle non-numeric input for PIN
    print("Invalid input. Please enter a numeric PIN.")
    exit()  # Exit the program if PIN is not numeric

# Check if the entered PIN is correct
if pin == password:
    while True:
        # Display the menu options to the user
        print("""
        1 == Balance 
        2 == Withdrawal Amount 
        3 == Deposit Balance 
        4 == Change Pin
        5 == Transaction History
        6 == Exit
        """)
        try:
            # Get the user's choice of operation
            option = int(input("Please enter your choice: "))
        except ValueError:
            # Handle non-numeric input for menu option
            print("Please enter a valid option")
            continue  # Continue to the next iteration of the loop

        # Check the balance
        if option == 1:
            print(f"Your current balance is {balance}")
            print("==================================")

        # Withdraw amount from the balance
        elif option == 2:
            try:
                withdraw_amount = int(input("Please enter withdrawal amount: "))
                if withdraw_amount > balance:
                    # Check if withdrawal amount exceeds current balance
                    print("Insufficient balance")
                else:
                    # Deduct the withdrawal amount from the balance
                    balance -= withdraw_amount
                    transaction_history.append(f"Withdrawal: {withdraw_amount}")
                    print(f"{withdraw_amount} is debited from your account")
                    print("==============================================")
                    print(f"Your updated balance is {balance}")
                    print("==================================")
            except ValueError:
                # Handle non-numeric input for withdrawal amount
                print("Please enter a valid amount")

        # Deposit amount into the balance
        elif option == 3:
            try:
                deposit_amount = int(input("Please enter deposit amount: "))
                balance += deposit_amount  # Add the deposit amount to the balance
                transaction_history.append(f"Deposit: {deposit_amount}")
                print(f"{deposit_amount} is credited to your account")
                print("============================================")
                print(f"Your updated balance is {balance}")
                print("==================================")
            except ValueError:
                # Handle non-numeric input for deposit amount
                print("Please enter a valid amount")

        # Change the PIN
        elif option == 4:
            try:
                new_pin = int(input("Enter your new PIN: "))
                confirm_new_pin = int(input("Confirm your new PIN: "))
                if new_pin == confirm_new_pin:
                    # Check if the new PINs match and update the PIN
                    password = new_pin
                    print("PIN successfully changed!")
                else:
                    # Handle mismatched PINs
                    print("PINs do not match. Try again.")
            except ValueError:
                # Handle non-numeric input for new PIN
                print("Please enter a valid numeric PIN")

        # Display transaction history
        elif option == 5:
            print("Transaction History:")
            if transaction_history:
                for transaction in transaction_history:
                    print(transaction)  # Print each transaction
            else:
                # If no transactions have occurred
                print("No transactions yet.")
            print("==================================")

        # Exit the program
        elif option == 6:
            print("Thank you for using the ATM. Goodbye!")
            break  # Exit the while loop, thus ending the program

        # Handle invalid menu options
        else:
            print("Please enter a valid option")

# If the entered PIN is incorrect
else:
    print("Wrong PIN. Please try again.")

