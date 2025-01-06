provinces = {
"D":"Dolnośląskie",
"C":"Kujawsko-pomorskie",
"L":"Lubelskie",
"F":"Lubuskie",
"E":"Łódzkie",
"K":"Małopolskie",
"W":"Mazowieckie",
"O":"Opolskie",
"R":"Podkarpackie",
"B":"Podlaskie",
"G":"Pomorskie",
"S":"Śląskie",
"T":"Świętokrzyskie",
"N":"Warmińsko-mazurskie",
"P":"Wielkopolskie",
"Z":"Zachodniopomorskie"
}

vehicles_form_province = {}

with open("vehicle.txt") as file:
    vehicle_not_splitted = file.read()
    vehicle = vehicle_not_splitted.split()
file.close()

for x in vehicle:
    for key in provinces.keys():
       if x[0] == key:
           x = 0 