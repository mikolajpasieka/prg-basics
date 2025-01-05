def f(amount_to_pay):
    total = 0 
    if amount_to_pay >= 5:
       x =  (amount_to_pay // 5) 
       total += x 
       amount_to_pay -= total*5
    if amount_to_pay >= 2:
       y =  (amount_to_pay // 2) 
       total += y 
       amount_to_pay -= y*2
    if total >= 1 : 
       total += amount_to_pay 
    return total

if __name__ == "__main__":
   print(f(23))
   print(f(8))
   print(f(2))
   print(f(0))