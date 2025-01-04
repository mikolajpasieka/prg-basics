amount = int(input("Enter the amount in PLN:"))
x = 0
y = 0 
z = 0
while amount > 5:
    amount -= 5
    x += 1
else:
    while amount > 2:
       amount -= 2
       y += 1
    else: 
       while amount >= 1:
          amount -= 1
          z += 1

print(f"The amount of PLN {amount} in coins:")
print(f"5 PLN coins: {x}")
print(f"2 PLN coins: {y}")
print(f"1 PLN coins: {z}")