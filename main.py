

class Employee:

# init function includes main attributes of the class
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.mail = first_name[0:3] + '.' + last_name[0:3] + '@company.com'
        self.salary = salary

# the following functions return some atributes of Employee
    def name(self):
        return self.first + self.last
    def mail(self):
        return self.mail
    def salary(self):
        return self.salary

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'Employee', 60000)
print(emp1.name())
print(emp1.mail())
print(emp1.salary())