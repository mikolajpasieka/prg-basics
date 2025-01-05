def occurs(number, array):
    if number in array:
        return True
    else:
        return False
    
number = int(input("enter number:"))
array = [15,38,7,23,14]
print(f'Number: {number}')
print("Array: 15 38 7 23 14")
if occurs(number, array):
    print(f'Result: number {number} appears in the array')
else:
    print(f'Result: number {number} does not appear in the array')