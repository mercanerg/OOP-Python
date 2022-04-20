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
emp2 = Department('Carol', 'Stoneshout', 6000, 'Marketing')
manager1 = Manager('Helena', 'Isabel', 10000, [emp1])

print(isinstance(manager1, Manager))
print(isinstance(manager1, Employee))
print(isinstance(manager1, Department))
print(issubclass(Department, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Department))



