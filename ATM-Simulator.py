#ATM SIMULATOR

class User:
    def __init__(self, username, pin, initial_balance=0):
        self.username = username
        self.pin = pin
        self.balance = initial_balance
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
            return f"${amount:.2f} has been deposited."
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            return f"${amount:.2f} has been withdrawn."
        elif amount > self.balance:
            return "Insufficient funds."
        return "Withdrawal amount must be positive."

    def get_transaction_history(self):
        return self.transaction_history


class ATM:
    def __init__(self):
        self.users = {}

    def create_account(self, username, pin, initial_balance):
        if username in self.users:
            return "Account already exists."
        self.users[username] = User(username, pin, initial_balance)
        return f"Account created for {username} with initial balance: ${initial_balance:.2f}"

    def login(self, username):
        if username not in self.users:
            return "Account not found."
        
        user = self.users[username]
        attempts = 0
        
        while attempts < 3:
            pin = input("Enter your 4-digit PIN: ")
            if user.pin == pin:
                return user
            else:
                attempts += 1
                print(f"Incorrect PIN. {3 - attempts} attempt(s) left.")
        
        print("Too many incorrect PIN attempts.")
        return None

    def run(self):
        while True:
            print("\nWelcome to the ATM")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")

            choice = input("Please select an option (1-3): ")

            if choice == '1':
                username = input("Enter a username: ")
                pin = input("Set a 4-digit PIN: ")
                if len(pin) != 4 or not pin.isdigit():
                    print("PIN must be a 4-digit number.")
                    continue
                try:
                    initial_balance = float(input("Enter initial balance: "))
                    print(self.create_account(username, pin, initial_balance))
                except ValueError:
                    print("Please enter a valid amount.")

            elif choice == '2':
                username = input("Enter your username: ")
                user = self.login(username)

                if user:
                    while True:
                        print("\nATM Menu:")
                        print("1. Check Balance")
                        print("2. Deposit Money")
                        print("3. Withdraw Money")
                        print("4. Transaction History")
                        print("5. Logout")

                        option = input("Select an option (1-5): ")

                        if option == '1':
                            print(f"Your current balance is: ${user.check_balance():.2f}")

                        elif option == '2':
                            try:
                                amount = float(input("Enter amount to deposit: "))
                                print(user.deposit(amount))
                            except ValueError:
                                print("Please enter a valid amount.")

                        elif option == '3':
                            try:
                                amount = float(input("Enter amount to withdraw: "))
                                print(user.withdraw(amount))
                            except ValueError:
                                print("Please enter a valid amount.")

                        elif option == '4':
                            history = user.get_transaction_history()
                            print("Transaction History:")
                            for transaction in history:
                                print(transaction)

                        elif option == '5':
                            print("Logging out.")
                            break

                        else:
                            print("Invalid option. Please choose again.")
                else:
                    print("Returning to the main menu. Please choose another option.")

            elif choice == '3':
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid option. Please choose again.")


# Run the ATM simulation
if __name__ == "__main__":
    atm = ATM()
    atm.run()
