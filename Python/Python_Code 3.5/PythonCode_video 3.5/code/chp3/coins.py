# coins.py

# This program asks the user how many coins of various
# types they have, and then prints the total amount
# of money in pennies.

# get the number of nickels, dimes, and quarters
# from the user
nickels = int(input('How many nickels do you have? '))
dimes = int(input('How many dimes do you have? '))
quarters = int(input('How many quarters do you have? '))

# calculate the total amount of money
total = 5 * nickels + 10 * dimes + 25 * quarters

# print the results
print()  # prints a blank line
print('You have exactly ' + str(total) + ' cents.')
