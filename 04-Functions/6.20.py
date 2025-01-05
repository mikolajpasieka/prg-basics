def f(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    count = 0  
    candidate = 2  
    
    while count < n:
        if is_prime(candidate):
            count += 1
        if count < n:
            candidate += 1
    
    return candidate

if __name__ == "__main__":
    print(f(1))
    print(f(5))