import main

# "test_" must be included for pytest to recognize it as a test case
def test_add():
    assert main.add(3, 4) == 7 # should pass
    assert main.add(4, 4) == 7 # should fail
    