class C:
    def __init__(self,stadion):
        self.stadion = stadion

    def m1(self,s,m):
        for key in self.stadion.keys():
           key = s
           self.stadion[key] = m 

    def m2(self,s):
        count = 0
        for key in self.stadion.keys():
            if key in s:
                count += self.stadion[key]
        return count
    
if __name__ == "__main__":
    stadium = C({'A':120,'D':150,'G':90, 'K':110})
    stadium.m1("G",130)
    print(stadium.m2("GD"))
    print(stadium.m2("KEJ"))
    
   
