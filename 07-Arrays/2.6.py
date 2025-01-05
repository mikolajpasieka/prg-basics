x = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for row in x:
    i = 0
    while i < len(x):
        x[i][i] = 1 
        i += 1 

for row in x: 
    for i in row:
        print(i, end=" ")
    print()
