# -*- coding: utf-8 -*-

import arcpy


if __name__ == '__main__':

    versione_ArcGIS = arcpy.GetInstallInfo()["Version"]

    if versione_ArcGIS in ["9.3.1", "10"]:
        arcpy.AddError("ATTENZIONE: La versione di ArcGIS e' obsoleta e pertanto non e' supportata da questo Toolbox Custom!")
    else:

        try:

            path_pdf = arcpy.GetParameterAsText(0)
            pdf = arcpy.mapping.PDFDocumentOpen(path_pdf)

            pdf.updateDocProperties(pdf_title=arcpy.GetParameterAsText(1),
                                       pdf_author=arcpy.GetParameterAsText(2),
                                       pdf_subject=arcpy.GetParameterAsText(3),
                                       pdf_keywords=arcpy.GetParameterAsText(4),
                                       pdf_open_view="USE_THUMBS",
                                       pdf_layout="SINGLE_PAGE")

            pdf.saveAndClose()
            del pdf

        except arcpy.ExecuteError:
            arcpy.AddError(arcpy.GetMessages(2))
