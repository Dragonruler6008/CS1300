"""This code checks a credit card and validates it to make sure it is correct."""
# --------------
# Lucas Bigler
# 2/24/23
# CS 1300
# -------------

# store user input
inptnum = input("Enter a credit card number: ")

# Creative element, clean number input up from user. (Not that creative but gimme a break)
inptnum = inptnum.strip()
inptnum = inptnum.replace('-', '').replace(' ', '')

# variables for even and odd sums of num variable
evennum = 0
oddnum = 0

# gets the first and every second after then multiplies it by two.
# it then makes any double digit numbers single again and adds them up.
for i in range(0, len(inptnum), 2):
    digit = int(inptnum[i]) * 2
    if digit >= 10:
        digit -= 9
    evennum += digit

# add the odds of the numbers together and set it to the oddsum
for i in range(1, len(inptnum) + 1, 2):
    oddnum += int(inptnum[i])

# Compare output of each and check if output is divisable by 10 and is 14 letters long.
if (evennum + oddnum) % 10 == 0 and len(inptnum) == 14:
    print("The number is valid.")
else:
    print("The number is not valid.")
