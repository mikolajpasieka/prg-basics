arr = [34,7,19,4,21,8]
i = 0 
count = 0
while i <= len(arr)-1:
    if arr[i] % 2 == 0:
        count += 1 
    i += 1 

print(count)