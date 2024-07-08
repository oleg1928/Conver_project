from docx2pdf import convert
import os.path
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
            print("What type of file do you want to convert it to?")
            print("fb2, pdf, doc, docx")
            type_ans = input()
            if type_ans in ["fb2", "pdf", "doc", "docx"]:
                # From docx to pdf
                if file_name[-4:] == "docx":
                    if type_ans == "pdf":
                        # you need internet for the convert function to work
                        convert("C:/Users/Admin/OneDrive/Desktop/Test.docx", "C:/Users/Admin/OneDrive/Desktop/Test.pdf")
                        break

                # From fb2 to
                if file_name[-3:] == "fb2":
                    if type_ans == "pdf":
                        raise NotImplementedError()
                        break
                # From docx to pdf
                if type_ans == "docx":
                    if file_name[-3:] == "pdf":
                        raise NotImplementedError()
                        break
                # from doc to
                if file_name[-3:] == "doc" and type_ans:
                    raise NotImplementedError()
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
        convert(filepath, "C:/")

srt = Start()
srt.Starter()