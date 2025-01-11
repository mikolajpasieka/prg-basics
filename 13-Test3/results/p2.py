def f(wyrażenie):
    import queue
    queue1 = queue.LifoQueue
    characters = wyrażenie.split()

    for char in characters:
        if char.isdigit():
            queue1.put(char)
        if char == "+":
            a = queue1.get()
            b = queue1.get()
            z = a + b 
            queue1.put(z)
        if char ==  "-":
            a = queue1.get()
            b = queue1.get()
            z = a - b 
            queue1.put(z)
    return  queue1.get()

if __name__ == "__main__":
    print(f("2 3 +"))
    print(f("2 6 + 4 5 - +"))
    print(f("11 7+ 15 - 14 +"))
