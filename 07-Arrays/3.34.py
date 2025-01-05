def identity_matrix(n):
    arr = [[0 for x in range(n)] for z in range(n)]
    j = 0 
    i = 0
    while i < len(arr):
        while j < len(arr[0]):
            arr[i][j] = 1
            j += 1 
            i += 1 
    return arr

def print_matrix(arr):
       for row in arr:
        print(' '.join(map(str, row)))

print(print_matrix(identity_matrix(5)))