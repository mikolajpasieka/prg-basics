def f(n):
    x = ""
    for i in range(1, n+1):
        x = x + str(i)
    return x 

if __name__ == "__main__":
    print(f(4))
    print(f(11))