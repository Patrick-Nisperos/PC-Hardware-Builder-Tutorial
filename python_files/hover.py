# file containing hover descriptions

def hoverEnter(label, description_label):
    text = ""
    if (label == "CPU"):
        text = "CPU stands for Central Processing Unit. The CPU is the BRAIN of the computer, containing all the circuitry needed to process input, store data, and output results."
    if (label == "CPU-CABLE"):
        text = "CPU cable is a power source for the CPU"
    if (label == "GPU"):
        text = "GPU stands for Graphics Processing Unit (Graphics Card. The GPU is a specialized electronic circuit that accelerates the creation and rendering of images, video, and animation."
    if (label == "RAM"):
        text = "RAM stands for Random Access Memory. The RAM is short term memory where data is stored as the processor needs it."
    if (label == "CPU-COOLER"):
        text = "CPU cooler removes the heat produced from the cpu to keep it from overheating and becoming damaged."
    if (label == "SSD"):
        text = "SSD stands for Solid-State Drive. M.2 is a form factor for SSDs. Similiar to a Hard drive, an SSD stores data even when the pc is off. However it uses flash memory and is much faster."
    if (label == "ANTENNA"):
        text = "These are antenna ports for wifi"
    if (label == "HDMI"):
        text = "This is a port for HDMI connection"
    if (label == "USB3.2_PS2"):
        text = "This is a port for USB3.2 and PS/2"
    if (label == "USB3.2_TypeA_TypeC"):
        text = "This is a port for USB3.2 type-A and USB3.2 type-C"
    if (label == "LAN_USB2.0"):
        text = "This is a port for LAN or local area network ethernet and USB2.0"
    if (label == "AUDIO-JACKS"):
        text = "This is a port for audio jacks for sound and mic"
    if (label == "PCIe_x1"):
        text = "PCIe x1 is a slot for low demanding PCIe expansion card"
    if (label == "CMOS"):
        text = "CMOS battery powers BIOS firmware"
    if (label == "PCIe_x16"):
        text = "PCIe x16 is a slot for expansion card with high bandwith requirements like graphics card"
    if (label == "RAM Slot"):
        text = "These are slots for RAM sticks" 
    try:
        description_label.setText(text)
    except:
        print("description label does not exist")
    if (description_label == "testing"):
        return text # for test cases

def hoverExit(label, description_label):
    text = "Hover over a part to see description!\nRight click to analyze a part!"
    try:
        description_label.setText(text)
    except:
        print("description label does not exist")
    if (description_label == "testing"):
        return text # for test cases