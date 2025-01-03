cart = {'juice':3, 'bread':1, 'milk':2}
prices = {'milk':1.49, 'butter': 2.09, 'juice':1.19, 'bread': 1.99}
def f(shopping_cart, price_list, customer_wallet):
    total = 0 
    for key in shopping_cart:
        b = shopping_cart[key]
        for y in price_list:
           if y == key:
              total += b*price_list[y]
    if total <= customer_wallet:
        x = True
    elif total > customer_wallet:
        x = False
    return x 


if __name__ == "__main__":
       print(f(cart, prices, 10))
       print(f(cart, prices, 8)) 