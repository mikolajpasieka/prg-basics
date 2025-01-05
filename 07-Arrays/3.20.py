arr = [7,9,2,4,5,6]
def f(arr):
    even = []
    odd = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        if i % 2 != 0:
            odd.append(i)
    even.sort()
    odd.sort()
    return even + odd 

print(f(arr))