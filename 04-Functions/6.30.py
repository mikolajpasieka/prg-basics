def sum_natural(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i 
    return sum 
    
if __name__ == "__main__":
    print(sum_natural(10))