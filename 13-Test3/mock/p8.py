def f(n):
    odd_digits = [int(digit) for digit in str(n) if int(digit) % 2 == 1]
    if not odd_digits:
        return -1
    return max(odd_digits) - min(odd_digits)

if __name__ == "__main__":
    print(f(10852))
    print(f(7235973)) 
    print(f(4388)) 
    print(f(846206))  




