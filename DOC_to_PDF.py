from docx2pdf import convert
import os.path
# It will ask you what type do you want to convert it to (e.g. fb2, pdf, doc)
# It is going to ask you whether you want to convert the whole folder or just a single file
# It is going to ask you which file do you want to convert
# Where do you want the converted file to go? (Desktop?)
class Start:
    def __init__(self):
        print("H")

    def Starter(self):
        while True:
            print("What type of file do you want to convert it to?")
            print("fb2, pdf, doc, docx")
            type_ans = input()
            if type_ans not in ["fb2", "pdf", "doc", "docx"]:
                    print("Please try again")
            else:
                break



class FileManager:
    def __init__(self, filename, search_path):
        self.filename = filename
        self.search_path = search_path


    def find_file(self, filename, search_path):
        result = []
        for path, folders, files in os.walk(search_path):
            if filename in files:
                result.append(os.path.join(path, filename))
        return result





class ConvertManager:
    def __init__(self):
        raise NotImplementedError()

    # convert("C:/Users/Admin/OneDrive/Desktop/Test.docx", "C:/Users/Admin/OneDrive/Desktop/Test_pdf.pdf")


if __name__ == "__main__":
    srt = Start()
    srt.Starter()