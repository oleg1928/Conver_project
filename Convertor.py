# Initiating
from docx2pdf import convert
import os.path
from lxml import etree
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import letter

# It will ask you what type do you want to convert it to (e.g. fb2, pdf, doc)
# It is going to ask you whether you want to convert the whole folder or just a single file
# It is going to ask you which file do you want to convert
# Where do you want the converted file to go? (Desktop?)
# Implement try except in the code

class Start:

    def Starter(self):
        """
        Function with the main loop

        """
        while True:
            print("What file do you want to convert?")
            print("Write name with file extension.")
            file_name = input()
            path = FileManager().find_file(file_name, "D:/")
            if path == "":
                path = FileManager().find_file(file_name, "C:/")
            print(path)
            print("What type of file do you want to convert it to?")
            print("fb2, pdf, doc, docx")
            type_ans = input()
            if type_ans in ["fb2", "pdf", "doc", "docx", "epub"]:
                # From docx to pdf
                if file_name[-4:] == "docx":
                    if type_ans == "pdf":
                        # you need internet for the convert function to work
                        convert("C:/Users/Admin/OneDrive/Desktop/Test.docx", "C:/Users/Admin/OneDrive/Desktop/Test.pdf")
                        break

                # From fb2 to pdf
                if file_name[-3:] == "fb2":
                    if type_ans == "pdf":
                        ConvertManager().fb2_to_pdf(path, f"C:/Users/Admin/OneDrive/Desktop/{file_name}.pdf") # desktop debugging
                        break
                # From pdf to docx
                if file_name[-3:] == "pdf":
                    if type_ans == "docx":
                        raise NotImplementedError()
                        break
                # from doc to pdf
                if file_name[-3:] == "doc":
                    if type_ans == "pdf":
                        raise NotImplementedError()
                        break
                # from epub to pdf
                if file_name[-4:] == "epub":
                    if type_ans == "pdf":

                        break


            else:
                print("Please try again")





class FileManager:

    def find_file(self, filename, search_path):
        """
        Finds the path to the file
        :param filename: Name of file you want to find
        :param search_path: Where do you want to start the search
        :return: The path of file on the computer
        """
        result = ""
        for path, folders, files in os.walk(search_path):
            if filename in files:
                result = os.path.join(path, filename)
        result = result.split("\\")
        return "/".join(result)





class ConvertManager:
    def docx_to_pdf(self,filepath):
        """
        Converts docx extension into pdf extension
        :param filepath: the path to the file
        """

        convert(filepath, "C:/Users/Admin/OneDrive/Desktop") # can go to desktop for debugging


    def fb2_to_pdf(self,fb2_path, pdf_path):
        """
        Converts the fb2 files into pdf
        :param fb2_path: path to the fb2 file
        :param pdf_path: where the converted
                pdf file is going to go
        """
        tree = etree.parse(fb2_path)
        root = tree.getroot()

        # Create a PDF document
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)
        story = []

        # Extract text from the FB2 file
        text_elements = root.xpath('//*[local-name()="p"]')

        styles = getSampleStyleSheet()
        normal_style = styles['Normal']

        for element in text_elements:
            text = element.text
            if text:
                paragraph = Paragraph(text, normal_style)
                story.append(paragraph)

        doc.build(story)



srt = Start()
srt.Starter()