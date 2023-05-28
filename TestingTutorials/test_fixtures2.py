import pytest

# here first lines are repeating multiple times
# so we will create fixtures for this here


@pytest.fixture
def setup():
    print("Start the browser")
    yield
    print("Close the browser")


def test_1(setup):
    print("Test 1 executed")


def test_2(setup):
    print("Test 2 executed")


def test_3(setup):
    print("Test 3 executed")


# note: If you don't see the close the browser line which is after yield in the test results. use -s flag
# pytest .\test_fixtures2.py -s
