
class employee:
	def __init__(self,eno,ename,esal,eaddr):
		self.eno=eno
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr
	def display(self):
		print('ENO:{},ENAME:{},ESAL:{},EADDR:{}'.format(self.eno,self.ename,self.esal,self.eaddr))
