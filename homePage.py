
# Created: Fri Dec 14 14:24:57 2018
#      by: PyQt5 UI code generator 5.2.1


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp, QDate, QTime, QDateTime, QTimer
from PyQt5.QtGui import QRegExpValidator, QIcon, QPixmap
from PyQt5.QtWidgets import QLineEdit,QMessageBox,QInputDialog, QFileDialog, QPushButton
from PyQt5.QtCore import pyqtSlot

from sqliteDB import *
from tcpclient import getDAQReadings
#from colorsettings import *


class Ui_homePage(object):
    deviceCount=0
    deviceNumber=1
    parNumber = 0
    seqNumber = 0
    parCount = 8
    lParName = ["C1","C2","C3","C4","C5","C6", "C7", "C8"]
    lParUnits = ["unit1","unit2","unit3","unit4","unit5","unit6","unit7","unit8"]
    lParMin = [0,0,0,0,0,0,0,0]
    lParMax = [10,10,10,10,10,10,10,10]
    lParValues = []
    sDaqName=[]
    sDaqIpAddrs=[]
    sDaqPortNum=[]
    sDaqStatus=[]
    iSwitchingTime = 0
    iSuspentionCount = 0
    liSuspentionNum = []
    colorStateOfDev=""
    def setupUi(self, homePage):
        homePage.setObjectName("homePage")
        homePage.resize(954, 749)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(homePage.sizePolicy().hasHeightForWidth())
        homePage.setSizePolicy(sizePolicy)
        Create_DB()
        self.deviceCount=getNoOfDAQs()
        self.sDaqStatus = [1]*self.deviceCount
        self.liSuspentionNum = [0]* self.deviceCount
        print("HomePage - DeviceCount", self.deviceCount,"\nDevice Status", self.sDaqStatus)
        self.centralWidget = QtWidgets.QWidget(homePage)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_top = QtWidgets.QWidget(self.centralWidget)
        self.widget_top.setMaximumSize(QtCore.QSize(1000, 80))
        self.widget_top.setObjectName("widget_top")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_top)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(732, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 3, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_ApplicationName = QtWidgets.QLabel(self.widget_top)
        self.label_ApplicationName.setObjectName("label_ApplicationName")
        self.horizontalLayout.addWidget(self.label_ApplicationName)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 3)
        self.labelLogo1 = QtWidgets.QLabel(self.widget_top)
        self.labelLogo1.setText("")
        self.labelLogo1.setObjectName("labelLogo1")
        self.gridLayout_2.addWidget(self.labelLogo1, 0, 4, 3, 1)
        self.labelLogo = QtWidgets.QLabel(self.widget_top)
        self.labelLogo.setMaximumSize(QtCore.QSize(10, 16777215))
        self.labelLogo.setText("")
        self.labelLogo.setObjectName("labelLogo")
        self.gridLayout_2.addWidget(self.labelLogo, 0, 0, 3, 1)
        self.label_time = QtWidgets.QLabel(self.widget_top)
        self.label_time.setText("")
        self.label_time.setObjectName("label_time")
        self.gridLayout_2.addWidget(self.label_time, 2, 1, 1, 2)
        self.gridLayout_5.addWidget(self.widget_top, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(130, 660, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 2, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(130, 60, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 1, 0, 1, 1)
        self.widget_main = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_main.sizePolicy().hasHeightForWidth())
        self.widget_main.setSizePolicy(sizePolicy)
        self.widget_main.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.widget_main.setObjectName("widget_main")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_main)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelclrR = QtWidgets.QLabel(self.widget_main)
        self.labelclrR.setMinimumSize(QtCore.QSize(15, 15))
        self.labelclrR.setMaximumSize(QtCore.QSize(15, 15))
        self.labelclrR.setStyleSheet("background-color:#fb587e;")
        self.labelclrR.setText("")
        self.labelclrR.setObjectName("labelclrR")
        self.horizontalLayout_2.addWidget(self.labelclrR)
        self.label_7 = QtWidgets.QLabel(self.widget_main)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.labelclrY = QtWidgets.QLabel(self.widget_main)
        self.labelclrY.setMinimumSize(QtCore.QSize(15, 15))
        self.labelclrY.setMaximumSize(QtCore.QSize(15, 15))
        self.labelclrY.setStyleSheet("background-color: #F7F975;")
        self.labelclrY.setText("")
        self.labelclrY.setObjectName("labelclrY")
        self.horizontalLayout_2.addWidget(self.labelclrY)
        self.label_6 = QtWidgets.QLabel(self.widget_main)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.labelclrP = QtWidgets.QLabel(self.widget_main)
        self.labelclrP.setMinimumSize(QtCore.QSize(15, 15))
        self.labelclrP.setMaximumSize(QtCore.QSize(15, 15))
        self.labelclrP.setStyleSheet("background-color:rgba(255, 194, 211, 255);")
        self.labelclrP.setText("")
        self.labelclrP.setObjectName("labelclrP")
        self.horizontalLayout_2.addWidget(self.labelclrP)
        self.label_11 = QtWidgets.QLabel(self.widget_main)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.labelclrG = QtWidgets.QLabel(self.widget_main)
        self.labelclrG.setMinimumSize(QtCore.QSize(15, 15))
        self.labelclrG.setMaximumSize(QtCore.QSize(15, 15))
        self.labelclrG.setStyleSheet("background-color: rgba(206, 246, 206, 255);")
        self.labelclrG.setText("")
        self.labelclrG.setObjectName("labelclrG")
        self.horizontalLayout_2.addWidget(self.labelclrG)
        self.label_13 = QtWidgets.QLabel(self.widget_main)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        spacerItem6 = QtWidgets.QSpacerItem(346, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 3, 1, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(880, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem7, 4, 0, 1, 3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.sDaqName=getDaqNamesfromList()
        self.sDaqIpAddrs=getDaqIpfromList()
        self.sDaqPortNum = getPortNumberfromList()
        #print("Daq Names: ",self.sDaqName)
        #print("Daq IP-Addrs: ",self.sDaqIpAddrs)
        if (self.deviceCount > 0):
            spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
            self.gridLayout_3.addItem(spacerItem8, 0, 0, 1, 2)
        self.button = []
        grid_row=1
        grid_col=0
        for num in range(0,self.deviceCount):
            self.button.append(QtWidgets.QPushButton(self.widget_main))
            self.button[num].setEnabled(True)
            self.button[num].setText(self.sDaqName[num])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(40)
            sizePolicy.setVerticalStretch(10)
            sizePolicy.setHeightForWidth(self.button[num].sizePolicy().hasHeightForWidth())
            self.button[num].setSizePolicy(sizePolicy)
            self.button[num].setMinimumSize(QtCore.QSize(80, 20))
            self.button[num].setMaximumSize(QtCore.QSize(100, 100))
            self.button[num].setObjectName("ButtonDAQ"+str(num+1)+"Helth")
            self.gridLayout_3.addWidget(self.button[num], grid_row, grid_col, 1, 1)
            if (self.deviceCount <=6):
                grid_col = 0
                grid_row = grid_row + 1
            elif (self.deviceCount > 6 and self.deviceCount <= 30):
                grid_col = grid_col+1
                if(grid_col >= 2):
                    grid_row = grid_row+1
                    grid_col = 0
            elif (self.deviceCount > 30 and self.deviceCount <= 50):
                grid_col = grid_col+1
                if(grid_col >= 3):
                    grid_row = grid_row+1
                    grid_col = 0
        if (self.deviceCount > 0):
            spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.gridLayout_3.addItem(spacerItem9, grid_row+1, 0, 1, 2)

        self.gridLayout_6.addLayout(self.gridLayout_3, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem16 = QtWidgets.QSpacerItem(600, 30, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem16, 0, 0, 1, 3)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem14, 1, 0, 2, 1)
        spacerItem15 = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 1, 4, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem13, 1, 9, 1, 1)

        '''self.label_ParName = []
        self.lineEdit_ParValue = []
        self.label_Units = []
        self.spacerItem17 = []
        grid_row=1
        grid_col=1
        for num in range(0,self.parCount):
            self.label_ParName.append(QtWidgets.QLabel(self.widget_main))
            self.label_ParName[num].setObjectName("label_ParName"+str(num+1))
            self.label_ParName[num].setText(QtCore.QCoreApplication.translate("homePage", "ParName"+str(num+1)+": "))
            self.gridLayout.addWidget(self.label_ParName[num], grid_row, grid_col, 1, 1)
            grid_col = grid_col + 1
            self.lineEdit_ParValue.append(QtWidgets.QLineEdit(self.widget_main))
            self.lineEdit_ParValue[num].setObjectName("lineEdit_ParValue"+str(num+1))
            self.gridLayout.addWidget(self.lineEdit_ParValue[num], grid_row, grid_col, 1, 1)
            grid_col = grid_col + 1
            self.label_Units.append(QtWidgets.QLabel(self.widget_main))
            self.label_Units[num].setObjectName("label_Units"+str(num+1))
            self.label_Units[num].setText(QtCore.QCoreApplication.translate("homePage", "     units"+str(num+1)))
            self.gridLayout.addWidget(self.label_Units[num], grid_row, grid_col, 1, 1)
            grid_col = grid_col + 2
            if grid_col >= 7 :
                grid_row = grid_row + 1
                self.spacerItem17.append(QtWidgets.QSpacerItem(500, 14, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum))
                self.gridLayout.addItem(self.spacerItem17[int(num/2)], grid_row, 0, 1, 3)
                grid_row = grid_row + 1
                grid_col = 1'''
        self.displayParameters()

        self.verticalLayout.addLayout(self.gridLayout)
        self.textEdit = QtWidgets.QTextEdit(self.widget_main)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.gridLayout_6.addLayout(self.verticalLayout, 1, 2, 2, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 438, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem10, 1, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(877, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_6.addItem(spacerItem11, 0, 0, 1, 3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 470, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem12, 1, 3, 1, 1)
        self.gridLayout_5.addWidget(self.widget_main, 1, 1, 1, 1)
        homePage.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(homePage)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 954, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuViewData = QtWidgets.QMenu(self.menuBar)
        self.menuViewData.setObjectName("menuViewData")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        homePage.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(homePage)
        self.mainToolBar.setObjectName("mainToolBar")
        homePage.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(homePage)
        self.statusBar.setObjectName("statusBar")
        homePage.setStatusBar(self.statusBar)
        self.actionGrid = QtWidgets.QAction(homePage)
        self.actionGrid.setObjectName("actionGrid")
        self.actionDAQ = QtWidgets.QAction(homePage)
        self.actionDAQ.setObjectName("actionDAQ")
        self.actionGraphVeiw = QtWidgets.QAction(homePage)
        self.actionGraphVeiw.setObjectName("actionGraphVeiw")
        self.menuViewData.addAction(self.actionGrid)
        self.menuViewData.addAction(self.actionGraphVeiw)
        self.menuSettings.addAction(self.actionDAQ)
        self.menuBar.addAction(self.menuViewData.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(homePage)
        self.actionDAQ.triggered.connect(lambda: self.on_triggered_actionDAQ(homePage))
        #self.connectDAQButtonsToSlots()
        QtCore.QMetaObject.connectSlotsByName(homePage)
        '''for num in range(0,self.deviceCount-1):
            homePage.setTabOrder(self.button[num], self.button[num+1])'''
        self.addStyleSheet(homePage)
        self.initFunctionality()
        

    def retranslateUi(self, homePage):
        _translate = QtCore.QCoreApplication.translate
        homePage.setWindowTitle(_translate("homePage", "tcpsocket"))
        self.label_ApplicationName.setText(_translate("homePage", "<html><head/><body><p align=\"center\">MST Radar Health Monitoring System</p></body></html>"))
        self.label_7.setText(_translate("homePage", "DAQ Unit Suspended"))
        self.label_6.setText(_translate("homePage", "DAQ Unit not Responding"))
        self.label_11.setText(_translate("homePage", "DAQ Unit Abnormal"))
        self.label_13.setText(_translate("homePage", "DAQ Unit Readings are Healthy"))
        '''self.label_ParName1.setText(_translate("homePage", "Par1Name: "))
        self.label_Units1.setText(_translate("homePage", "units1"))
        self.label_Units2.setText(_translate("homePage", "Units2"))
        self.label_ParName2.setText(_translate("homePage", "Par2Name: "))'''
        self.textEdit.setHtml(_translate("homePage", "Add text related to MST radar"))
        self.menuViewData.setTitle(_translate("homePage", "History"))
        self.menuSettings.setTitle(_translate("homePage", "Settings"))
        self.actionGrid.setText(_translate("homePage", "GridVeiw"))
        self.actionDAQ.setText(_translate("homePage", "DAQ"))
        self.actionGraphVeiw.setText(_translate("homePage", "GraphVeiw"))

    def addStyleSheet(self, homePage):

        sName = "Default"
        sHederColor = "#40ff00"
        sBodyColor = "#cdd6d9"
        sBackgroundColor = "#e9eaea"
        sBackImagePath = ""
        sTextColor = "black"
        sFont = "10"
        sTextStyle = "Comic Sans MS"
        sTextBGColor = "#e9eaea"
        '''settingsList = getAppColorSettings()
        if len(settingsList) >=9:
            sName = settingsList[1]
            sHederColor = settingsList[2]
            sBodyColor = settingsList[3]
            sBackgroundColor = settingsList[4]
            sBackImagePath = settingsList[5]
            sTextColor = settingsList[6]
            sFont = settingsList[7]
            sTextStyle = settingsList[8]
            sTextBGColor = settingsList[9]'''

        '''hederColor = "#72BAEA"
        bodyColor = "#cdd6d9"
        backgroundColor = "#e9eaea"
        backImagePath = "/home/tss-nandini/python/qtpy/practice/ui_python/UseFullApplications/pics/20.jpg"
        lableTextColor ="black"
        textfont = "font:10pt Comic Sans MS"
        hederColor = "#75d3ca"
        bodyColor = "#cdd6d9"
        backgroundColor = "#e9eaea"
        backImagePath = "/home/tss-nandini/python/qtpy/practice/ui_python/UseFullApplications/pics/13.jpg"
        lableTextColor ="black"
        textfont = "font:10pt Comic Sans MS"'''
        #background-image:url(/home/tss-nandini/python/qtpy/practice/ui_python/UseFullApplications/pics/HH.png)
        styleSheet = '''QMenuBar,QToolBar{background: qlineargradient(x1:0,x2:0,y1:0,y2:1,stop:0 #cccccc, stop:0.4  #C0C0C0 );color:white;} 
QStatusBar{background: qlineargradient(x1:0,x2:0,y1:0,y2:1,stop:0 #cccccc, stop:0.4  #C0C0C0 );color:white;} 
QLineEdit{ background-color: '''+sTextBGColor+'''; padding: 1px; border-width: 5px;  border-color: beige;min-width: 120px; max-width: 260px;}
QComboBox{ background-color: '''+sTextBGColor+'''; padding: 1px; border-width: 1px;  border-color: beige;min-width: 120px;}
QMainWindow{background-color: '''+sBackgroundColor+''';} #widget_main{background-color:'''+sBodyColor+''';  border-radius: 5px;background-image:url('''+sBackImagePath+''')}
QLabel{min-width: 120px;min-width: 140px;} #labelclrR{min-width: 20px;} #labelclrY{min-width: 20px;} #labelclrP{min-width: 20px;} #labelclrG{min-width: 20px;}
QPushButton{font: 10pt;background-color:;}
#widget_top{background-color:'''+sHederColor+''';  border-radius: 5px; border-style: outset;padding: 0px;}
QLabel{font:'''+sFont+'''pt '''+sTextStyle+''';color:'''+sTextColor+''';} QPushButton{font:'''+sFont+'''pt '''+sTextStyle+''';color:'''+sTextColor+''';} QLineEdit{font:'''+sFont+'''pt '''+sTextStyle+''';color:'''+sTextColor+''';} QCheckBox{font:'''+sFont+'''pt '''+sTextStyle+''';color:'''+sTextColor+''';}  QTextEdit{font:'''+sFont+'''pt '''+sTextStyle+''';color:'''+sTextColor+''';background-color:'''+sBodyColor+'''; } '''
        #self.textEdit.setAutoFillBackground(False)
        homePage.setStyleSheet(styleSheet)
        listAppSettings = selectFromAppSettings()
        print(listAppSettings)
        '''if len(listAppSettings) >= 13:
            pixmap = QPixmap(listAppSettings[2])
            self.labelLogo.setPixmap(pixmap.scaled(60,60))'''

    def initFunctionality(self):
        operationSettings = selectFromOperationSettings()
        self.iSwitchingTime = int(operationSettings[0])
        self.iSuspentionCount = int(operationSettings[1])
        self.timerDaq = QTimer()
        self.timerDaq.setSingleShot(False)
        self.timerDaq.timeout.connect(self.timerDaq_timeout)
        self.timerDaq.start(self.iSwitchingTime*1000)
        self.timerDaq_timeout()

    def timerDaq_timeout(self):
        print("Time out : timerDaq")
        if self.sDaqStatus[self.deviceNumber-1] == 1:
            self.sDaqIpAddrs=getDaqIpfromList()
            self.sDaqPortNum = getPortNumberfromList()
            readings = str(getDAQReadings(self.sDaqIpAddrs[self.deviceNumber-1], self.sDaqPortNum[self.deviceNumber-1]))
            lreadings = []
            if len(readings) > 10 and readings.find("#") != -1:
                lreadings = readings.split("#")[1].split(",")
            print("device Number: ", self.deviceNumber)
            print("device Name: ", self.sDaqName[self.deviceNumber-1])
            print("device IP: ", self.sDaqIpAddrs[self.deviceNumber-1])
            print("device Port: ", self.sDaqPortNum[self.deviceNumber-1])
            print("lreadings: ", lreadings)
            self.displayDAQSettings(self.deviceNumber, lreadings)
            self.deviceNumber += 1
            if (self.deviceNumber>self.deviceCount):
                self.deviceNumber=1
        elif self.sDaqStatus[self.deviceNumber-1] != 1:
            self.deviceNumber += 1
            if (self.deviceNumber>self.deviceCount):
                self.deviceNumber=1
            self.timerDaq_timeout()
        #self.daqButton1Clicked()

    def connectDAQButtonsToSlots(self):
        for num in range(0,self.deviceCount):
            if num == 0:
                self.button[num].clicked.connect(self.daqButton1Clicked)
            elif num == 1:
                self.button[num].clicked.connect(self.daqButton2Clicked)
            elif num == 2:
                self.button[num].clicked.connect(self.daqButton3Clicked)
            elif num == 3:
                self.button[num].clicked.connect(self.daqButton4Clicked)
            elif num == 4:
                self.button[num].clicked.connect(self.daqButton5Clicked)
            elif num == 5:
                self.button[num].clicked.connect(self.daqButton6Clicked)
            elif num == 6:
                self.button[num].clicked.connect(self.daqButton7Clicked)
            elif num == 7:
                self.button[num].clicked.connect(self.daqButton8Clicked)
            elif num == 8:
                self.button[num].clicked.connect(self.daqButton9Clicked)
            elif num == 9:
                self.button[num].clicked.connect(self.daqButton10Clicked)
            elif num == 10:
                self.button[num].clicked.connect(self.daqButton11Clicked)
            elif num == 11:
                self.button[num].clicked.connect(self.daqButton12Clicked)
            elif num == 12:
                self.button[num].clicked.connect(self.daqButton13Clicked)
            elif num == 13:
                self.button[num].clicked.connect(self.daqButton14Clicked)
            elif num == 14:
                self.button[num].clicked.connect(self.daqButton15Clicked)
            elif num == 15:
                self.button[num].clicked.connect(self.daqButton16Clicked)
            elif num == 16:
                self.button[num].clicked.connect(self.daqButton17Clicked)
            elif num == 17:
                self.button[num].clicked.connect(self.daqButton18Clicked)
            elif num == 18:
                self.button[num].clicked.connect(self.daqButton19Clicked)
            elif num == 19:
                self.button[num].clicked.connect(self.daqButton20Clicked)
            elif num == 20:
                self.button[num].clicked.connect(self.daqButton21Clicked)
            elif num == 21:
                self.button[num].clicked.connect(self.daqButton22Clicked)
            elif num == 22:
                self.button[num].clicked.connect(self.daqButton23Clicked)
            elif num == 23:
                self.button[num].clicked.connect(self.daqButton24Clicked)
            elif num == 24:
                self.button[num].clicked.connect(self.daqButton25Clicked)
            elif num == 25:
                self.button[num].clicked.connect(self.daqButton26Clicked)
            elif num == 26:
                self.button[num].clicked.connect(self.daqButton27Clicked)
            elif num == 27:
                self.button[num].clicked.connect(self.daqButton28Clicked)
            elif num == 28:
                self.button[num].clicked.connect(self.daqButton29Clicked)
            elif num == 29:
                self.button[num].clicked.connect(self.daqButton30Clicked)
            elif num == 30:
                self.button[num].clicked.connect(self.daqButton31Clicked)
            elif num == 31:
                self.button[num].clicked.connect(self.daqButton32Clicked)
            elif num == 32:
                self.button[num].clicked.connect(self.daqButton33Clicked)
            elif num == 33:
                self.button[num].clicked.connect(self.daqButton34Clicked)
            elif num == 34:
                self.button[num].clicked.connect(self.daqButton35Clicked)
            elif num == 35:
                self.button[num].clicked.connect(self.daqButton36Clicked)
            elif num == 36:
                self.button[num].clicked.connect(self.daqButton37Clicked)
            elif num == 37:
                self.button[num].clicked.connect(self.daqButton38Clicked)
            elif num == 38:
                self.button[num].clicked.connect(self.daqButton39Clicked)
            elif num == 39:
                self.button[num].clicked.connect(self.daqButton40Clicked)
            elif num == 40:
                self.button[num].clicked.connect(self.daqButton41Clicked)
            elif num == 41:
                self.button[num].clicked.connect(self.daqButton42Clicked)
            elif num == 42:
                self.button[num].clicked.connect(self.daqButton43Clicked)
            elif num == 43:
                self.button[num].clicked.connect(self.daqButton44Clicked)
            elif num == 44:
                self.button[num].clicked.connect(self.daqButton45Clicked)
            elif num == 45:
                self.button[num].clicked.connect(self.daqButton46Clicked)
            elif num == 46:
                self.button[num].clicked.connect(self.daqButton47Clicked)
            elif num == 47:
                self.button[num].clicked.connect(self.daqButton48Clicked)
            elif num == 48:
                self.button[num].clicked.connect(self.daqButton49Clicked)
            elif num == 49:
                self.button[num].clicked.connect(self.daqButton50Clicked)



    @pyqtSlot()

    def daqButton1Clicked(self):
        self.deviceNumber=1
        self.displayDAQSettings(self.deviceNumber)

    def daqButton2Clicked(self):
        self.deviceNumber=2
        self.displayDAQSettings(self.deviceNumber)

    def daqButton3Clicked(self):
        self.deviceNumber=3
        self.displayDAQSettings(self.deviceNumber)

    def daqButton4Clicked(self):
        self.deviceNumber=4
        self.displayDAQSettings(self.deviceNumber)

    def daqButton5Clicked(self):
        self.deviceNumber=5
        self.displayDAQSettings(self.deviceNumber)

    def daqButton6Clicked(self):
        self.deviceNumber=6
        self.displayDAQSettings(self.deviceNumber)

    def daqButton7Clicked(self):
        self.deviceNumber=7
        self.displayDAQSettings(self.deviceNumber)

    def daqButton8Clicked(self):
        self.deviceNumber=8
        self.displayDAQSettings(self.deviceNumber)

    def daqButton9Clicked(self):
        self.deviceNumber=9
        self.displayDAQSettings(self.deviceNumber)

    def daqButton10Clicked(self):
        self.deviceNumber=10
        self.displayDAQSettings(self.deviceNumber)

    def daqButton11Clicked(self):
        self.deviceNumber=11
        self.displayDAQSettings(self.deviceNumber)

    def daqButton12Clicked(self):
        self.deviceNumber=12
        self.displayDAQSettings(self.deviceNumber)

    def daqButton13Clicked(self):
        self.deviceNumber=13
        self.displayDAQSettings(self.deviceNumber)

    def daqButton14Clicked(self):
        self.deviceNumber=14
        self.displayDAQSettings(self.deviceNumber)

    def daqButton15Clicked(self):
        self.deviceNumber=15
        self.displayDAQSettings(self.deviceNumber)

    def daqButton16Clicked(self):
        self.deviceNumber=16
        self.displayDAQSettings(self.deviceNumber)

    def daqButton17Clicked(self):
        self.deviceNumber=17
        self.displayDAQSettings(self.deviceNumber)

    def daqButton18Clicked(self):
        self.deviceNumber=18
        self.displayDAQSettings(self.deviceNumber)

    def daqButton19Clicked(self):
        self.deviceNumber=19
        self.displayDAQSettings(self.deviceNumber)

    def daqButton20Clicked(self):
        self.deviceNumber=20
        self.displayDAQSettings(self.deviceNumber)

    def daqButton21Clicked(self):
        self.deviceNumber=21
        self.displayDAQSettings(self.deviceNumber)

    def daqButton22Clicked(self):
        self.deviceNumber=22
        self.displayDAQSettings(self.deviceNumber)

    def daqButton23Clicked(self):
        self.deviceNumber=23
        self.displayDAQSettings(self.deviceNumber)

    def daqButton24Clicked(self):
        self.deviceNumber=24
        self.displayDAQSettings(self.deviceNumber)

    def daqButton25Clicked(self):
        self.deviceNumber=25
        self.displayDAQSettings(self.deviceNumber)

    def daqButton26Clicked(self):
        self.deviceNumber=26
        self.displayDAQSettings(self.deviceNumber)

    def daqButton27Clicked(self):
        self.deviceNumber=27
        self.displayDAQSettings(self.deviceNumber)

    def daqButton28Clicked(self):
        self.deviceNumber=28
        self.displayDAQSettings(self.deviceNumber)

    def daqButton29Clicked(self):
        self.deviceNumber=29
        self.displayDAQSettings(self.deviceNumber)

    def daqButton30Clicked(self):
        self.deviceNumber=30
        self.displayDAQSettings(self.deviceNumber)

    def daqButton31Clicked(self):
        self.deviceNumber=31
        self.displayDAQSettings(self.deviceNumber)

    def daqButton32Clicked(self):
        self.deviceNumber=32
        self.displayDAQSettings(self.deviceNumber)

    def daqButton33Clicked(self):
        self.deviceNumber=33
        self.displayDAQSettings(self.deviceNumber)

    def daqButton34Clicked(self):
        self.deviceNumber=34
        self.displayDAQSettings(self.deviceNumber)

    def daqButton35Clicked(self):
        self.deviceNumber=35
        self.displayDAQSettings(self.deviceNumber)

    def daqButton36Clicked(self):
        self.deviceNumber=36
        self.displayDAQSettings(self.deviceNumber)

    def daqButton37Clicked(self):
        self.deviceNumber=37
        self.displayDAQSettings(self.deviceNumber)

    def daqButton38Clicked(self):
        self.deviceNumber=38
        self.displayDAQSettings(self.deviceNumber)

    def daqButton39Clicked(self):
        self.deviceNumber=39
        self.displayDAQSettings(self.deviceNumber)

    def daqButton40Clicked(self):
        self.deviceNumber=40
        self.displayDAQSettings(self.deviceNumber)

    def daqButton41Clicked(self):
        self.deviceNumber=41
        self.displayDAQSettings(self.deviceNumber)

    def daqButton42Clicked(self):
        self.deviceNumber=42
        self.displayDAQSettings(self.deviceNumber)

    def daqButton43Clicked(self):
        self.deviceNumber=43
        self.displayDAQSettings(self.deviceNumber)

    def daqButton44Clicked(self):
        self.deviceNumber=44
        self.displayDAQSettings(self.deviceNumber)

    def daqButton45Clicked(self):
        self.deviceNumber=45
        self.displayDAQSettings(self.deviceNumber)

    def daqButton46Clicked(self):
        self.deviceNumber=46
        self.displayDAQSettings(self.deviceNumber)

    def daqButton47Clicked(self):
        self.deviceNumber=47
        self.displayDAQSettings(self.deviceNumber)

    def daqButton48Clicked(self):
        self.deviceNumber=48
        self.displayDAQSettings(self.deviceNumber)

    def daqButton49Clicked(self):
        self.deviceNumber=49
        self.displayDAQSettings(self.deviceNumber)

    def daqButton50Clicked(self):
        self.deviceNumber=50
        self.displayDAQSettings(self.deviceNumber)


    def displayParameters(self):
        self.label_ParName = []
        self.lineEdit_ParValue = []
        self.label_Units = []
        self.spacerItem17 = []
        grid_row=1
        grid_col=1
        iParValueslen = len(self.lParValues)
        for num in range(0,self.parCount):
            self.label_ParName.append(QtWidgets.QLabel(self.widget_main))
            self.label_ParName[num].setObjectName("label_ParName"+str(num+1))
            self.label_ParName[num].setText(QtCore.QCoreApplication.translate("homePage", self.lParName[num]+": "))
            self.gridLayout.addWidget(self.label_ParName[num], grid_row, grid_col, 1, 1)
            grid_col = grid_col + 1
            self.lineEdit_ParValue.append(QtWidgets.QLineEdit(self.widget_main))
            self.lineEdit_ParValue[num].setObjectName("lineEdit_ParValue"+str(num+1))
            if (iParValueslen>0 and iParValueslen>num):
                self.lineEdit_ParValue[num].setText(self.lParValues[num])
            self.gridLayout.addWidget(self.lineEdit_ParValue[num], grid_row, grid_col, 1, 1)
            grid_col = grid_col + 1
            '''self.label_Units.append(QtWidgets.QLabel(self.widget_main))
            self.label_Units[num].setObjectName("label_Units"+str(num+1))
            self.label_Units[num].setText(QtCore.QCoreApplication.translate("homePage", "     "+self.lParUnits[num]))
            self.gridLayout.addWidget(self.label_Units[num], grid_row, grid_col, 1, 1)'''
            grid_col = grid_col + 2
            if grid_col >= 7 :
                grid_row = grid_row + 1
                self.spacerItem17.append(QtWidgets.QSpacerItem(500, 14, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum))
                self.gridLayout.addItem(self.spacerItem17[int(num/2)], grid_row, 0, 1, 3)
                grid_row = grid_row + 1
                grid_col = 1

    def RemoveParameters(self):
        for num in range(0,self.parCount):
            #self.button[num] = QtWidgets.QPushButton(self,'Delete')
            self.label_ParName[num].deleteLater()
            self.lineEdit_ParValue[num].deleteLater()
            #self.label_Units[num].deleteLater()
            #QPushButton.remove(self.button[num])

    def displayDAQSettings(self,deviceNumber, lreadings):
        print ("daqButton"+str(deviceNumber)+"Clicked")
        listParSettings = getParSettings(deviceNumber)
        #print(listParSettings)
        iCount = 0
        lParName = []
        lParUnits = []
        lParMin = []
        lParMax = []
        for parSettings in listParSettings:
            lParName.append(parSettings[0])
            #lParUnits.append(parSettings[1])
            lParMin.append(parSettings[4])
            lParMax.append(parSettings[5])
            iCount += 1
        self.lParName = lParName
        #self.lParUnits = lParUnits
        self.lParMin = lParMin
        self.lParMax = lParMax
        self.lParValues = lreadings
        print("lParName: ",self.lParName)
        #print("lParUnits: ", self.lParUnits)
        print("lParMin", self.lParMin)
        print("lParMax", self.lParMax)
        self.RemoveParameters()
        self.parCount = iCount
        print("iCount: ", self.parCount)
        self.displayParameters()
        #insertToDaqRecards()
        self.getHealthConditionOfDaq(deviceNumber)
        #self.indicateCurrentDAQinUI(deviceNumber)

    def indicateCurrentDAQinUI(self, iDAQNumber):
        '''for num in range(0,self.deviceCount):
            self.button[num].setStyleSheet("background-color:;")
        self.button[iDAQNumber-1].setStyleSheet("background-color:   #FE9A2E ; border-radius: 6px; ")'''
        for num in range(0,self.deviceCount):
            self.button[num].setStyleSheet("border-color:;")
        self.button[iDAQNumber-1].setStyleSheet("border:2px solid #FE9A2E;")

    def getHealthConditionOfDaq(self, iDAQNumber):
        iParValueslen = len(self.lParValues)
        inrange = True
        print(iDAQNumber-1,self.colorStateOfDev)
        if iDAQNumber <= 1:
            self.button[self.deviceCount-1].setStyleSheet("background-color:#"+self.colorStateOfDev+"; border-color:;")
            print(self.deviceCount-1)
        elif iDAQNumber > 1:
            self.button[iDAQNumber-2].setStyleSheet("background-color:#"+self.colorStateOfDev+";border-color:;")
            print(iDAQNumber-2)
        if iParValueslen > 0:
            for num in range(0,self.parCount):
                if (iParValueslen>0 and iParValueslen>num):
                    if(self.lParMax[num] != self.lParMin[num] ):
                        if(float(self.lParValues[num])< self.lParMin[num] or float(self.lParValues[num]) > self.lParMax[num]):
                            #not With in range
                            print("**readings are not with in the range")#background-color:pink;
                            self.colorStateOfDev = "FFC0CB"
                            self.button[iDAQNumber-1].setStyleSheet("background-color:#FFC0CB;border:2px solid #FE9A2E;")
                            inrange = False
                            break
            if inrange == True :
                print("*readings are with in the range")#background-color:#CEF6CE;
                self.colorStateOfDev = "CEF6CE"
                self.button[iDAQNumber-1].setStyleSheet("background-color:#CEF6CE;border:2px solid #FE9A2E;")
            self.liSuspentionNum[iDAQNumber-1] = 0
        else :
            print("**no Readings")#"background-color: #F7F975;"
            self.colorStateOfDev = "F7F975"
            self.button[iDAQNumber-1].setStyleSheet("background-color:#F7F975;border:2px solid #FE9A2E;")
            self.liSuspentionNum[iDAQNumber-1] += 1
            if self.liSuspentionNum[iDAQNumber-1] > self.iSuspentionCount :
                print("** Device is not working")
                self.colorStateOfDev = "fb587e"
                self.button[iDAQNumber-1].setStyleSheet("background-color:#fb587e;border:2px solid #FE9A2E;")
                self.sDaqStatus[iDAQNumber-1] = 0
        #    iSuspentionCount = 0
        #background-color: #fb587e; colorStateOfDev



    def on_triggered_actionDAQ(self, homePage):
        print("on_triggered_actionDAQ")
        '''DAQSettings = QtWidgets.QMainWindow()
        ui = Ui_DAQSettings()
        ui.setupUi(DAQSettings)
        DAQSettings.show()
        homePage.close()'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homePage = QtWidgets.QMainWindow()
    ui = Ui_homePage()
    ui.setupUi(homePage)
    homePage.show()
    sys.exit(app.exec_())

