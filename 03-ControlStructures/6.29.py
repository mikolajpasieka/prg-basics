def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n+1):
        if n % i == 0:
            return False 
        else:
            return True 
        
def f(N): 
    x = ""
    num = 1
    while N > 0:
        if is_prime(num):
            x = x + str(num) + " "
            N -= 1
        num += 1 
    return x 


if __name__ == "__main__":
    print(f(10))