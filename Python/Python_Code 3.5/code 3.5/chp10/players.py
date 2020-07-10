# players.py

class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0

    def reset_score(self):
        """ Resets the players score to 0.
        """
        self._score = 0

    def incr_score(self):
        """ Increases the player's score by 1.
        """
        self._score = self._score + 1

    def get_name(self):
        """ Return this player's name.
        """
        return self._name

    def __str__(self):
        return "name = '%s', score = %s" % (self._name, self._score)

    def __repr__(self):
        return 'Player(%s)' % str(self)


class Human(Player):
    def __repr__(self):
        return 'Human(%s)' % str(self)

    def get_move(self):
        while True:
            try:
                n = int(input('%s move (1 - 10): ' % self.get_name()))
                if 1 <= n <= 10:
                    return n
                else:
                    print('Oops: your move must be in the range 1 - 10')
            except:
                print('Please enter an integer from 1 - 10.')
        

class Computer(Player):
    import random
    def __repr__(self):
        return 'Computer(%s)' % str(self)

    def get_move(self):
        return random.randint(1, 10)


def play_undercut(p1, p2):
    """ Plays one round of Undercut.
    Returns a tuple of three values (p1, p2, message). The p1 and p2
    are the passed-in player objects; if there was a winner, then that
    player's object will have its score increased by 1. The message
    indicates who won the game, or if it was a draw
    """
    p1.reset_score()
    p2.reset_score()
    m1 = p1.get_move()
    m2 = p2.get_move()
    print("%s move: %s" % (p1.get_name(), m1))
    print("%s move: %s" % (p2.get_name(), m2))
    if m1 == m2 - 1:
        p1.incr_score()
        return p1, p2, '%s wins!' % p1.get_name()
    elif m2 == m1 - 1:
        p2.incr_score()
        return p1, p2, '%s wins!' % p2.get_name()
    else:
        return p1, p2, 'draw: no winner'
