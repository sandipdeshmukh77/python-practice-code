class bird:
	wings=2
	@classmethod
	def fly(cls,name):
		print('{} flies with {} wings'.format(name,cls.wings))
bird.fly('eagle')
bird.fly('parrot')