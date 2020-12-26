import time
def countdown(num):
	print('countdown starts')
	while num>0:
		yield num
		
		num=num-1
value=countdown(10)
for x in value:
	print(x)
	time.sleep(1)
print('Launch Started...')	
