class student:
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks
	def display(self):
		print('hello',self.name)
		print('your marks is',self.marks)
	def grade(self):
		if self.marks>=60:
			print('you got first grade')
		elif self.marks>=50:
			print('you got second grade')
		elif self.marks>=35:
			print('you got third grade')
		else:
			print('you are failed')
n=int(input('enter number of students'))
students=[] #empty list
for i in range(n):
	name=input('enter your name')
	marks=int(input('enter your marks'))
	s=student(name,marks)
	students.append(s)
for s in students:
	s.display()
	s.grade()
	print()

	