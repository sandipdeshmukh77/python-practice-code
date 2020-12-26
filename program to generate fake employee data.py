from random import *
alphabets='abcdefghijklmnopqrstuvwxyz'
digits='1234567890'
cities=['pune','aurangabad','mumbai','banglore','Nashik','chennai']
designation=['software engineer','testing engineer','developer',
'data analyst','java developer','security manager']

def emp_fake_name():
	ename=choice(alphabets).upper()
	n=randint(2,9)
	for i in range(n):
		ename=ename+choice(alphabets)
	return ename

def emp_fake_mono():
	eno=choice('6789')
	for i in range(9):
		eno=eno+choice(digits)
	return eno

def emp_fake_salary():
	return uniform(10000,50000)

def emp_fake_city():
	return choice(cities)

def emp_fake_number():
	eno='e-'
	for i in range(4):
		eno=eno+choice(digits)
	return eno
print(emp_fake_number())

def emp_fake_designation():
	return choice(designation)

def emp_fake_data():
	print('employee name:',emp_fake_name())
	print('employee number:',emp_fake_number())
	print('employee mobile number:',emp_fake_mono())
	print('employee city:',emp_fake_city())
	print('employee designation:',emp_fake_designation())
	print('employee salary:{:.2f}'.format(emp_fake_salary()))	
for i in range(3):
	emp_fake_data()
	print()