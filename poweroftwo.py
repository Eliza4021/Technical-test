"""Write a program that takes an integer as input and returns true if the input is a power of two."""

def power(n):
    if n <= 0:
        return False
    
    while n % 2 == 0:
        n //= 2
    
    return n == 1
    user_input = int(input("Enter an integer: ")) 
print(power(user_input))
