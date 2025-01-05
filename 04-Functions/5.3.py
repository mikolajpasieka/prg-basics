##
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard # your own defined module

# Reads employee's data from keyboard
first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter name: ')
age = keyboard.input_integer('Enter age:')
salary = keyboard.input_real('Enter salary')
is_salary_hidden = keyboard.input_string('Hide salary? (y/n)')
if is_salary_hidden == "y":
    is_salary_hidden == True
if is_salary_hidden == "n":
    is_salary_hidden == False

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Surname', last_name)
print('Age', age)
if is_salary_hidden == False:
    print('Salary', salary)