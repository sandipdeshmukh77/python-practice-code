from pyaml import yaml
edict={'en0':100,'ename':'sandi','esal':10000,'ismarried':None,'isempo':False}
#serialization to string
y=yaml.dump(edict)
print(y)
#print(type(y))
#deserialization from string

l=yaml.safe_load(y)
print(l)
#print(type(l))

#serialization to file
with open('abc.yaml','w') as f:
	yaml.dump(edict,f)
#deserialization from file
with open('abc.yaml','r') as f:
	a=yaml.safe_load(f)
	print(a)


