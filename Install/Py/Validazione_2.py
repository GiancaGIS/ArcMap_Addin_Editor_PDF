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
    self.params[0].enabled = True
    self.params[1].enabled = False
    return

  def updateParameters(self):
    """Modify the values and properties of parameters before internal
    validation is performed.  This method is called whenever a parameter
    has been changed."""
    if self.params[0].value is not None:
        self.params[1].enabled = True
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