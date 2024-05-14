from pypdf import PdfReader


class Extractor():


    def __init__(self, target_document, delimiter):
        """
        Target_Document needs to contain a fully qualified path, name, and file type.
        Delimiter is a string object type that commonly separates each unique data entry.
        """
        #Arguments
        self.target_document = target_document
        self.delimiter = delimiter

        #Initialization References
        self.file_name = self.target_document.split('.')[0]
        self.pdf = PdfReader(self.target_document)
        self.number_of_pages = len(self.pdf.pages)
        self.lines = None
        

    def extract_text(self):
        with open("Logging/Non-Final/base_text.txt", "w") as f:
            for n in range(self.number_of_pages):
                text = self.pdf.pages[n].extract_text()
                f.write(text)
