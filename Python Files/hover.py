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

def hoverExit(label, description_label):
    description_label.setText("Hover over a part to see description!          Right click to analyze a part!")