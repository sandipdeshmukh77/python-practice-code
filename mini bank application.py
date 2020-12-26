class customer:
	bankname='SBI'
	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance=balance
	def deposit(self,amount):
		self.balance=self.balance+amount
		print('Balace after deposit',self.balance)
	def withdraw(self,amount):
		if amount>self.balance:
			print('insufficient fund')
		else:
			self.balance=self.balance-amount
			print('balance after withdraw',self.balance)


print('welcome to',customer.bankname)
name=input('Please enter your name:-')
c=customer(name)
while True:
	print('d-deposit\nw-withdraw\ne-exit')
	option=input('Please enter option')
	if option.lower()=='d':
		amount=float(input('Please enter amount to deposit'))
		c.deposit(amount)
	elif option.lower()=='w':
		amount=float(input('Please enter amount to withdraw'))
		c.withdraw(amount)
			
	elif option.lower()=='e':
		print('Thank you for banking with',c.bankname)
		break
	else:
		print('You have entered wronge keyword please select option again')

