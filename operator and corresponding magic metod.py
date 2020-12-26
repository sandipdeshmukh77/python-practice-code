class student:
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks
	def __gt__(self,other): # you can perform __gt__ and __lt__ operation by using any one of them
		return self.marks>other.marks
	def __le__(self,other): # you can perform __ge__ and __le__ operation by using any one of them
		return self.marks>=other.marks
		
s1=student('sam',100)
s2=student('jack',200)
print(s1>s2)
print(s1<s2)
print(s1>=s2)
print(s1<=s2)


