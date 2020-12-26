class test:
	def m1(self):
		def calc(a,b):
			print('the sum is',a+b)
			print('the subtraction is',b-a)
			print('the product is',a*b)
			print('the division is',a/b)
			print()
		calc(10,20)
		calc(20,30)
t=test()
t.m1()

