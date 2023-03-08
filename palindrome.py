"""Checks a word or phrase to see if it is a palindrome"""
# --------------
# Lucas Bigler
# 2/24/23
# CS 1300
# -------------

# gets the user input and sets it to another variable for later.
word = str(input("Enter a word or phrase to see if it is a palindrome: "))
inputstring = word

# Cleans up user input to make the code run correctly.
word = word.replace(' ', '').replace(',', '').replace(
    ':', '').replace(':', '').replace('.', '')
word = word.upper()

# reverses the phrase/word and then compares the strings to see if it is a palindrome.
word1 = word
word = word[::-1]
if word1 == word:
    print("\n", inputstring, "is a(n) palindrome\n")
else:
    print("\n", inputstring, "is not a(n) palindrome\n")
    # Creative element, Asks user on failed input if they want to hear examples.
    if input(" Would you like to hear an example of a palindrome? (yes , no): ") == "yes":
        print("Some examples of palindromes are as follows: racecar, radar, civic, rotator")
    else:
        exit

# test input for validation.
# A MAN, A PlAN, A CANAL: PANAMA.
