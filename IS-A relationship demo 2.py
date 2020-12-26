class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def eatdrink(self):
		print('eats biryani and drink beer')
class employee(person):
	def __init__(self,name,age,eno,esal):
		#self.name=name      no need to write again we can use this from parent class
		#self.age=age		 by using 'super().__init__(name,age)'
		super().__init__(name,age)
		self.eno=eno
		self.esal=esal
	def work(self):
		print('i am python programer')
	def empinfo(self):
		print(self.name)
		print(self.age)
		print(self.eno)
		print(self.esal)
e=employee('sandip',26,14888,10000)
e.eatdrink()
e.work()
e.empinfo()
