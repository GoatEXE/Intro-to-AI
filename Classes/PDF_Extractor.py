from pypdf import PdfReader
import os


class Extractor():


    def __init__(self, target_document, **kwargs):
        """
        Target_Document needs to contain a fully qualified path, name, and file type.
        Delimiter is a string object type that commonly separates each unique data entry.
        """
        #TODO: Have AI find strings of text that aren't needed for the data plots

        #Arguments
        self.target_document = target_document
        self.delimiter = kwargs.get("delimiter", None)
        self.unwanted_text = kwargs.get("unwanted_text", None)

        #Initialization References
        self.file_name = os.path.splitext(os.path.basename(target_document))[0]
        self.pdf = PdfReader(self.target_document)
        self.number_of_pages = len(self.pdf.pages)
        self.lines = None
        

    def extract_text(self):
        """
        Extract the text from the class's targeted .pdf document.
        Loops through each page to find every unwanted phrase and removes it from that page.
        Creates a text file in the Logging/Non-Final directory of the total extracted text.
        Calls self.read_lines to set self.lines to be the filtered .pdf data.
        """
        #TODO: Test with multipage document
        with open("Logging/Non-Final/base_text.txt", "w", encoding="utf-8") as f:
            for n in range(self.number_of_pages):
                text = self.pdf.pages[n].extract_text()

                if self.unwanted_text:
                    for phrase in self.unwanted_text:
                        if phrase in text:
                            #Remove the instance of an unwanted phrase from the current page
                            first_half, second_half = map(str.strip, text.split(phrase, 1))
                            text = first_half + second_half
                         

                f.write(text)

        self.read_lines()

    
    def read_lines(self):
        """
        Set self.lines to be the filtered data of the self.extract_text method.
        """
        with open("Logging/Non-Final/base_text.txt", "r", encoding="utf-8") as f:
            self.lines = f.readlines()
