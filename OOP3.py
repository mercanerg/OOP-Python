class Employee:
    emp_numbers = 0
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
        net_salary = round(float(self.salary * self.tax_rate), 2)
        tax = round(float(self.salary - net_salary))
        return net_salary, tax

class Department(Employee):
    tax_rate = 0.8
    def __init__(self, first_name, last_name, salary, department):
        super().__init__(first_name, last_name, salary)
        self.department = department

class Manager(Employee):
    tax_rate = 0.6
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
        if employees is None:
            employees = []
        else:
            self.employees = employees

    def append_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def delete_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def display_emp(self):
        for emp in self.employees:
            print('*', emp.name(), '*')

emp1 = Department('George', 'Carel', 5000, 'Account')
emp2 = Employee('Carol', 'Stoneshout', 6000)
man1 = Manager('Helena', 'Isabel', 10000, 'Sales Manager')

print(emp1.name(), emp1.mail )
print(emp2.name(), emp2.mail )
print('===================================')
# print(help(Department))
income1, tax_amount1 = emp1.apply_tax()
print(emp1.name(), emp1.department, emp1.mail, income1, emp1.salary, emp1.tax_rate)
income2, tax_amount2 = emp2.apply_tax()
print(emp2.name(), emp2.salary, emp2.mail, income2, emp2.tax_rate)
print('-----------------------------------------')
print(man1.name(), man1.employees)

man2 = Manager('Sarah', 'Juliet', 8000, [emp1])
man2.append_employee(emp2)
print(man2.name(), man2.mail)
man2.display_emp()
print('----------------------------------')
man2.delete_employee(emp2)
man2.display_emp()