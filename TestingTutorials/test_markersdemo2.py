import pytest


@pytest.mark.skip   # inbuilt marker skip to skip this test function
def test_login():
    print("Login done")


def test_addProducts():
    print("added products")


def test_logout():
    print("Logout done")
