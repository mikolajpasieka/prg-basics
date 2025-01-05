arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

min_value = 0
max_value = 0
min_position = (-1, -1)
max_position = (-1, -1)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < min_value:
            min_value = arr[i][j]
            min_position = (i, j)
        if arr[i][j] > max_value:
            max_value = arr[i][j]
            max_position = (i, j)

print(f'Min value: {min_value}, location: {min_position}')
print(f'Max value: {max_value}, location: {max_position}')
