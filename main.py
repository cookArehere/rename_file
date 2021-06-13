from pathlib import *
from PyPDF2 import PdfFileReader
import re


if __name__ == '__main__':

    path_for_pdf_file = PureWindowsPath("D:/admin/python/pdf-reader")

    for i_file in Path(path_for_pdf_file).glob("*.pdf"):

       pdf_file = PdfFileReader(str(i_file))

       page = pdf_file.getPage(0)
       text = page.extractText()

       name_pdf = re.search(r"[S]?\w-\d\d\d[G]?", text)

       if "E" in name_pdf[0]:
           path_name_pdf = Path(path_for_pdf_file, "ERECTION PLATE", f"{name_pdf[0]}.pdf")
           i_file.rename(path_name_pdf)
       elif "SP" in name_pdf[0]:
           path_name_pdf = Path(path_for_pdf_file, "SPESIAL PLATE", f"{name_pdf[0]}.pdf")
           i_file.rename(path_name_pdf)
       elif "P" in name_pdf[0]:
           path_name_pdf = Path(path_for_pdf_file, "STANDART PLATE", f"{name_pdf[0]}.pdf")
           i_file.rename(path_name_pdf)

       print("DONE", name_pdf[0])




