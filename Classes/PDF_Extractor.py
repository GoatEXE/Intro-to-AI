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
        self.delimiter = kwargs.get("delimiter", str())
        self.unwanted_text = kwargs.get("unwanted_text", list())
        self.page_identifier = kwargs.get("page_identifier", False)
        self.page_minimum = kwargs.get("page_minimum", int())
        self.page_maximum = kwargs.get("page_maximum", int())

        #Initialization References
        self.file_name = os.path.splitext(os.path.basename(target_document))[0]
        self.pdf = PdfReader(self.target_document)
        self.number_of_pages = len(self.pdf.pages)
        self.lines = None

        #Initialization Function
        if self.page_identifier:
            for n in range(self.page_minimum, self.page_maximum+1):
                self.unwanted_text.append(f"Page {n}")
        

    def extract_text(self):
        """
        Extract the text from the class's targeted .pdf document.
        Loops through each page to find every unwanted phrase and removes it from that page.
        Creates a text file in the Logging/Non-Final directory of the total extracted text.
        Calls self.read_lines to set self.lines to be the filtered .pdf data.
        """
        with open("Logging/Non-Final/base_text.txt", "w", encoding="utf-8") as f:
            #for n in range(self.number_of_pages):
            for n in range(2):
                text = self.pdf.pages[n].extract_text().strip("\n")
                print(text)
                page = ""


                if self.unwanted_text:
                    for phrase in self.unwanted_text:
                        while phrase in text:
                            #Remove the instance of an unwanted phrase from the current page
                            first_half, second_half = map(str.strip, text.split(phrase, 1))
                            text = first_half + second_half


                if self.delimiter:
                    self.separate()
                    # split_list = text.split(self.delimiter)
                    
                    # for item in split_list:
                    #     page += f"{item}"

                    # text = page.strip()
                        

                f.write(f"{text}\n")

        self.read_lines()

    
    def separate(self):
        self.read_lines()
        current_object = []
        all_objects = []

        for line in self.lines:
            if line.startswith(self.delimiter):
                all_objects.append(current_object)
                current_object = []
                
            elif line not in current_object:
                line.append(current_object)
            



    def read_lines(self):
        """
        Set self.lines to be the filtered data of the self.extract_text method.
        """
        with open("Logging/Non-Final/base_text.txt", "r", encoding="utf-8") as f:
            self.lines = f.readlines()
