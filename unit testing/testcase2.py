import unittest
class TestCase2(unittest.TestCase):
	def setUp(self):
		print('setup method execution')
	def test2(self):
		print('test2 method execution')
	def tearDown(self):
		print('teardown method execution')