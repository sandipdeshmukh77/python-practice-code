import os
fname=input('enter the name of file:')
if os.path.isfile(fname):
	print('this file is available',fname)
	print('the content of this file is:')
	f=open(fname,'r+')
	print('*'*40)
	print(f.read())
	print('*'*40)
	f.close()
else:
	print("this file does not exist",fname)
