# file containing hover descriptions
import PartAnalyzer as Analyzer

def hoverEnter(label, description_label):
    text = ""
    i = 0
    for names in Analyzer.partNames:
        if(label == names):
            text = Analyzer.shortDescriptions[i]
        i += 1

    try:
        description_label.setText(text)
    except:
        print("Description not found")

    #Test case
    if(description_label == "testing"):
        return text


def hoverExit(label, description_label):
    text = "Hover over a part to see description!\nRight click to analyze a part!"
    try:
        description_label.setText(text)
    except:
        print("description label does not exist")
    if (description_label == "testing"):
        return text # for test cases