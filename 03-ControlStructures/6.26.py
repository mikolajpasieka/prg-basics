pin = "0805"
i = 2
pin1 = input("Enter the PIN code:")
while i > 0:
    if pin1 == pin:
        print("pin ok")
        break 
    else: 
        print("Incorrect...")
        pin1 = input("Enter the PIN code:")
    i -= 1 
if i == 0:
    print("Incorrect...")
    print("Sorry, your payment card has been blocked.")
