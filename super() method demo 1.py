class p:
	a=10
	def __init__(self):
		self.c=30
		print('parent constructer')
	def m1(self):
		self.b=20
		print('parent instance method')
	@classmethod
	def m2(cls):
		print('parents class method')
	@staticmethod
	def m3():
		print('parents static method')
class c(p):
	def __init__(self):
		super().__init__()
		self.m1()
		self.m2()
		self.m3()
		print(self.b)
		print(self.a)
		print(self.c)
	def m4(self):
		super().__init__()
		self.m1()
		self.m2()
		self.m3()
		print(self.b)
		print(self.a)
		print(self.c)
	@classmethod
	def m5(cls):
		super(c,cls).__init__(cls)
		super(c,cls).m1(cls)
		super().m2()
		super().m3()
	@staticmethod
	def m6():
		super(c,c).m2()
		super(c,c).m3()
c.m6()

