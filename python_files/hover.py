# file containing hover descriptions
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt
import PartAnalyzer as Analyzer
import Labels

def hoverEnter(drop, description_label):
    text = ""
    i = 0
    for names in Analyzer.partNames:
        if(drop.name == names):
            text = Analyzer.shortDescriptions[i]
        i += 1

    try:
        description_label.setText(text)
    except:
        print("Description not found")

    if isinstance(drop, Labels.DragLabel):
        drop.highlighteffect.setEnabled(True)

    #Test case
    if(description_label == "testing"):
        return text


def hoverExit(drop, description_label):
    text = "Hover over a part to see description!\nRight click to analyze a part!"
    
    if isinstance(drop, Labels.DragLabel):
        drop.highlighteffect.setEnabled(False)

    try:
        description_label.setText(text)
    except:
        print("description label does not exist")
    if (description_label == "testing"):
        return text # for test cases