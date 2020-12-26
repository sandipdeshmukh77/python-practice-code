from selenium import webdriver
import unittest
import time
class googleDemo(unittest.TestCase):
	def setUp(self):
		global driver
		driver=webdriver.Chrome('E:\library\chromedriver.exe')
		driver.get('https://www.google.com')
		time.sleep(5)
		driver.maximize_window()
	def test(self):
		driver.find_element_by_name('q').send_keys('ratan tata')
		time.sleep(5)
		driver.find_element_by_name('btnK').click()
		time.sleep(5)
		driver.find_element_by_class_name('LC20lb ').click()
		time.sleep(5)
	def tearDown(self):
		driver.close()
		

unittest.main()
