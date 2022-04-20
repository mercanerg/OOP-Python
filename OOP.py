class Customer:
    pass

cus_1 = Customer()
cus_2 = Customer()

print('cus_1 object memory stack', cus_1)
print('cus_2 object memory stack', cus_2)
input('press ENTER to go on\n')
cus_1.name = 'Ester'
cus_1.mail = 'esterdaan@company.com'
cus_1.pay = 1200

cus_2.name = 'Michel'
cus_2.mail = 'michelanderson@company.com'
cus_2.pay = 700

print(cus_1.name, cus_1.mail, cus_1.pay)
print(cus_2.name, cus_2.mail, cus_2.pay)
input('press ENTER to go on\n')