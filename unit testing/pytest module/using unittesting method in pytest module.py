import pytest
@pytest.fixture
def setUp():
	print('setup method execution')
def test_case1(setUp):
	print('execution of test method 1')
def test_case2(setUp):
	print('execution of test method 2')
