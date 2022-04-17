# Tests to ensure hover part descriptions are fully functional
from python_files import hover

""" Test 1 - Test mouse hover over qualified parts registers """
# "test_" must be included for pytest to recognize it as a test case
def test_hoverEnter() -> None:
    # test CPU
    assert hover.hoverEnter("CPU", "mock_label") == "CPU stands for Central Processing Unit. The CPU is the BRAIN of the computer, containing all the circuitry needed to process input, store data, and output results."
    # test GPU
    assert hover.hoverEnter("GPU", "mock_label") == "GPU stands for Graphics Processing Unit (Graphics Card. The GPU is a specialized electronic circuit that accelerates the creation and rendering of images, video, and animation."
    # test CPU-cooler
    assert hover.hoverEnter("CPU-COOLER", "mock_label") == "CPU cooler removes the heat produced from the cpu to keep it from overheating and becoming damaged."
    # test Antenna
    assert hover.hoverEnter("ANTENNA", "mock_label") == "These are antenna ports for wifi"
    # test USB3.2_PS2
    assert hover.hoverEnter("USB3.2_PS2", "mock_label") == "This is a port for USB3.2 and PS/2"
    # test LAN_USB2.0
    assert hover.hoverEnter("LAN_USB2.0", "mock_label") == "This is a port for LAN or local area network ethernet and USB2.0"
    # test PCIe_x1
    assert hover.hoverEnter("PCIe_x1", "mock_label") == "PCIe x1 is a slot for low demanding PCIe expansion card"
    # test PCIe_x16
    assert hover.hoverEnter("PCIe_x16", "mock_label") == "PCIe x16 is a slot for expansion card with high bandwith requirements like graphics card"


""" Test 2 - Test that when mouse doesn't hover, default desc. is displayed """
# "test_" must be included for pytest to recognize it as a test case
def test_hoverExit() -> None:
    assert hover.hoverExit("N/A", "mock_label") == "Hover over a part to see description!\nRight click to analyze a part!"

