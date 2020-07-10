# write.py

import os

def make_story1():
    """ Writes a story to the file 'story.txt'.
    """
    f = open('story.txt', 'w')
    f.write('Mary had a little lamb,\n')
    f.write('and then she had some more.\n')
    
def make_story2():
    """ Writes a story to the file 'story.txt'.
    If the file story.txt alreay exist, then it does
    nothing.
    """
    if os.path.isfile('story.txt'):
        print('story.txt already exists; nothing written')
    else:
        f = open('story.txt', 'w')
        f.write('Mary had a little lamb,\n')
        f.write('and then she had some more.\n')

def add_to_story(line, fname = 'story.txt'):
    """ Appends line to the end of the given file.
    """
    f = open(fname, 'a')
    f.write(line)

def insert_title(title, fname = 'story.txt'):
    """ Inserts title as the first line of fname.
    """
    f = open(fname, 'r+')

    temp = f.read()
    temp = title + '\n\n' + temp
    
    f.seek(0)  # reset file pointer to beginning
    f.write(temp)
