# global_correct.py

name = 'Jack'

def say_hello():
    print('Hello ' + name + '!')

def change_name(new_name):
    nonlocal name = new_name
