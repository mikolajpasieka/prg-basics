def f(number, even):
    total = 0 
    if even == True:
        for digit in str(number):
            if int(digit) %2 == 0:
                total += int(digit) 
            else: 
                continue 
    if even == False:
        for digit in str(number):
            if int(digit) %2 != 0:
                total += int(digit)
            else: 
                continue 
    return total 
if __name__ == "__main__":
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))
