def create_2d_arr(x,y):
    arr = [0 for i in range(y)]
    arr1 = [arr]*x
    return arr1 

arr = create_2d_arr(3,5)
for row in arr:
    for i in row:
        print(row[i], end= " ")
    print()