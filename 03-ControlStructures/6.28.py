def fibonacci_sequence(n):
    sequence = ""
    a, b = 0, 1
    for i in range(n):
        sequence  = sequence + str(a) + " "
        a, b = b, a + b
    return sequence

# Print the first twenty words of the Fibonacci sequence
if __name__ == "__main__":
    print(fibonacci_sequence(20))