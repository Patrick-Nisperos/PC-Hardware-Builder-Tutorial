import main

# "test_" must be included for pytest to recognize it as a test case
def test_multiply() -> None:
    assert main.multiply(3, 4) == 12 # should pass
    assert main.multiply(4, 4) == 16 # should pass