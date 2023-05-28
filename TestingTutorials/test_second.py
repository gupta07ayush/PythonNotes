# pytest will run all files from current dir/ subdirectory.
# pytest test_second.py -This will run only specified file

def test_login():
    print("Login to application")


def test_checkout():
    print("Checkout")


def test_logout():
    print("Log out from the application")


# Note 1: This will run only first function of the this file.
# pytest test_second.py -k login


# Note 2: v=verbose -It will show you some more details
# pytest -rA -v
