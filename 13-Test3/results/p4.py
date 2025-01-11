class C:
    def __init__(self,imię,nazwisko,wiek):
        self.name = imię 
        self.surname = nazwisko
        self.age = wiek 

    def __str__(self):
        if self.age >= 18:
          return f"{self.name[0]}{self.surname[0]}{self.age}"
        if self.age < 18:
            return f"{self.name[0].lower()}{self.surname[0].lower()}{self.age}"
        
    
if __name__ == "__main__":
    print(C('John','May',21))
    print(C('Anna','Brown',17))