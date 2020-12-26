from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
class googleDemo(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		global driver
		driver=webdriver.Chrome('E:\library\chromedriver.exe')
		driver.get('http://www.seleniumbymahesh.com/')
		time.sleep(5)
		driver.maximize_window()
		time.sleep(3)
	def test(self):
		driver.find_element(By.LINK_TEXT,'HMS').click()
		time.sleep(5)
		driver.find_element(By.NAME,'username').send_keys('admin')
		driver.find_element(By.NAME,'password').send_keys('admin')
		driver.find_element(By.NAME,'submit').click()
		time.sleep(10)
	def test_1(self):
		driver.find_element(By.LINK_TEXT,'Logout')
	@classmethod
	def tearDownClass(cls):
		driver.close()


unittest.main()

	

		