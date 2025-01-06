names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

names_sorted = sorted(names)

print(names_sorted, lambda x,y: len(x)<len(y))