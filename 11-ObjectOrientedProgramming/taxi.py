class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * int(self.rate_per_km)
        return self.fare

    def print_receipt(self): 
        return f'Rate per km: {self.rate_per_km}\nDistance {self.distance}\nFare {self.calculate_fare(self.distance)}'




def main():
    # your program
    ride1 = TaxiRide(2)
    ride2 = TaxiRide(1.5)
    ride1.distance = 10
    ride2.distance = 6
    print(ride1.print_receipt())
    print(ride2.print_receipt())
    

if __name__ == "__main__":
    main()
