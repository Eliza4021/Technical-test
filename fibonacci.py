"""Write a program to generate the Fibonacci sequence up to 100."""
fibonacciSequence = [0, 1]
while True:
    z = fibonacciSequence[-1] + fibonacciSequence[-2]
    if z > 100:
        break
    else:
        fibonacciSequence.append(z)
print(fibonacciSequence)