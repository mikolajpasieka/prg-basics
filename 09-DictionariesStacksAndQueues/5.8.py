# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
cost = 0 
for x in cart.keys():
    if x in prices.keys():
        cost += cart[x]*prices[x]

print(cost)