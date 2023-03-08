import datetime

current_year = datetime.datetime.now().year

birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year

for x in range(age, 0, -1):
    if x**2 >= current_year:
        print(f"You will be {x} years old in the year {x**2}.")
        break 