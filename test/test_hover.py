# Tests to ensure hover part descriptions are fully functional
from python_files import hover

""" Test 1 - Test mouse hover over qualified parts registers """
# "test_" must be included for pytest to recognize it as a test case
def test_hoverEnter() -> None:
    # test CPU
    assert hover.hoverEnter("CPU", "mock_label") == "CPU stands for Central Processing Unit. The CPU is the BRAIN of the computer, containing all the circuitry needed to process input, store data, and output results."



""" Test 2 - Test that when mouse doesn't hover, default desc. is displayed """
# "test_" must be included for pytest to recognize it as a test case


