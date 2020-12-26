import time
def double(n):
	for i in n:
		time.sleep(1)
		print(i*2)
def square(n):
	for i in n:
		time.sleep(1)
		print(i*i)
n=[1,2,3,4,5]
start_time=time.time()
double(n)
square(n)
end_time=time.time()
print('the total time is',end_time-start_time)

