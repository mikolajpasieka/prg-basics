num = int(input("Number of products purchased:"))
price = float(input("Product price:"))
if num == 1 or num == 2:
    total = num*price
elif num >2:
    total = price*2
    i = num - 2 
    while i >0:
        total += price*0.75
        i -= 1 
print(f"Amount to pay: {total}")
