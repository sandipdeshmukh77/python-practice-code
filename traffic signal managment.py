from threading import *
import time
e=Event()
def trafficpolice():
	while True:
		time.sleep(10)
		print('traffic police is giving green signal people can go now')
		e.set()
		time.sleep(20)
		print('traffic police is giving RED signal stop the vehicles')
		e.clear()
def driver():
	n=1
	while True:
		print('drivers are waiting on signal')
		e.wait()
		
		while e.isSet()==True:
			print('passenger',n,'crossing the road')
			time.sleep(2)
			n=n+1
t1=Thread(target=trafficpolice)
t2=Thread(target=driver)
t1.start()
t2.start()

		
