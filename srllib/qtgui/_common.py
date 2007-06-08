from PyQt4.QtCore import *
from PyQt4.QtGui import *

def messageCritical(title, text, detailedText=None, informativeText=None, parent=None):
    """ Display a critical message in a L{QMessageBox}. """
    dlg = QMessageBox(QMessageBox.Critical, title, text, QMessageBox.Ok, parent)
    if informativeText:
        dlg.setInformativeText(informativeText)
    if detailedText:
        dlg.setDetailedText(detailedText)
    dlg.exec_()

def messageWarning(title, text, detailedText=None, informativeText=None, parent=None):
    """ Display a warning message in a L{QMessageBox}. """
    dlg = QMessageBox(QMessageBox.Warning, title, text, QMessageBox.Ok, parent)
    if informativeText:
        dlg.setInformativeText(informativeText)
    if detailedText:
        dlg.setDetailedText(detailedText)
    dlg.exec_()
