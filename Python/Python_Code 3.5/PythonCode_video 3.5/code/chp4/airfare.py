# airfare.py

age = int(input('How old are you? '))
if age <= 2:
    print('you fly for free')
elif 2 < age < 13:
    print('you pay the kids rate')
else:
    print('you pay regular adult fare')
          
