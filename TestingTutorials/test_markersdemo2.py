import pytest
import sys


@pytest.mark.skip   # inbuilt marker skip to skip this test function
def test_login():
    print("Login done")


@pytest.mark.skipif(sys.version_info < (3, 12), reason="Python version not supported")
def test_addProducts():
    print("added products")


@pytest.mark.xfail
def test_logout():
    assert True
    print("Logout done")
