def f(word):
    a = len(word)
    while a > 0:
        x = word[a-1]
        return x 

if __name__ == "__main__":
    print(f("book"))
    print(f("water")) 
    print(f("ok")) 
    print(f("a")) 
    print(f("")) 