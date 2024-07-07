from docx2pdf import convert
# It will ask you what type do you want to convert it to (e.g. fb2, pdf, doc)
# It is going to ask you whether you want to convert the whole folder or just a single file
# It is going to ask you which file do you want to convert
# Where do you want the converted file to go? (Desktop?)
class Start:
    type_ans = input()
    print("What type of file do you want to convert it to?")
    print("fb2, pdf, doc, docx")
    for i in type_ans:
        if i  not in ["fb2", "pdf", "doc", "docx"]:
            print("Please try again")

class FileManager:
    pass





class ConvertManager:

    convert("C:/Users/Admin/OneDrive/Desktop/Test.docx", "C:/Users/Admin/OneDrive/Desktop/Test_pdf.pdf")


if __name__ == "__main__":
    ConvertManager()