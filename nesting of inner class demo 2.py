class person:
	def __init__(self,name,dd,mm,yyyy):
		print('creation of person class')
		self.name=name
		self.dob=self.dob(dd,mm,yyyy)
	def info(self):
		print('name',self.name)
		self.dob.display()
	class dob:
		def __init__(self,dd,mm,yyyy):
			print('creation of dob class')
			self.dd=dd
			self.mm=mm
			self.yyyy=yyyy
		def display(self):
			print('{}/{}/{}'.format(self.dd,self.mm,self.yyyy))

p=person('sandip',24,11,1993)
p.info()