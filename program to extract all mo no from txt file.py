import re
f1=open('input.txt','r')
f2=open('output.txt','w')
for line in f1:
	l=re.findall('[6-9]\d{9}',line)
	for n in l:
		f2.write(n+'\n')
print('all no. extracted successfully')
f1.close
f2.close
