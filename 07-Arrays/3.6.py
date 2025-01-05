arr = [15, 8, 31, 47, 2, 19]

def f(arr):
    count = 0 
    x = 0 
    while x < len(arr):
        count += arr[x]
        x += 1 
    mean = round(count/len(arr),2)
    return f'aritmetic mean of array: {arr} is {mean}'

print(f(arr))