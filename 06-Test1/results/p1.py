def f(x,y):
    z = x % y 
    b = "" 
    if z >=1 and z<= 9:
         r = z 
    elif z == 10:
         r = "a"
    elif z == 11:
         r = "b"
    elif z == 12:
         r = "c"
    elif z == 13:
         r = "d"
    elif z == 14:
         r = "e"
    elif z == 15:
         r = "f"
    elif z > 15:
         a = z - 16 
         if a >=1 and a<= 9:
           b = a
         elif a== 10:
           b = "a"
         elif a == 11:
           b = "b"
         elif a == 12:
            b = "c"
         elif a == 13:
            b = "d"
         elif a == 14:
           b = "e"
         elif a == 15:
           b = "f"

    if z <= 15:
        return (f"0x{r}")
    elif z >15:
        return (f"0x1{b}")



if __name__ == "__main__":
     print(f(118,20))
     print(f(210,100))