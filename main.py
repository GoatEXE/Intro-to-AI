
###############
#Imports
###############


from Classes.PDF_Extractor import Extractor
from Classes.OllamaAI import AI


###############
#Variables
###############


#TODO: Have this generated by AI
unwanted = [
    "Discount Mufflers",
    "Prepared by AI on 05/14/2024", 
    "Customer List",
]


#############
#Objects
#############


extractor = Extractor(
    target_document="Source-Documents/discountmufflers.pdf",
    unwanted_text=unwanted,
    delimiter=None,
    )

ai = AI()


#############
#Main Body
#############


extractor.extract_text()

for line in extractor.lines:
    ai.arrange_line(line)
    break