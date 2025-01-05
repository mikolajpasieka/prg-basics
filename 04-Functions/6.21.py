def f(number1,number2,number3):
    x = (number1, number2, number3)
    return max(x) - min(x)

if __name__ == "__main__":
    print(f(7,4,9))
    print(f(2,12,8))