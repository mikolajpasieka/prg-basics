def f(number):
    total = 0 
    for i in range(0,10):
        a = str(number).count(str(i))
        if  a > 1:
            total += a*i
    return total  


if __name__ == "__main__":
    print(f(1027)) 
    print(f(230335) ) 
    print(f(513553007)) 







 