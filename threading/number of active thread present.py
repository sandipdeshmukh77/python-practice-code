from threading import *
import time
def test():
	print(current_thread().name,'starts...')
	time.sleep(3)
	print(current_thread().name,'ends...')
print('the number of active threads',active_count())
t1=Thread(target=test,name='child class 1')
t2=Thread(target=test,name='child class 2')
t3=Thread(target=test,name='child class 3')
t1.start()
t2.start()
t3.start()
print('the number of active threads',active_count())
time.sleep(3)
print('the number of active threads',active_count())
