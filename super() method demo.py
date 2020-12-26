class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print("the name is",self.name)
		print('the age is',self.age)
class students(person):
	def __init__(self,name,age,rollno,marks):
		super().__init__(name,age)
		self.rollno=rollno
		self.marks=marks
	def display(self):
		super().display()
		print('the rollno is',self.rollno)
		print('the marks is',self.marks)
s=students('sandip',27,19,93)
s.display()

