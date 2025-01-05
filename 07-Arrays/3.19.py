def f(arr,n):
    count = 0 
    for i in arr:
        if i > n:
            count +=1
    return count

print(f([7,5,6,7889,554,775,325,677,3,56,7,3,67,3,67,5,3,4,4,67,5,8,3,35,6], 4))