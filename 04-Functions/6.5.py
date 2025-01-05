import range
num = int(input("Enter number:"))
range1 = int(input("Enter firts digit of range"))
range2 = int(input("Enter second digit of range"))
print(f"A number: {num}")
print(f"Number {num} in the range <{range1},{range2}>: {range.f(num,range1,range2)}")