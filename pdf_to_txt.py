from PyPDF2 import PdfFileReader
from nonfunctional import ( 
    SHOW_MESSAGE, open_file_dialogue,
    confirm_action
)
import sys, os, random

_filename = confirm_action()

def get_pdf_content_lines(pdf_file_path):
    data = []
    try:
        with open(pdf_file_path, 'rb') as f:
            pdf_reader = PdfFileReader(f)
            for page in pdf_reader.pages: 
                for line in page.extractText().splitlines():
                    data.append(str(line))    
    except:
        SHOW_MESSAGE("PDF File Not Found", flag='error')
        return
    return data
    
_file_name = str(_filename)
try:
    real_name = _file_name.split('/')[-1]
    head, part, tail = real_name.partition('.')
    real_name = head + '.txt'
except:
    real_name = str(f"output_{random.randint(100, 10000).txt}")
try:
    with open(real_name, 'w') as writer:
        writer.writelines(get_pdf_content_lines(_filename))
    SHOW_MESSAGE(f"Data written to txt file named {real_name}.")
except:
    SHOW_MESSAGE("Can't create a new file to save data. Try Again.", "error")