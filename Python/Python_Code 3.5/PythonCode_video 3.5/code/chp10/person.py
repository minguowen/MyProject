# person.py

class Person:
    """ Class to represent a person
    """
    def __init__(self, name = '', age = 0):
        self._name = name
        self._age = age
        self.__test = 5

    @property
    def age(self):
        """ Returns this person's age.
        """
        return self._age

    @age.setter
    def age(self, age):
        """ Sets self.age to be age if 0 < age <= 150.
        If age is not within that range, then self.age is
        not changed.
        """
        if 0 < age <= 150:
            self._age = age

    def display(self):
        """ Prints the object on the console.
        """
        print(self)

    def __str__(self):
        """ String representation of a Person.
        """
        return "Person('%s', %s)" % (self._name, self._age)

    def __repr__(self):
        return str(self)


