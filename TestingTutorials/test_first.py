# rule no 1: test file name-
# test_fileNameWhichYouWantToTest.py
# function name will start from the word 'test'.

def test_1():
    x = 10
    y = 20

    assert x == y

# this test will fail because here x is not equal to y.
# to run the test simply write pytest in the terminal.


def test_2():
    # I am writing another test.
    x = 5
    y = 5

    assert x == y
# this test will pass because 5=5
# fail = F
# pass = . (green dot)
