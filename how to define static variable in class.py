class test:
	a=10
	def __init__(self):
		self.c=30
		test.b=20
	def m1(self):
		test.c=40
	@classmethod
	def m2(cls):
		cls.d=50
		test.e=60
	@staticmethod
	def m3():
		test.f=70

t=test()
t.m1()
test.m2()
test.m3()
test.g=80
print(test.__dict__)	



