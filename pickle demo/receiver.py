import pickle
with open('abc.dat','rb') as f:
	while True:
		try:
			newobj=pickle.load(f)
			newobj.display()
		except EOFError:
			print('all employee completed')
			break