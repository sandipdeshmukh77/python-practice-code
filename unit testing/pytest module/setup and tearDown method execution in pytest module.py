import pytest
@pytest.yield_fixture
def setUptearDown():
	print('setup method execution')
	yield # this word is responsible for setup and tearDown method
	print('tearDown activity')
def test_case1(setUptearDown):
	print('execution of test method 1')
def test_case2(setUptearDown):
	print('execution of test method 2')
