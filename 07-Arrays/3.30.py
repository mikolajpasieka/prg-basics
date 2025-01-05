arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
arr[0][0] = 1 

# Fill the array with multiplication table values
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = (i + 1) * (j + 1)

# Print the array
for row in arr:
    for value in row:
        print(value, end=" ")
    print()