class Student(object):
   def __init__(self, name, score):
       self.name = name
       self.score = score
   def print_score(self):
       print("%s: %d" % (self.name, self.score))

   def get_grade(self):
       if self.score >= 90:
           return 'A'
       if self.score >= 60:
           return 'B'
       else:
           return 'C'

bart = Student('Bart Simpson', 59)
bart.print_score()
print(bart.name,    ':' , bart.get_grade())
print(bart.name, ':' , bart.get_grade())
print(bart.name + ':' + bart.get_grade())
#print(bart.name)
#print(bart.score)
