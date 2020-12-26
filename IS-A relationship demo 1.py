class p:
	a=10
	def __init__(self):
		print('this is the parent instance method')
		self.b=20
	@classmethod
	def m2(cls):
		print('this is the parents class method')
	@staticmethod
	def m3():
		print('this is the parents static method')
class c(p):
	pass
	
c=c()
print(c.a)
print(c.b)
c.m2()
c.m3()

