# -*- coding: utf-8 -*-

import arcpy
import os
import sys
from winsound import MessageBeep


def ricava_path_relativa_script_Python():
    """  Ritorna la path nella quale e' presente lo script in esecuzione """
    if os.path.dirname(__file__) != "":
        return os.path.dirname(__file__)

    elif os.path.dirname(os.path.abspath(__file__)) != "":
        return os.path.dirname(os.path.abspath(__file__))

    elif os.path.dirname(os.getcwd()) != "":
        return os.path.dirname(os.getcwd())

    else:
        from inspect import getsourcefile
        return os.path.dirname(os.path.abspath(getsourcefile(lambda _:None)))


path_relativa = ricava_path_relativa_script_Python()
sys.path.append(os.path.dirname(path_relativa))

import PyPDF2


def PDFsplit(pdf, splits):
    # creating input pdf file object
    pdfFileObj = open(pdf, 'rb')

    # creating pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # starting index of first slice
    start = 0

    # starting index of last slice
    end = splits[0]

    for i in range(len(splits)+1):
        # creating pdf writer object for (i+1)th split
        pdfWriter = PyPDF2.PdfFileWriter()

        # output pdf file name
        outputpdf = pdf.split('.pdf')[0] + "_" + str(i) + '.pdf'

        # adding pages to pdf writer object
        for page in range(start,end):
            pdfWriter.addPage(pdfReader.getPage(page))

        # writing split pdf pages to pdf file
        with open(outputpdf, "wb") as f:
            pdfWriter.write(f)

        # interchanging page split start position for next split
        start = end
        try:
            # setting split end positon for next split
            end = splits[i+1]
        except IndexError:
            # setting split end position for last split
            end = pdfReader.numPages

    # closing the input pdf file object
    pdfFileObj.close()
    del pdfFileObj


def main():
    pdf = arcpy.GetParameterAsText(0)

    splits = []
    for pagina in arcpy.GetParameterAsText(1).split(";"):
        splits.append(int(pagina))


    # calling PDFsplit function to split pdf
    PDFsplit(pdf, splits)

if __name__ == "__main__":

    versione_ArcGIS = arcpy.GetInstallInfo()["Version"]

    if versione_ArcGIS in ["9.3.1", "10"]:
        arcpy.AddError("ATTENZIONE: La versione di ArcGIS e' obsoleta e pertanto non e' supportata da questo Toolbox Custom!")
    else:
        main()