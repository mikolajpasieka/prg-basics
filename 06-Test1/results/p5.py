def f(a,b):
    s = 0 
    for x in range (a,b+1):
        if len(str(x)) == 2:
            s += x 
    return s 





if __name__ == "__main__":
    print(f(8,12))
    print(f(98,105))