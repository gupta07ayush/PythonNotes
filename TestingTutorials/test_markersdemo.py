# In order to use markers we need to import pytest and then you can decorators
import pytest


@pytest.mark.smoke   # created custom marker smoke
def test_login():
    print("Login done")


@pytest.mark.regression   # created custom marker smoke
def test_addProducts():
    print("added products")


@pytest.mark.smoke   # created custom marker smoke
def test_logout():
    print("Logout done")

 # To run the marker
 # pytest test_markersdemo.py -m markername
