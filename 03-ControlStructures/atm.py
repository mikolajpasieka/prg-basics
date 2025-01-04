###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        entered_pin = input("Enter PIN code: ")
        if entered_pin == pin:
            print("PIN code is correct.")
        else: 
            print("PIN code is incorrect.")
    elif choice == '5':
        new_pin = input("Enter a new 4-digit PIN code: ")
        while new_pin.isdigit():
               if len(new_pin) == 4:
                  pin = new_pin
                  print("PIN code has been changed.")
                  break
               elif new_pin.isdigit() and len(new_pin) > 4:
                print("PIN is too long")
                print("TRY AGAIN!")
                new_pin = input("Enter new PIN code: ")
               elif new_pin.isdigit() and len(new_pin) < 4:
                print("PIN is too short")
                print("TRY AGAIN!")
                new_pin = input("Enter new PIN code: ")
        while not new_pin.isdigit():
            print("PIN code must be a 4-digit number.")
            print("TRY AGAIN!")
            new_pin = input("Enter a new 4-digit PIN code: ")
            while new_pin.isdigit():
               if len(new_pin) == 4:
                  pin = new_pin
                  print("PIN code has been changed.")
                  break
               elif new_pin.isdigit() and len(new_pin) > 4:
                print("PIN is too long")
                print("TRY AGAIN!")
                new_pin = input("Enter new PIN code: ")
               elif new_pin.isdigit() and len(new_pin) < 4:
                print("PIN is too short")
                print("TRY AGAIN!")
                new_pin = input("Enter new PIN code: ")
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")
