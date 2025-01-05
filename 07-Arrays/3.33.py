arr = [[1,0,0,0,6],[2,0,0,0,6],[3,0,0,0,6]] 

for row in arr:
    a = row[0] 
    b = row[-1]
    row[0] = b
    row[-1] = a
 
for row in arr:
    for value in row:
        print(value, end=" ")
    print()