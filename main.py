from pathlib import *
from PyPDF2 import PdfFileReader
import re


if __name__ == '__main__':



   for pdf_files in Path("pdf-reader").glob("*.pdf"):

       pdf_file = PdfFileReader(str(pdf_files))

       with Path("pdf-reader", "text.txt").open(mode="a", encoding='utf-8') as text_file:
           page = pdf_file.getPage(0)
           text = page.extractText()
           name_pdf = re.search(r"[S]?\w-\d\d\d[G]?", text)
           text_file.write(f"{name_pdf[0]} \n")
           pdf_files.rename(f"pdf-reader\{name_pdf[0]}.pdf")

       print("DONE: ", pdf_files)



