arr = [[1,0,0,0,0],[2,0,0,0,0],[3,0,0,0,0]] 
for row in arr:
    for value in row:
        print(value, end=" ")
    print()

row1 = arr[-1]
row2 = arr[1]
row3 = arr[0]

arr1 = []

arr1.append(row1)
arr1.append(row2)
arr1.append(row3)

print("    ")

for row in arr1:
    for value in row:
        print(value, end=" ")
    print()