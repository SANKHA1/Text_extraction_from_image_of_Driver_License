from pytesseract import pytesseract


class OCR:
    def __init__(self):
        self.path = r"E:\Pycharm Projects\Img_to_text\Tesseract\tesseract.exe" #change this if Tesseract is installed in another path.Mention the path of 'tesseract.exe' here.

    def extract(self,filename):

        try:
            pytesseract.tesseract_cmd = self.path
            text = pytesseract.image_to_string(filename)
            return text

        except Exception as e:
            print(e)
            return "Error"

if __name__ == "__main__":
    obj = OCR()
    image_name = input("Enter your image name: ")
    text = obj.extract(image_name)
    print("Your extracted text: \n\n", text)
