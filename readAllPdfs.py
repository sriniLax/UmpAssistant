# Load data and partition the pdfs into text, tables, and images
from typing import Any
import os
from unstructured.partition.pdf import partition_pdf
import pytesseract
#import PyPDF2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# from pdf2image import convert_from_path

# poppler_path = r"C:\Users\Ramakrishna\Documents\WorkFolder\ProgramPractice\python\Packages\Poppler\poppler-24.08.0\Library\bin"  # Replace with the actual path

# Get all pdf files -- restricted to the Laws alone for now
pdf_path = 'Documents For RAG'+os.sep+'PDFs'+os.sep+'Laws of Cricket'



"""
def partition_pdf_with_pypdf2(pdf_path, output_dir):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text() 1    
 1. 
github.com
"""

files_list = []
for root, dirs, files in os.walk(pdf_path):
    for file in files:
      files_list.append(os.path.join(root, file))

input_path = os.getcwd()
output_path = os.path.join(os.getcwd(),"output")

file = files_list[1]
# Get elements
raw_pdf_elements = partition_pdf(
    filename = file, #os.path.join(input_path,file)
    extract_images_in_pdf = True,
    infer_table_structure = True,
    chunking_strategy = "by_title",
    max_characters = 4000,
    new_after_n_characters = 3000,
    combine_text_under_n_characters = 2000,
    image_output_dir_path = output_path,
)

