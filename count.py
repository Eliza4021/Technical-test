#Write a program that counts the number of vowels in a sentence.

vowels=['a','e','i','o','u']
def CountVowels(sentence):
    found_vowels=[]
    for letter in sentence:
        if letter in vowels:
            found_vowels.append(letter)
    return len(set(found_vowels))
            

print(CountVowels("Hello World"))
