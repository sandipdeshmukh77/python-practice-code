s=input('enter any string:-')
if s.isalnum():
	print('it is alphanumeric character')
	if s.isalpha():
		print('it is alphabate character')
		if s.islower():
			print('lowercase alphabet character')
		elif s.isupper():
			print('uppercase alphabet character')
	else:
		print('it is a digit')
elif s.isspace():
	print('it is space charater')
else:
	print('non space special character')