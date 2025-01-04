###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    total = 0 
    if number < 0:
        number = abs(number)
    num_to_str = str(number)
    for char in num_to_str:
        total += int(char)
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')