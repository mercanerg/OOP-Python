class Employee:
    emp_numbers = 0  # defining a variable to use in the class 
    tax_rate = 0.70
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        email = first_name[0:3] + '_' + last_name[0:3] + '@company.com'
        self.mail = email.lower()
        self.salary = salary
        Employee.emp_numbers +=1

    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)
        
    def apply_tax(self):
        # calculating net salary
        net_salary = round(float(self.salary * self.tax_rate), 2)
        tax = round(float(self.salary - net_salary))
        return net_salary, tax

    @classmethod
    def set_tax_rate(cls, rate):
        cls.tax_rate = rate

    # defining classmethod
    @classmethod
    def convert_text(cls, emp_text):
        first_name, last_name, salary = emp_text.split('-')
        return cls(first_name, last_name, float(salary))
    # defining static method
    @staticmethod
    def workday(day):
    # The function returns False when Saturday or Sunday is involved, 
    # otherwise True
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('George', 'Carel', 5000)
emp2 = Employee('Carol', 'Stoneshout', 6000)
  
Employee.set_tax_rate(0.75)
print(Employee.tax_rate)
print(emp1.tax_rate)
print(emp1.tax_rate)
net_income1, tax1 = emp1.apply_tax()
print('Net income = ', net_income1,'Tax amount = ', tax1)

emp_str1 = 'Emma-Charlotte-4000'
emp_str2 = 'Elijah-Ava-5500'
emp3 = Employee.convert_text(emp_str1)
income, tax_amount = emp3.apply_tax()
print(f'{emp3.name()}   income = ${income}   tax amount = ${tax_amount}')
print(f'{emp3.name()}   email = {emp3.mail}')

import datetime
emp_date = datetime.date(2015, 10, 5)
print(Employee.workday(emp_date))