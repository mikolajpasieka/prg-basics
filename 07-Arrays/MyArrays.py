def second_largest(arr):
    arr.sort()
    return arr[-2]


def max_min(arr):
    return max(arr)-min(arr)

def median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        x = int(len(arr)/2)
    else:
        x = int((len(arr)-1)/2)
    return arr[x]

def smallest_largest(arr):
    arr1 = []
    arr1.append(min(arr))
    arr1.append(max(arr))
    return arr1 

def numbers_to_string(arr):
    x = str(arr[0])
    for i in range(1,len(arr)):
        x = x + "-" + str(arr[i])
    return x 