def f(n):
    if n == 1:
        return "*"
    else:
        return "*/"*(n -1) + "*"


if __name__ == "__main__":
    print(f(4))
    print(f(1))