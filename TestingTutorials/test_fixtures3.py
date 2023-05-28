import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# here first lines are repeating multiple times
# so we will create fixtures for this here


driver = None


@pytest.fixture
def setup():
    print("Start the browser")
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()
    print("Close the browser")


def test_1(setup):
    driver.get('https://google.com')
    print("Test 1 executed")


def test_2(setup):
    driver.get('https://github.com/gupta07ayush')
    print("Test 2 executed")


def test_3(setup):
    driver.get('https://youtube.com')
    print("Test 3 executed")


# note: If you don't see the close the browser line which is after yield in the test results. use -s flag
# pytest .\test_fixtures2.py -s


# pip install pytest-xdist
# speedup tests by sending tests to multiple CPU
# pytest -n NoOfCPU
