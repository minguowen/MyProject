# monty.py

"""
This simulates the infamous Monty Hall problem. Suppose Monty Hall,
a game show host, offers you a choice of one of three doors. Behind
one door is a car (which you want!), and behind the other two doors
are goats (which you definitely don't want).

After you make your choice, Monty opens one of the doors you didn't
choose to reveal one of the goats (he knows where the car and goats are).
Now he gives you a second choice: do you stick with the first door you
chose, or do you switch and take the door he didn't open?

This program estimates the probabilities of switching versus not
switching, and confirms the surprising answer that you have a much
better chance of winning if you switch doors!

Sample runs:

>>> main()
keep wins = 3399 (34.0%)
switch wins = 6656 (66.6%)
>>> main()
keep wins = 3297 (33.0%)
switch wins = 6570 (65.7%)
"""

def place_prizes():
    """ Randomly place the two goats and the cars.
    """
    prizes = ['goat', 'goat', 'car']
    random.shuffle(prizes)
    return prizes

def door_to_switch_to(choice, prizes):
    """ Returns the door number the player should switch to.
    """
    if choice == 0:
        return 2 if prizes[1] == 'goat' else 1
    elif choice == 1:
        return 0 if prizes[2] == 'goat' else 2
    else:
        return 1 if prizes[0] == 'goat' else 0

def keep_strategy(n = 10000):
    """ Perform the "don't switch" strategy n times.
    Returns the number of wins (which should be about n/3).
    """
    wins = 0
    for i in range(n):
        prizes = place_prizes()
        choice = random.randrange(3)
        if prizes[choice] == 'car':
            wins += 1
    return wins

def switch_strategy(n = 10000):
    """ Perform the "switch doors" strategy n times.
    """
    wins = 0
    for i in range(n):
        prizes = place_prizes()
        choice = random.randrange(3)
        switch_door = door_to_switch_to(choice, prizes)
        if prizes[switch_door] == 'car':
            wins += 1
    return wins

def main():
    keep_wins = keep_strategy()
    switch_wins = switch_strategy()
    print('keep wins = %s (%.1f%%)' % (keep_wins, 100 * keep_wins / 10000))
    print('switch wins = %s (%.1f%%)' % (switch_wins, 100 * switch_wins / 10000))
