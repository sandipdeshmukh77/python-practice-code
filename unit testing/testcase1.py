import unittest
class TestCase1(unittest.TestCase):
	def setUp(self):
		print('setup method execution')
	def test1(self):
		print('test1 method execution')
	def tearDown(self):
		print('teardown method execution')