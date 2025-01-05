def f(arr):
    arr_power_two = []
    for digit in arr:
        x = digit ** 2 
        arr_power_two.append(x)
    return arr_power_two

if __name__ == "__main__":
    print(f([8,2,5,1,9]))