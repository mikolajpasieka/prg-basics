person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print("Name:",person["name"])
print("Hobbys:", end = " ")
for x in person["hobby"]:
    print(x, end=" ")
print()

person["surname"] = "Nowak"

person["married"] = False

person["gender"] = 'male'

person['hobby'] 


print(person)