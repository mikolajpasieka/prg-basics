def f(password):
    if len(password) >= 6:
        list = []
        for i in range(0, len(password)):
            list.append(password[i])
        set1 = set(password)
        if len(list) == len(set1):
            return True 
        else: 
            return False
    else:
        return False

if __name__ == "__main__":
    print(f("ax15"))
    print(f("book123"))
    print(f("A2water3"))
    print(f("qwerty"))
    print(f(""))


    