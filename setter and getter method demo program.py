class student:
	def setName(self,name):
		self.name=name
	def getName(self):
		return self.name
	def setMarks(self,marks):
		self.marks=marks
	def getMarks(self):
		return self.marks
students=[]
n=int(input('enter number of student'))
for i in range(n):
	s=student()
	name=input('enter name')
	marks=int(input('enter marks'))
	s.setname(name)
	s.setMarks(marks)
	students.append(s)

for s in students:

	print('hello',s.getName())
	print('your marks is',s.getMarks())
	print()

	

