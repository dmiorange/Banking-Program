def show_balance(balance):
    print("*******************************")
    print(f"Your balance is ${balance:.2f}")
    print("*******************************")

def deposit():
    print("*******************************")
    try:
        amount = float(input("Enter the amount you want to deposit: "))
        if amount > 0:
            return amount
        else:
            print("*******************************")
            print("That is not a valid amount.")
            print("*******************************")
            return 0
    except ValueError:
        print("*******************************")
        print("Invalid input. Please enter a number.")
        print("*******************************")
        return 0

def withdraw(balance):
    print("*******************************")
    try:
        amount = float(input("Enter the amount you want to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
            return 0
        elif amount > 0:
            return amount
        else:
            print("That is not a valid amount.")
            return 0
    except ValueError:
        print("*******************************")
        print("Invalid input. Please enter a number.")
        print("*******************************")
        return 0

def main():
    balance = 0
    is_running = True

    while is_running:
        print("**********************")
        print("   Banking Program   ")
        print("**********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")
        print("**********************")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
            print("Thank you for choosing us!")
        else:
            print("**************************")
            print("That is not a valid Choice")
            print("**************************")

    print("**************************")
    print("Thank you for choosing us!")
    print("**************************")

if __name__ == "__main__":
    main()
