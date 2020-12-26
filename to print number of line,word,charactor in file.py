import os
fname=input('enter file name:')
if os.path.isfile(fname):
	print('file exist',fname)
	f=open(fname,'r')
	lcount=wcount=ccount=0
	for line in f:
		lcount=lcount+1
		no_of_word=len(line.split())
		wcount=wcount+no_of_word
		no_of_charactor=len(line)
		ccount=ccount+no_of_charactor
	print('the number of line',lcount)
	print('the number of word',wcount)
	print('the number of charactor',ccount)
else:
	print('{} file does not exist'.format(fname))