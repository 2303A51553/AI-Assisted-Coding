# Generate fibinocci in the given range iterativerly



# Generate fibinocci in the given range using recursion
def fibonacci_recursive(n, a=0, b=1, fib_sequence=None):
    if fib_sequence is None:
        fib_sequence = []
    if a < n:
        fib_sequence.append(a)
        return fibonacci_recursive(n, b, a + b, fib_sequence)
    return fib_sequence
limit = int(input("Enter the upper limit for Fibonacci sequence: "))
fib_sequence = fibonacci_recursive(limit)       
print("Fibonacci sequence up to", limit, "is:", fib_sequence)
