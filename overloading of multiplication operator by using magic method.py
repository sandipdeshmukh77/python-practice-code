class employee:
	def __init__(self,name,salperday):
		self.name=name
		self.salperday=salperday
	def __mul__(self,other):
		return self.salperday*other.workingdays
class timesheet:
	def __init__(self,name,workingdays):
		self.name=name
		self.workingdays=workingdays
e=employee('sam',1000)
t=timesheet('sam',25)
print('the total salary is',e*t)
#this will call magic method from employee class because we e first in e*t 
# if t is first(t*e) them it will call magic method from timesheet class
		