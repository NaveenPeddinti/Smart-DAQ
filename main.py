from PyQt5 import QtCore, QtGui, QtWidgets
from homePage import *

#pyuic5 -x pagename.ui -o pagename.py

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homePage = QtWidgets.QMainWindow()
    ui = Ui_homePage()
    ui.setupUi(homePage)
    homePage.show()
    '''DAQSettings = QtWidgets.QMainWindow()
    ui = Ui_DAQSettings()
    ui.setupUi(DAQSettings)
    DAQSettings.show()'''
    sys.exit(app.exec_())

