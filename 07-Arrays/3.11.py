def bubble_sort(arr):
   n = len(arr)
   for i in range (0, n-1):
      for j in range(0, n-i-2):
         if arr[j] > arr[j+1]:
            arr[j] = arr[j+1]
            arr[j+1] = arr[j]

   return arr


print(bubble_sort([1,4,7,2,9,3,8,32,7,32,5,35,78,47]))