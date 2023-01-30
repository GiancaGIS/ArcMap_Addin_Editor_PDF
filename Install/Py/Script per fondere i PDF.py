# -*- coding: utf-8 -*-

import arcpy



class Liste:

    def __init__(self, lista_input="Inserire lista di path"):
        self.lista = lista_input

    def ordina_lista_di_stringhe_numericamente(self):
        """ Questa funzione mi permette di ordinare numericamente delle liste di stringhe con path a file numerati!
        Es: C:\\.....\\1.txt, C:\\.....\\2.txt eccetera"""

        import re

        convert = lambda text: float(text) if text.isdigit() else text
        alphanum = lambda key: [convert(c) for c in re.split("([-+]?[0-9]*\.?[0-9]*)", key)]
        self.lista.sort(key = alphanum)

        return self.lista



def fondi_pdf(pdf, vera_lista_file_pdf):
    for file in vera_lista_file_pdf:
        pdf.appendPages(file)


def elimina_pagine_PDF(pdf, pagine_da_rimuovere):
    pdf.deletePages(pagine_da_rimuovere)



if __name__ == '__main__':

    versione_ArcGIS = arcpy.GetInstallInfo()["Version"]

    if versione_ArcGIS in ["9.3.1", "10"]:
        arcpy.AddError("ATTENZIONE: La versione di ArcGIS e' obsoleta e pertanto non e' supportata da questo Toolbox Custom!")
    else:

        try:

            path_pdf = arcpy.GetParameterAsText(0)
            pdf = arcpy.mapping.PDFDocumentOpen(path_pdf)

            operazione_scelta = arcpy.GetParameterAsText(1)

            if operazione_scelta.lower() == "elimina pagine da pdf":
                lista_file_pdf = None
                pagine_da_rimuovere = arcpy.GetParameterAsText(3)
                elimina_pagine_PDF(pdf, pagine_da_rimuovere)

            else:

                lista_file_pdf = arcpy.GetParameterAsText(2)
                temp = []
                for file_pdf in lista_file_pdf.split(";"):
                    temp.append(file_pdf.replace("'", ""))

                vera_lista_file_pdf = Liste.ordina_lista_di_stringhe_numericamente(Liste(temp))
                pagine_da_rimuovere = None

                fondi_pdf(pdf, vera_lista_file_pdf)

            if arcpy.GetParameterAsText(4).lower() == "true":

                pdf.updateDocProperties(pdf_title=arcpy.GetParameterAsText(5),
                                           pdf_author=arcpy.GetParameterAsText(6),
                                           pdf_subject=arcpy.GetParameterAsText(7),
                                           pdf_keywords=arcpy.GetParameterAsText(8),
                                           pdf_open_view="USE_THUMBS",
                                           pdf_layout="SINGLE_PAGE")

            pdf.saveAndClose()
            del pdf

        except arcpy.ExecuteError:
            arcpy.AddError(arcpy.GetMessages(2))
