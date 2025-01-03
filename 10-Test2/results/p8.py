def f(c):
    if not "2" in c:
        x = 2 
    elif not "3" in c:
        x = 3
    elif not "4" in c: 
        x = 4 
    elif not "5" in c:
        x = 5 
    elif not "6" in c:
        x = 6
    elif not "7" in c:
        x = 7
    elif not "8" in c:
        x = 8
    elif not "9" in c:
        x = 9
    elif not "T" in c:
        x = "T"
    elif not "J" in c:
        x = "J"
    elif not "Q" in c:
        x = "Q"
    elif not "K" in c:
        x = "K"
    elif not "A" in c:
        x = "A"
    return x 
    

if __name__ == "__main__":
       print(f("2345678TQKJA"))
       print(f("2K345AQJ967T"))
      