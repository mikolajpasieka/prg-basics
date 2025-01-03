def f(wyrażenie):
    list = wyrażenie.split()
    stack = []
    for i in list:
        if i.isnumeric() == True:
            stack.append(i)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if i == "*":
                stack.append(a*b)
            elif i == "+":
                stack.append(a+b)
            elif i == "-":
                stack.append(a-b)
            elif i == "/":
                stack.append(a/b)
            elif i == "%":
                stack.append(b%a)
    return stack.pop()

if __name__ == "__main__":
    print(f("5 4 *"))
    print(f("2 6 % 4 5 * *"))
    print(f("11 7 % 15 * 14 %"))