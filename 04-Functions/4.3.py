###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
def triangle_area(a,b,c):
    p = (a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c))**0,5
    return area

print(f'The area of ​​a triangle with sides 3, 4, 5 is {triangle_area(3, 4, 5)}')
print(f'The area of ​​a triangle with sides 5, 12, 13 is {triangle_area(5, 12, 13)}')
print(f'The area of ​a triangle with sides 7, 24, 25 is {triangle_area(7, 24, 25)}')