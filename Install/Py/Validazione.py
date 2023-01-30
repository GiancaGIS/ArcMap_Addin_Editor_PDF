import arcpy

class ToolValidator(object):
  """Class for validating a tool's parameter values and controlling
  the behavior of the tool's dialog."""

  def __init__(self):
    """Setup arcpy and the list of tool parameters."""
    self.params = arcpy.GetParameterInfo()

  def initializeParameters(self):
    """Refine the properties of a tool's parameters.  This method is
    called when the tool is opened."""
    self.params[5].enabled = False
    self.params[6].enabled = False
    self.params[7].enabled = False
    self.params[8].enabled = False
    return

  def updateParameters(self):
    """Modify the values and properties of parameters before internal
    validation is performed.  This method is called whenever a parameter
    has been changed."""
    if str(self.params[1].value).lower() == "elimina pagine da pdf":
        self.params[2].enabled = False
        self.params[3].enabled = True

    elif str(self.params[1].value).lower() == "fondi piu' pdf tra loro":
        self.params[2].enabled = True
        self.params[3].enabled = False

    if str(self.params[4].value).lower() == "true":
        self.params[5].enabled = True
        self.params[6].enabled = True
        self.params[7].enabled = True
        self.params[8].enabled = True
    else:

        self.params[5].enabled = False
        self.params[6].enabled = False
        self.params[7].enabled = False
        self.params[8].enabled = False

    return

  def updateMessages(self):
    """Modify the messages created by internal validation for each tool
    parameter.  This method is called after internal validation."""
    self.params[0].clearMessage()
    for carattere_marcio in ["'", "?", "<", ">", "*", "|"]:
        if carattere_marcio in str((self.params[0].value)):
            self.params[0].setErrorMessage("ATTENZIONE: Nella directory e' presente uno di questi caratteri speciali: \/*?'<>|   \nSI PREGA DI RIMUOVERLO, GRAZIE.")
            break
    return