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


# Built-in markers
# By using pytest.mark helper you can easily set metadata on your test functions.
# You can find the full list of builtin markers in the API reference. Or
# You can list all the markers, including builtin and custom, using the CLI- pytest --markers

# 1. usefixtures - use fixtures on a test function or class
# 2. filterwarnings - filter certain warnings of a test function
# 3. skip - always skip a test function
# 4. skipif - skip a test function if a certain condition is met
# 5. xfail - produce an “expected failure” outcome if a certain condition is met
# 6. parametrize - perform multiple calls to the same test function.

"""
Registering marks

You can register custom marks in your pytest.ini file like this:

[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    serial
or in your pyproject.toml file like this:

[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "serial",
"""