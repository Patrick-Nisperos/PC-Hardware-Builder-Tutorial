# file containing hover descriptions

def hoverEnter(label, description_label):
    if (label == "cpu"):
        description_label.setText("CPU stands for Central Processing Unit. The CPU is the BRAIN of the computer, containing all the circuitry needed to process input, store data, and output results.")
    if (label == "gpu"):
        description_label.setText("GPU stands for Graphics Processing Unit (Graphics Card). The GPU is a specialized electronic circuit that accelerates the creation and rendering of images, video, and animation.")
    if (label == "ram"):
        description_label.setText("RAM stands for Random Access Memory. The RAM is short term memory where data is stored as the processor needs it.")
    if (label == "cpu cooler"):
        description_label.setText("CPU cooler removes the heat produced from the cpu to keep it from overheating and becoming damaged.")
    if (label == "ssd"):
        description_label.setText("SSD stands for Solid-State Drive. M.2 is a form factor for ssds. Similiar to a Hard drive, an ssd stores data even when the pc is off. However it uses flash memory and is much faster.")
    if (label == "ANTENNA"):
        description_label.setText("These are antenna ports for wifi")
    if (label == "HDMI"):
        description_label.setText("This is the port for HDMI connection")
    if (label == "USB3.2_PS2"):
        description_label.setText("This is the port for USB3.2 and PS/2")
    if (label == "USB3.2_TypeA_TypeC"):
        description_label.setText("This is the port for USB3.2 type-A and USB3.2 type-C")
    if (label == "LAN_USB2.0"):
        description_label.setText("This is the port for LAN or local area network ethernet and USB2.0")
    if (label == "AUDIO-JACKS"):
        description_label.setText("This is the port for audio jacks for sound and mic")

def hoverExit(label, description_label):
    description_label.setText("Hover over a part to see description!\nRight click to analyze a part!")