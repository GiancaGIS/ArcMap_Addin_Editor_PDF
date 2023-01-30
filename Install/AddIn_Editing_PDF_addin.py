# -*- coding: utf-8 -*-

import arcpy
import pythonaddins
import os


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



class EditaPDF(object):
    """Implementation for AddIn_Editing_PDF_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        path_mio_toolbox = os.path.join(path_relativa, "Modifica_PDF.tbx")
        pythonaddins.GPToolDialog(path_mio_toolbox, "EditaPDF")



class SplittaPDF(object):
    """Implementation for AddIn_Editing_PDF_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        path_mio_toolbox = os.path.join(path_relativa, "Modifica_PDF.tbx")
        pythonaddins.GPToolDialog(path_mio_toolbox, "SplittaPDF")


class ModificaMetadatiPDF(object):
    """Implementation for AddIn_Editing_PDF_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        path_mio_toolbox = os.path.join(path_relativa, "Modifica_PDF.tbx")
        pythonaddins.GPToolDialog(path_mio_toolbox, "EditaMetadatiPDF")