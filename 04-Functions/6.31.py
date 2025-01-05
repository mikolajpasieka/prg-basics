def power(x,n):
    if x  == 0:
        return 0 
    if n == 0:
        return 1 
    if n == 1:
        return x 
    if n > 1:
        if (n-1) == 0:
            return x
        if (n-1) == 1:
            return x*x
        else:
            return x**n

if __name__ == "__main__":
    print(power(5,3))
    print(power(135784847,0))
    print(power(6,2))