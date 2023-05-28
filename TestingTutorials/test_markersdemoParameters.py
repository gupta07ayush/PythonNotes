import pytest
import sys

# Suppose you have a condition or a test which you want to run multiple times with different set of data.
# In that case you can pass parameters as list of tuples and each tuple is nothing but a saperate record


@pytest.mark.parametrize('username,password', [('selenium', 'WebDriver'), ("Python", "Pytest"), ("Ayush", 'Gupta')])
def test_login(username, password):
    # I want to login with ten different users.
    print(username)
    print(password)
