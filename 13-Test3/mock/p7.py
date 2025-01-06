def f(arr2D):
   col_sums = [sum(row[i] for row in arr2D) for i in range(len(arr2D[0]))]
   return len(col_sums) != len(set(col_sums))
    
if __name__ == "__main__":
    print(f([[3,4,2],[5,1,6]]))
    print(f([[3,4,2],[5,1,7]])) 
    print(f([[3,4],[5,1],[4,7]])) 
    print(f([[3,4],[5,9],[4,7]]))  
