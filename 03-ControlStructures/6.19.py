print("SURVEY")
print("___________________________________________________")
x = input("Are you interested in computer science? (y/n):")
y = input("Do you like playing computer games? (y/n):")
z = input("Do you have an Instagram account? (y/n): ")

if x == "y":
    a = "Yes"
elif x == "n":
    a = "No"
else:
    a = "Invalid answer"

if y == "y":
    b = "Yes"
elif y == "n":
    b = "No"
else:
    b = "Invalid answer"

if z == "y":
    c = "Yes"
elif z == "n":
    c = "No"
else:
    c = "Invalid answer"

print("___________________________________________________")
print("SURVEY RESULTS")
print("___________________________________________________")
print(f"Interested in computer science: {a}")
print(f"Playing computer games: {b}")
print(f"Has an Instagram account: {c}")
