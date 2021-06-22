from pathlib import *
from PyPDF2 import PdfFileReader
import re

def renaming_pdf_file(path, dir, name):

    try:
        path_name_pdf = Path(path, dir, f"{name}.pdf")
        i_file.rename(path_name_pdf)

    except FileExistsError:
        order_list_same_file = list(Path(path, dir).glob("*.pdf"))

        quantity = 0

        for i in order_list_same_file:
            if re.findall(name, str(i)):
                quantity += 1

        path_name_pdf = Path(path, dir, f"{name}_{int(quantity)}.pdf")
        i_file.rename(path_name_pdf)


if __name__ == '__main__':

    path_for_pdf_file = PureWindowsPath("D:/admin/python/pdf-reader")

    for i_file in Path(path_for_pdf_file).glob("*.pdf"):

       pdf_file = PdfFileReader(str(i_file))

       page = pdf_file.getPage(0)
       text = page.extractText()

       name_pdf = re.search(r"[S]?\w-\d\d\d[G, AG, BG]?", text)

       if "E" in name_pdf[0]:
           renaming_pdf_file(path_for_pdf_file, "ERECTION PLATE", name_pdf[0])
       elif "SP" in name_pdf[0] or "Y" in name_pdf[0]:
           renaming_pdf_file(path_for_pdf_file, "SPECIAL PLATE", name_pdf[0])
       elif "P" in name_pdf[0]:
           renaming_pdf_file(path_for_pdf_file, "STANDART PLATE", name_pdf[0])

       print("DONE", name_pdf[0])




