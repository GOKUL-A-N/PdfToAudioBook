# this program conerts a pdf file to audio file


# importing the python libraries
import pyttsx3
import pdfplumber
import PyPDF2

# get the file name and the location of the pdf file
file = 'gokul.pdf'

pdfFileObj = open(file, 'rb')

#create a PDF file reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)


# get the number of pages
pages = len(pdfReader.pages)

# create a pdf plumber object and leap through the number of pages in pdf file
with pdfplumber.open(file) as pdf:

    speaker = pyttsx3.init();

    text = ""

    for i in range(0 , pages):
        page = pdf.pages[i]
        text += page.extract_text()
        print(text)
        
        # speaker.say(text)
        # speaker.runAndWait()
        # speaker.stop()
    
    speaker.save_to_file(text,'audio.mp3')
    speaker.runAndWait()