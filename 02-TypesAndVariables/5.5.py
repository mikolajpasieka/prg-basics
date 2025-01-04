amount = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
print(f"Price with discount: {round(amount * (1 - discount / 100),2)}")
print(f"Reduction: {round(amount * discount/100, 2)}")