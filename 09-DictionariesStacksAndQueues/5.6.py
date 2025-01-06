basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}


person = {}


for key,value in basic_data.items():
    person[key] = value

for key1,value1 in advanced_data.items():
    person[key1] = value1

print(person)