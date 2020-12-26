import pickle
class employee:
	def __init__(self,eno,ename,esal,eaddr):
		self.eno=eno
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr
	def display(self):
		print('ENO:{},ENAME:{},ESAL:{},EADDR:{}'.format(self.eno,self.ename,self.esal,self.eaddr))
e=employee(100,'sandi',20000,'pune')
with open('emp.dat','wb') as f:
	pickle.dump(e,f)
	print('serialization done succefully')
with open ('emp.dat','rb') as f:
	obj=pickle.load(f)
	print('deserialization done succefully')
obj.display()	
