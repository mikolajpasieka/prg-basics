def f(arr1, arr2):
    for i in arr1:
        if not i in arr2:
            return False
    return True
        
        
print(f([1,7,9,2,4,5,6], [2,2,5,7,8,9]))
print(f([1,4,5], [1,5,4,5,6,3]))