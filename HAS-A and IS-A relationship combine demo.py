class car:
	def __init__(self,name,model,color):
		self.name=name
		self.model=model
		self.color=color
	def carinfo(self):
		print('name of car:{}\nmodel:{}\ncolor:{}'.format(self.name,self.model,self.color))

class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def eatdrink(self):
		print('eats biryani and drink beer')
class employee(person):
	def __init__(self,name,age,eno,esal,car):
		#self.name=name      no need to write again we can use this from parent class
		#self.age=age		 by using 'super().__init__(name,age)'
		super().__init__(name,age)
		self.eno=eno
		self.esal=esal
		self.car=car
	def work(self):
		print('i am python programer')
	def empinfo(self):
		print('name of the employee',self.name)
		print('age of the employee',self.age)
		print('employee number',self.eno)
		print('employee salary',self.esal)
		print('the car details:')
		self.car.carinfo()
car=car('mahindra','XUV500','black')
e=employee('sandip',26,14888,10000,car)
e.eatdrink()
e.work()
e.empinfo()
