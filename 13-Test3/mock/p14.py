def f(d):
   parking = []

   for key, value in d:
       if value == "in":
           parking.append(key)
       if value == "out":
           parking.remove(key)
           parking.sort()
   return parking
           





if __name__ == "__main__":
    cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
    print(f(cars))
    cars1 = [["KR234","in"],["KR234","out"]]
    print(f(cars1)) 
