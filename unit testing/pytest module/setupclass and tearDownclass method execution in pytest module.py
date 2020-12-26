import pytest
@pytest.yield_fixture(scope='module')#because of scope='module' it will execute like setupclass and tearDownclass method
def setUptearDownClass():
	print('setup method execution')
	yield # this word is responsible for setup and tearDown method
	print('tearDown activity')
def test_case1(setUptearDownClass):
	print('execution of test method 1')
def test_case2(setUptearDownClass):
	print('execution of test method 2')
