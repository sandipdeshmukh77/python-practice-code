from threading import *
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
t1=Thread(target=double,args=(n,))
t2=Thread(target=square,args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()
end_time=time.time()
print('the total time is',end_time-start_time)
