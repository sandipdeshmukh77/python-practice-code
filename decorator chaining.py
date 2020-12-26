def decor(func):
	def inner():
		x=func()
		return x*x
	return inner
def decor2(func):
	def inner():
		x=func()
		return x*2
	return inner
@decor2
@decor
def num():
	return 20
print(num())