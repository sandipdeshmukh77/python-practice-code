def decor(func):
	def inner(a,b):
		print('#'*30)
		print('The sum is:',end='')
		func(a,b)
		print('#'*30)
	return inner
		
@decor
def sum(a,b):
	print(a+b)
sum(10,20)
sum(30,40)

