arr = [15, 8, 31, 47, 2, 19]
arr_r = []
for i in range(0, len(arr)):
    if i == 0:
        arr_r.append(arr[-1])
    if i >0:
        arr_r.append(arr[-i-1])




print('existed array:',arr)
print('reverse array:', arr_r)