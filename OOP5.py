
class Employee:

    tax_rate = 0.70

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.salary = salary

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_tax(self):
        net_salary = round(float(self.salary * self.tax_rate), 2)
        tax = round(float(self.salary - net_salary))
        return net_salary, tax

    def __repr__(self): # concanating strings
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.salary)

# This function returns the employee's name and address using the str
# built-in function
    def __str__(self): 
        return 'Name :{} - email :{}'.format(self.fullname(), self.email)

# This function returns sum of the employees'salaries using the add
# built-in function
    def __add__(self, other): 
        return self.salary + other.salary

# This function returns length of the employee's fullname using the len
# built-in function
    def __len__(self):
        return len(self.fullname())


emp1 = Employee('George', 'Carel', 5000)
emp2 = Employee('Carol', 'Stoneshout', 6000)

print(emp1)
print(repr(emp1))
print(emp1+emp2)
print(len(emp1))