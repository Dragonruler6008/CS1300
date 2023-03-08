##Car Loan Write a program to analyze a car loan. See Fig. 3.79. The user should enter the amount of the loan, the annual percentage rate of interest, and the duration of the loan in months. After each piece of data is entered, the data should be checked to make sure it is reasonable. If bad data has been supplied, the user should be so advised. Otherwise, the monthly payment and the total amount of interest paid should be displayed. The formula for the monthly payment is

loan = float(input("Enter the amount of the loan: "))
InterestRate = float(input("Enter the interest rate: "))
duration = int(input("Enter the duration in months: "))
monthlyPayment = (loan - InterestRate)/1-(1+InterestRate)**-duration
print("Monthly payment: $", str(monthlyPayment),sep="")
print("total interest paid: $", str(duration*monthlyPayment-loan),sep="")

##Write a program to determine the real roots of the quadratic equation 
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
smallPart = 0 ##b**2 - 4*a*c part
if a == 0:
    print("A cannot be 0")
    a = int(input("Enter a: "))
else:
    smallPart = b**2 - 4*a*c
    if smallPart < 0:
        print("This eqiations has no real roots.")
    elif smallPart == 0:
        displayOneRoot = -b/(2*a)
        print("The equation has no real roots.")
    else:
        displayFirst = (-b + sqrt(smallPart))/(2*a)
        displaySecond = (-b - sqrt(smallPart))/(2*a)
        print("The equation has two real roots:", displayFirst, "and", displaySecond)

#Caffeine Absorption After caffeine is absorbed into the body, 13% is eliminated from the body each hour. Assume a person drinks an 8-oz cup of brewed coffee containing 130 mg of caffeine, and that the caffeine is absorbed immediately into the body. Write a program to calculate the following values.
print("CAFFEINE VALUES")
caffeine = 130
count = 0
while count > 65:
    caffeine *= .87
    count += count
print("One cup: less than 65 mg. Will remain after", count, "hours." )
while count < 24:
    caffeine *= .87
    count += count
print("One cup:", caffeine, ". will remain after", count, "hours")
caffeine = 130
for i in range(24):
    caffeine *= 0.83
    caffeine += 130
print("Hourly cup:", caffeine, "mg. will remain after 24 hours.")

#Rule of 72 This rule is used to approximate the time required for prices to double due to inflation. If the inflation rate is r%, then the Rule of 72 estimates that prices will double in 72/r years. For instance, at an inflation rate of 6%, prices double in about 72/6 or 12 years. Write a program to test the accuracy of this rule. For each interest rate from 1% to 20%, the program should display the rounded value of 72/r and the actual number of years required for prices to double at an r% inflation rate. (Assume prices increase at the end of each year.) Fig. 3.82 shows the first five sets of values.
print("Rule of 72".center(38))
print("Interest Doubleing Time", "Actual Doubling".rjust(16))
print("rate".rjust(13), "(in years) Time (inyears)")
startAmount = 10000
estimated = 72
count = 0
for i in range(1, 21):
    while startAmount <= 20000:
        startAmount *= (1 + (i/100))
        count += 1
    estimated = int(72/i)    
    print(str(i),"%".ljust(9),str(estimated).ljust(14),str(count),sep="")
    count = 0
    startAmount = 10000
    
#Individual Retirement Accounts Money earned in an ordinary savings account is subject to federal, state, and local income taxes. However, a special type of retirement savings account, called a traditional individual retirement account (traditional IRA), allows these taxes to be deferred until after retirement. IRAs are highly touted by ­financial planners. The purpose of this programming project is to show the value of starting an IRA early. Earl and Larry each begin full-time jobs in January 2015 and plan to retire in January 2063 after working for 48 years. Assume that any money they ­deposit into IRAs earns 4% interest compounded annually. Earl opens a traditional IRA account immediately and deposits $5,000 into his account at the end of each year for fifteen years. After that he plans to make no further deposits and just let the money earn interest. Larry plans to wait fifteen years before opening his traditional IRA and then deposit $5,000 into the account at the end of each year until he retires. Write a program that calculates the amount of money each person has deposited into his account and the amount of money in each account upon retirement.
earl_years = 15
earl_amount = 5000
earl_interest_rate = 0.04
earl_balance = 0

for i in range(earl_years):
    earl_balance = earl_balance + earl_amount
    earl_balance = earl_balance * (1 + earl_interest_rate)

earl_total_deposit = earl_years * earl_amount

larry_years = 33
larry_amount = 5000
larry_interest_rate = 0.04
larry_balance = 0

for i in range(larry_years):
    larry_balance = larry_balance + larry_amount
    larry_balance = larry_balance * (1 + larry_interest_rate)

larry_total_deposit = larry_years * larry_amount
print("                                                      AMOUNTS DEPOSITED")
print("Earl's total deposit: $", round(earl_total_deposit,2), "     ", "Larry's account balance upon retirement: $", round(larry_balance,2))
print("                                                AMOUNTS IN IRA UPON REITREMENT")
print("Earl's account balance upon retirement: $", round(earl_balance,2), "      ", "Larry's total deposit: $", round(larry_total_deposit,2))

#Soundex System Soundex is a system that encodes a word into a letter followed by three numbers that roughly describe how the word sounds. Similar sounding words have the same four-character codes. For instance, the words Carrot and Caret are both coded as C123. A slight variation of the Soundex coding algorithm is as follows:
word = input("Enter a word: ")

# Retain the first letter
soundex = word[0].upper()

# Delete all occurrences of a, e, i, o, u, h, y, and w
word = word.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("h", "").replace("y", "").replace("w", "")

# Assign numbers to the other letters that remain
result = ""
for letter in word:
    if letter in "bfpv":
        result += "1"
    elif letter in "cgjkqsxz":
        result += "2"
    elif letter in "dt":
        result += "3"
    elif letter == "l":
        result += "4"
    elif letter in "mn":
        result += "5"
    elif letter == "r":
        result += "6"

# If two or more letters that have been replaced by the same number were next to each other, keep only the first of them
soundex += ''.join([result[i] for i in range(1, len(result)) if result[i] != result[i-1]])

# Keep only the first four characters of what you have left. If fewer than four, then add zeros on the end to make the string have length four
soundex += '0' * (4 - len(soundex[1:]))

print("The Soundex code of the word is:", soundex)

#Error Detection Suppose you type a 14-digit credit card number into a Web site, but mistype one of the digits or inadvertently interchange two adjacent digits. The Web site will perform a validation check that always detects the first type of error and nearly always detects the second type of error. The validation check is as follows:
credit_card_number = input("Enter a 14-digit credit card number: ")

doubled_digits_sum = 0
remaining_digits_sum = 0

for i in range(len(credit_card_number)):
    if i % 2 == 0:
        doubled_digit = int(credit_card_number[i]) * 2
        if doubled_digit > 9:
            doubled_digit -= 9
        doubled_digits_sum += doubled_digit
    else:
        remaining_digits_sum += int(credit_card_number[i])

total_sum = doubled_digits_sum + remaining_digits_sum

if total_sum % 10 == 0:
    print("Accepted")
else:
    print("Rejected")
#Palindrome A palindrome is a word or phrase that reads the same forward and backward, character for character, disregarding punctuation, case, and spaces. Some examples are “racecar”, “Madam, I’m Adam”, and “Was it a cat I saw?”. Write a program that asks the user to input a word or phrase and then determines if it is a palindrome
import string

# Get the user's input
user_input = input("Enter a word or phrase: ")

# Remove all spaces and punctuation
user_input = user_input.lower().translate(str.maketrans("", "", string.punctuation))
user_input = user_input.replace(" ", "")

# Check if the input is a palindrome and print the result
if user_input == user_input[::-1]:
    print("The word or phrase is a palindrome.")
else:
    print("The word or phrase is not a palindrome.")
