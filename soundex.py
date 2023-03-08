"""
A peice of code known as a soundex system.
This code allows for the encoding of a name into a letter and 3 numbers.
Lucas Bigler
CS-1300
2/16/23
"""
# Imports for later
import random
import time

# Set variable to true for code repetability later.
AGAIN = True

# Loop so the user can run more than one letter.
while AGAIN is True:
    # Gets a user input for a word of choice
    word = input("Enter a word! : ")

    # lowercase the entire word and remove added spaces by accident
    word = word.lower().strip()

    # Set "first" var to an uppercase version of the first char in the word
    first = word[0].upper()

    # Sets soundexword to the first letter for later
    SOUNDEXWORD = first

    # Compute length for word and if more than 4, set length to 4 to prevent too many outputs.
    LENGTH = len(word)

    # Run for all the length for the range will output first letter with number codes after it.
    for i in range(1, LENGTH):
        match word[i]:
            case "b":
                SOUNDEXWORD += "1"
            case "f":
                SOUNDEXWORD += "1"
            case "p":
                SOUNDEXWORD += "1"
            case "v":
                SOUNDEXWORD += "1"
            case "c":
                SOUNDEXWORD += "2"
            case "g":
                SOUNDEXWORD += "2"
            case "j":
                SOUNDEXWORD += "2"
            case "k":
                SOUNDEXWORD += "2"
            case "q":
                SOUNDEXWORD += "2"
            case "s":
                SOUNDEXWORD += "2"
            case "x":
                SOUNDEXWORD += "2"
            case "z":
                SOUNDEXWORD += "2"
            case "d":
                SOUNDEXWORD += "3"
            case "t":
                SOUNDEXWORD += "3"
            case "l":
                SOUNDEXWORD += "4"
            case "m":
                SOUNDEXWORD += "5"
            case "n":
                SOUNDEXWORD += "5"
            case "r":
                SOUNDEXWORD += "6"
            # Passes the letters that need to be skipped.
            case "a":
                pass
            case "e":
                pass
            case "i":
                pass
            case "o":
                pass
            case "u":
                pass
            case "h":
                pass
            case "y":
                pass
            case "w":
                pass
            # in case of undefined letter or other set to 0
            case _:
                SOUNDEXWORD += "0"

    # If two or more letters that have been replaced by the same number
    # were next to each other, keep only the first of them
    first += ''.join([SOUNDEXWORD[i] for i in range(1, len(SOUNDEXWORD))
                      if SOUNDEXWORD[i] != SOUNDEXWORD[i-1]])

    # compute the needed number of extra zeros and add them to the program
    # if none are needed, do not add them.
    if 1 < len(first) < 3:
        first += "0"
        first += "0"
    elif 2 < len(first) < 4:
        first += "0"
    else:
        pass

    # prints out the soundex code for the user
    print("The soundex code for the word you entered is: ", first)

    # provides the code for the slow printing.
    def print_slow(string):
        """makes line print slow when string passed in.

        Args:
            str (String): Takes in string and prints it out slowly.
        """
        for letter in string:
            print(letter, end='', flush=True)
            time.sleep(random.randint(10, 15)/100)

    # Asks the user if they would like to enter another word.
    # If not it ends the program and prints a cool leaving statment.
    if input("would you like to do another word? (yes , no) : ") != "yes":
        AGAIN = False
        print_slow("Exiting... Goodye!")
