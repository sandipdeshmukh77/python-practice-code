class outer:
	def __init__(self):
		print('creating outer class object')
	class inner:
		def __init__(self):
			print('creating inner class object')
		class innerinner:
			def __init__(self):
				print('creating innerinner class')
			def m1(self):
				print('innerinner class method')
#o=outer()
#i=o.inner()
#ii=i.innerinner()
#ii.m1()   Other method to call m1()
outer().inner().innerinner().m1()

				