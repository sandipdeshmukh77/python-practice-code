class employee:
	def __init__(self,eno,ename,esal):
		self.eno=eno
		self.ename=ename
		self.esal=esal
	def display(self):
		print('employee number',self.eno)
		print('employee name',self.ename)
		print('employee salary',self.esal)
class manager:
	def modify(emp):
		emp.esal=emp.esal+10000
		emp.display()
emp=employee(101,'sandi',50000)
manager.modify(emp)
		