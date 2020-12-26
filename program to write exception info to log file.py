import logging
logging.basicConfig(filename='record.log',level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(msg)s',datefmt='%d/%m/%Y %I:%M:%S %p')
logging.info('A new request came')
try:
	a=int(input('enter first number'))
	b=int(input('enter sencond number'))
	print(a/b)
except ZeroDivisionError as msg:
	print("can't divide with zero")
	logging.exception(msg)
except ValueError as msg:
	print('please enter int value only')
	logging.exception(msg)
logging.info('request proceesing completed')
	