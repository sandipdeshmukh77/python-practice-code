import os
w=os.walk('python tutorials')
for x,y,z in w:
	print('directory name:',x)
	print('name of sub directory:',y)
	print('list of files:',z)
	print()
