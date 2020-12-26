import json
class employee:
	def __init__(self,eno,ename,esal,eaddr):
		self.eno=eno
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr
	def display(self):
		print('ENO:{},ENAME:{},ESAL:{},EADDR:{}'.format(self.eno,self.ename,self.esal,self.eaddr))
e=employee(100,'sandi',20000,'pune')
edict=e.__dict__
with open('emp.json','w') as f:
	json.dump(edict,f,indent=4)
with open('emp.json','r') as f:
	edicts=json.load(f)
	newemp=employee(edicts['eno'],edicts['ename'],edicts['esal'],edicts['eaddr'])
newemp.display()

