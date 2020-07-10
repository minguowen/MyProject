# coins_short.py

# This program asks the user how many
# coins of various types they have,
# and then prints the total amount
# of money in pennies.

# get the number of nickels, dimes,
# and quarters from the user
n = int(input('Nickels? '))
d = int(input('Dimes? '))
q = int(input('Quarters? '))

# calculate the total amount of money
total = 5 * n + 10 * d + 25 * q

# print the results
print()  # prints a blank line
print(str(total) + ' cents')
