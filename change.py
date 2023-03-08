"""
This program makes change out of a user input from 0 to any amount, will accept both dollars and
euros. I know its a bit clunky but this is my first time with python so I know nothing of
optimal placements for things.

Name: Lucas Bigler
Date: 1/30/23
Class: CS 1300
"""
# define coin denominations
denomination = [100, 25, 10, 5, 1]
eudenomination = [100, 50, 20, 10, 5, 2, 1]

# pre declare these variables false for program functionality
US = False
EU = False

# ask user for which denomination to use will accept a string labeled "Dollar" or "Euro"
MSG = "Enter 'Dollar' or 'Euro' to get change from that denomination: "
if input(MSG) != "Euro":
    # get input from user and tell them instructions.
    # Changes variable to true so the program knows what coin denomination to use
    amount = int(input("Enter the amount of money in cents (0-any amount): "))
    US = True
else:
    # get input from user and tell them instructions.
    # Changes variable to true so the program knows what coin denomination to use
    euamount = int(
        input("Enter the amount of money in EUcents (0-any amount): "))
    EU = True

# initialize dollar variables when needed to store the number of coins for display later
if US is True:
    DOLLARS = 0
    QUARTERS = 0
    DIMES = 0
    NICKELS = 0
    PENNIES = 0

# initialize euro variables when needed for use / display later
else:
    EURO = 0
    HALFEURO = 0
    TWENTYERO = 0
    TENEURO = 0
    FIVEEURO = 0
    TWOEURO = 0
    ONEEURO = 0

# make change from US coins, this relies on the US/EU variables to tell what side to run
if US is True:
    # start by getting remainders starting for dollars (100c)
    for coin in denomination:
        if coin == 100:
            dollars = amount // coin
            amount = amount % coin
        # get quarters via remainder
        elif coin == 25:
            quarters = amount // coin
            amount = amount % coin
        # get dimes via remainder
        elif coin == 10:
            dimes = amount // coin
            amount = amount % coin
        # get nickels via remainder
        elif coin == 5:
            nickels = amount // coin
            amount = amount % coin
        # get pennies via remainder
        elif coin == 1:
            pennies = amount // coin
            amount = amount % coin

    # output the results in an esay to read format
    print("\nHere is the change from your coins!")
    print("Dollars:", dollars)
    print("Quarters:", quarters)
    print("Dimes:", dimes)
    print("Nickels:", nickels)
    print("Pennies:", pennies, "\n")

# This is the calculations for the euro side of the coins
else:
    for coin in eudenomination:
        # get remainder for full euros
        if coin == 100:
            EURO = euamount // coin
            euamount = euamount % coin
        # get remainder from half euro coins
        elif coin == 50:
            HALFEURO = euamount // coin
            euamount = euamount % coin
        # get remainder for 20c coins
        elif coin == 20:
            TWENTYERO = euamount // coin
            euamount = euamount % coin
        # get remainder for 10c coins
        elif coin == 10:
            TENEURO = euamount // coin
            euamount = euamount % coin
        # get remainder for 5c coins
        elif coin == 5:
            FIVEEURO = euamount // coin
            euamount = euamount % coin
        # get remainder for 2c coins
        elif coin == 2:
            TWOEURO = euamount // coin
            euamount = euamount % coin
        # get remainder for 1c coins
        elif coin == 1:
            ONEEURO = euamount // coin
            euamount = euamount % coin
    # output the results in an esay to read format
    print("\nHere is the change from your coins!")
    print("Euro:", EURO)
    print("50c Euro:", HALFEURO)
    print("20c Euro:", TWENTYERO)
    print("10c Euro:", TENEURO)
    print("5c Euro:", FIVEEURO)
    print("2c Euro:", TWOEURO)
    print("1c Euro", ONEEURO, "\n")
