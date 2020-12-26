import pytest
@pytest.yield_fixture(scope='module')
def setUptearDownClass():
	print('setupclass execution')
	yield
	print('teardownclass execution')

@pytest.yield_fixture()
def setUptearDown():
	print('setup execution')
	yield
	print('teardown execution')
