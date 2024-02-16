"""Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string."""
def capitalize(string_input):
    String_output = string_input.title()
    return String_output

user_input = input("Enter a string to capitalize: ")
print(capitalize(user_input))
