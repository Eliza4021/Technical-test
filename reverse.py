"""Write a program that takes an integer as input and returns an integer with reversed digit
ordering."""
def ReverseNumber(number):
    if number < 0:
        number *= -1
        return int(str(number)[::-1]) * -1
    else:
        return int(str(number)[::-1])

user_input = int(input("Enter an integer to reverse: "))
print(ReverseNumber(user_input))
