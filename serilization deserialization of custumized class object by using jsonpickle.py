import jsonpickle
class employee:
	def __init__(self,eno,ename,esal,eaddr):
		self.eno=eno
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr
	def display(self):
		print('ENO:{},ENAME:{},ESAL:{},EADDR:{}'.format(self.eno,self.ename,self.esal,self.eaddr))
#serialization to string
e=employee(100,'sandi',20000,'pune')
json_string=jsonpickle.encode(e)
print(json_string)

#serialization to file
with open('eemp.json','w') as f:
	f.write(json_string)
#deserialization from string
e=jsonpickle.decode(json_string)
#print(type(e))
e.display()
#deserialization from file
with open('eemp.json','r') as f:
	a=f.readline()
	e2=jsonpickle.decode(a)
	#print(type(e2))
e2.display()



