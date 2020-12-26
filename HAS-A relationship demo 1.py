class car:
	def __init__(self,name,model,color):
		self.name=name
		self.model=model
		self.color=color
	def getinfo(self):
		print('the name of car is:{} ,model:{},color:{}'.format(self.name,self.model,self.color))
class employee:
	def __init__(self,ename,eno,car):
		self.ename=ename
		self.eno=eno
		self.car=car
	def empinfo(self):
		print('name of the employee',self.ename)
		print('employee number',self.eno)
		print('employee car info')
		self.car.getinfo()
car=car('honda','city','black')
e=employee('sandip',19928,car)
e.empinfo()