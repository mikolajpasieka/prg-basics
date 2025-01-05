def f(arr):
    arr1 = []
    for x in arr:
        if arr.count(x) == 1:
            arr1.append(x)
    return f'Unique elements: {arr1}'

arr = [2,3,2,5,8,1,9,8,]
print(f'Array: {arr}')
print(f(arr))