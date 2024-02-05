import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename

try:
    book = askopenfilename()

    if book:
        with open(book, 'rb') as file:
            pdfreader = PdfReader(file)
            pages = len(pdfreader.pages)

            for num in range(pages):
                page = pdfreader.pages[num]
                text = page.extract_text()
                player = pyttsx3.init()
                player.say(text)
                player.runAndWait()

    else:
        print("File selection canceled.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
