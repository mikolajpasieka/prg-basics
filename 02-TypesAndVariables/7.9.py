import random 
roll = random.randint(1,6)
x = roll == 1 or roll == 6
print(f"Dice rolled: {roll}")
print(f"Special number (1 or 6): {x}")