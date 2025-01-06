def f(num):
    import queue
    binary = ""
    rests = queue.LifoQueue()
    while num > 0:
        rest = num%2
        num = num // 2
        rests.put(rest)

    while not rests.empty():
        binary = binary + str(rests.get())
    
    return binary 

number = int(input('Enter number: '))   
print(f'Natural number: {number}')
print(f'Binary number: {f(number)} ')