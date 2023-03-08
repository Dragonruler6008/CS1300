"""
*coffee coffee coffee coffee coffee coffee,
Just kidding this program calculates the time
and amount respectivly for when your body gets below 65mg
and how much you have after 24 hours.
The last function is just rediculous and you
drink a cup every hour for 24 hours and have a heart attack.

Lucas Bigler
CS-1300
2/8/2023
"""

# Declaring all the Globals for the first two functions
HOURS = 0
CAFFEINE = 130
INITIAL_AMOUNT = 0

# This is used to prevent the code from running all the time in a loop,
# it just keeps it more compartmentalized.
CAFFEINE_TOO_MUCH = True
CAFFEINE24 = True
WAYTOOMUCH = True

# Function one tells you how many hours it
# takes till you have less than 65mg of caffeine in your body.
while CAFFEINE_TOO_MUCH is True:
    # checks caffeine level and if true ends the loop
    if CAFFEINE < 65:
        print("It will take", HOURS,
              "hours untill less than 65 mg of caffeing remains in the body.\n")
        CAFFEINE_TOO_MUCH = False
    else:
        # Decrements caffeine level and adds an hour to the counter.
        CAFFEINE *= .87
        HOURS += 1

# Function two builds off of function one allowing it to
# use variables that have been edited in function one.
while CAFFEINE24 is True:
    # Checks the hour count to see if it has been 24 hours, and when it has, termintae the loop.
    if HOURS == 24:
        CAFFEINE = round(CAFFEINE, 2)
        print(
            f"After 24 hours, there will be {CAFFEINE:.2f} mg of caffeine in the body.\n")
        CAFFEINE24 = False
    else:
        # decrements the caffeine variable and adds an hour to the counter
        CAFFEINE *= .87
        HOURS += 1

# Reset these variables to make it easy for this function to work properly.
HOURS = 0
CAFFEINE = 130
while WAYTOOMUCH is True:
    # we use the initial ammount in the calculations below.
    INITIAL_AMOUNT = CAFFEINE
    # check the hour counter for when it hits 24 then terminates the loop.
    if HOURS == 24:
        # prints with a nicely formatted two decimal places
        print(
            f"After 24 hours of too much coffee, there will be \n{CAFFEINE:.2f}",
            "mg of caffeine in the body. And you have suffered a Heart Attack\n")
        WAYTOOMUCH = False
    else:
        # sets the hours to 24 for the for loop to work
        HOURS = 24
        # Calculates the total amount of caffeine in the body and stores it in the caffeine variable
        for i in range(0, HOURS):
            CAFFEINE = CAFFEINE * 0.87 + INITIAL_AMOUNT
