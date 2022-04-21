""" It is avaliable to inject code or modify functions or classes by using decorators.  
Aspect Oriented Programming (AOP) in Java sounds a bit like that, doesn't it? """

class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def email(self):
        return '{}_{}@company.com'.format(self.first_name, self.last_name)
    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @name.setter
    def name(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name
    
    @name.deleter
    def name(self):
        print('name was deleted')
        self.first_name = None
        self.last_name = None
        

emp1 = Employee('Lucas', 'Amelia')
emp1.name = 'Mia Larson'

print(emp1.first_name)
print(emp1.last_name)
print(emp1.name)
print(emp1.email)

del emp1.name
print(emp1.first_name)
print(emp1.name)