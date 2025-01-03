def f(x,y,digit):
    z = 0
    for i in range(x, y+1):
      z += str(i).count(str(digit))
    return z

if __name__ == "__main__":
    print(f(10,15,1))
    print(f(28,32,2)) 
    print(f(100,105,6)) 
    print(f(100,101,0))  