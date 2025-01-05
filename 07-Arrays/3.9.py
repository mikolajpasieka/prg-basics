def compare(array1, array2):
    if array1 == array2:
         return True
    else:
         return False
    

array1 = ["water","book","sky"]  
array2 = ["water","book","sky"]
print('Array1:', array1)
print('Array2:', array2)

if compare(array1,array2) == True:
     print('Comparison: arrays are the same')
else:
     print('Comparison: arrays are not the same')