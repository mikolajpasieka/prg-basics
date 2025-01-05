def f(name):
    x = name[0]
    for i in range(0, len(name)):
        if name[i] == " ":
            x = x + name[i + 1]
    return x 

if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))