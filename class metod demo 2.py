class test:
	count=0
	def __init__(self):
		test.count=test.count+1
	@classmethod
	def no_of_object(cls):
		print('the number of object created is',cls.count)
test.no_of_object()
t=test()
t=test()
t=test()
t=test()
test.no_of_object()
