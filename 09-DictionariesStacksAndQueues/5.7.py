hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    y = ""
    for x in hotels:
         y = y + x['name'] + ','
    return y
    
def avg_price(hotels):
    y = 0 
    count = 0 
    for x in hotels:
        y += x['price'] 
        count +=1 
    z = y/count
    return int(round(z))


print("Hotels in Krakow:", hotel_list(hotels_in_Krakow))
print("Average hotel price in Krakow:", avg_price(hotels_in_Krakow))
print("Hotels in Sopot:", hotel_list(hotels_in_Sopot))
print("Average hotel price in Sopot:", avg_price(hotels_in_Sopot) )