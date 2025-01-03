def f(arr):
    arr.sort()
    p = int(len(arr))
    for i in range(1, p -1):
        if arr[0] != arr[1]:
            x = arr[0]
        if arr[i] != arr[i - 1]:
            x = arr[i-1]
        if arr[i-2] != arr[i-2]:
            x = arr[i-2]
    return x 

if __name__ == "__main__":
       print(f([25,25,23]))
       print(f([7,7,7,7,7,5,7,7]))
      