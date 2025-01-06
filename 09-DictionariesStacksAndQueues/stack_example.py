import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put('King of Hearts \u2665')    
cards.put('Queen of Diamonds \u2666')  
cards.put('Jack of Spades \u2660')     

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# removes and prints elements from the top of the stack
while not cards.empty():
    card = cards.get()
    print(card)

"""
Note the order of the printed elements.
The last added element is printed first.
"""
numbers = queue.LifoQueue()
numbers.put(2)
numbers.put(3)
numbers.put(7)
numbers.put(4)
numbers.put(1)
numbers.put(9)
numbers.put(8)
num1 = numbers.get()
num2 = numbers.get()
print(num1 + num2)