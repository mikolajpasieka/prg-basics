current_price = 140
previous_price = 200
print(f"Current product price: {current_price}")
print(f"Previous product price: {previous_price}")
x = (previous_price-current_price)/previous_price
if x >= 0.1:
    print(f"Buy the product!!")
    print(f"Product price reduced by: {int(x*100)}%")