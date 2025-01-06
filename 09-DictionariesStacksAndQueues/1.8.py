price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
print("===============================================")
print('PRICES BEFORE DISCOUNT')
print("===============================================")
for x,y in price_list.items():
    print(x,y)

for w in price_list.keys():
    price_list[w] = round(price_list[w]*0.9,2)
    

print("===============================================")
print('PRICES AFTER DISCOUNT')
print("===============================================")
for c,b in price_list.items():
    print(c,b)

total = 0 
for z in price_list.values():
   total += z

print("===============================================")
print('Total value of the products after the discount:', round(total,2))
print("===============================================")
