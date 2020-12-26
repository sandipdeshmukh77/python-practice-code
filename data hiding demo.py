class bank:
	def __balance(self):
		print('Your balance is = 10000')
	def getyourbalance(self):
		userid = input('enter your userid')
		passwd = input('enter your password')
		if userid=='sandip' and passwd=='sam123':
			self.__balance()
b=bank()
b.getyourbalance()


