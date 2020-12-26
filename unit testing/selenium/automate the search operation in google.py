from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path='E:\library\chromedriver.exe')
driver.get('https://www.google.com/')
driver.maximize_window()
driver.find_element_by_name('q').send_keys('mahesh babu')
time.sleep(5)
driver.find_element_by_name('btnK').click()
driver.find_element_by_class_name('LC20lb').click()
time.sleep(10)
driver.close()