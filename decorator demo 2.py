def decor(func):
	def inner(name):
		if name=='pradip':
			print('Bad Morning',name)
		else:
			func(name)
		
	return inner
		
@decor
def wish(name):
	print('Good Morning',name)
wish('sandip')
wish('pradip')
wish('rushi')

