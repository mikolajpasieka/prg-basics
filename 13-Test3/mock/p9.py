def f(x,y,d):
    num = [str(i) for  i in range(x,y+1)]
    for a in num:
        if d in str(a):
           return True  
    return False

#2sposob:
# for num in range(x, y + 1):
#      if d in str(num):  
#           return True
# return False

if __name__ == "__main__":
    print(f(10,15,"14") )
    print(f(100,120,"11")) 
    print(f(205,210,"04")) 