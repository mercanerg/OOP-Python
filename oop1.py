class Employee:
    emp_numbers = 0
    tax_rate = 0.70
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.mail = first_name[0:3] + '_' + last_name[0:3] + '@company.com'
        self.salary = salary
        Employee.emp_numbers +=1

    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)
        
    def apply_tax(self):
        net_salary = round(float(self.salary * self.tax_rate), 2)
        tax = round(float(self.salary - net_salary))
        return net_salary, tax

print('Employee of Numbers = ', Employee.emp_numbers)
emp_1 = Employee('Maximus', 'Ryan', 5000)
emp_2 = Employee('Shmit', 'Gibson', 5500)
print(emp_1.mail)
print('Full name of employee > ', emp_1.name())
print('Full name of employee > ', Employee.name(emp_2))
input('press ENTER to go on\n')

net_pay, income_tax = emp_2.apply_tax()
print('Gross Salary : €', emp_2.salary)
print('Net Salary   : €', net_pay)
print('Income Tax   : €', income_tax)
print(emp_1.__dict__)
input('press ENTER to go on\n')

Employee.tax_rate = 0.80
print(emp_1.tax_rate, 'emp_1 Tax rate changed')
print(emp_2.tax_rate, 'emp_2 Tax rate changed')

#employee 2
input('press ENTER to go on\n')
net_pay, income_tax = emp_2.apply_tax()
print(f'Gross Salary               : €{emp_2.salary}')
print(f'Net Salary (tax rate {emp_2.tax_rate})  : €{net_pay}')
print(f'Income Tax (tax rate {emp_2.tax_rate})  : €{income_tax}')

# employee 1
input('press ENTER to go on')
emp_1.tax_rate = 0.6
net_pay, income_tax = emp_1.apply_tax()
print(f'Gross Salary               : €{emp_1.salary}')
print(f'Net Salary (tax rate {emp_1.tax_rate})  : €{net_pay}')
print(f'Income Tax (tax rate {emp_1.tax_rate})  : €{income_tax}')

input('press ENTER to go on')
print('Employee of Numbers = ', Employee.emp_numbers)