#!/usr/bin/python

import sqlite3
from sqlite3 import Error
from PyQt5.QtCore import QDateTime


def Create_DB():
    conn = sqlite3.connect('SmartDAQ.db')
    print ("Opened database successfully")
    #isAppTable = conn.execute('''SELECT name FROM sqlite_master WHERE name=\'table_name\';''')
    #print ("isAppTable: ",isAppTable)

    try:
        conn.execute('''CREATE TABLE AppSettings
         (SrNo INTEGER PRIMARY KEY AUTOINCREMENT,
         ApplicationName    TEXT,
         LogoPath           TEXT,
         Password           TEXT,
         SignaturePath      TEXT,
         NoOfDAQ            INT,
         SwitchingTime      INT,
         SuspemsionCount    INT,
         AutoReport     CHAR,
         MailIds        TEXT,
         MailInterval   INT,
         SMTPserver     TEXT,
         EMailId        TEXT,
         EPassword      TEXT);''')
        print ("AppSettings Table created successfully")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    try:
        conn.execute('''CREATE TABLE DAQSettings
         (SrNo INTEGER PRIMARY KEY AUTOINCREMENT,
         DateTime           TEXT,
         DeviceNumber       INT,
         DeviceName         TEXT,
         IpAddress          TEXT,
         PortNumber         INT,
         isConnected        CHAR,
         StartTime          TEXT,
         StopTime           TEXT);''')
        print ("DAQSettings Table created successfully")
        for num in range(0,50):
            DAQSettingsList = []
            DAQSettingsList.append(QDateTime.currentDateTime().toString())
            DAQSettingsList.append(str(num+1))
            DAQSettingsList.append("DAQ"+str(num+1))
            DAQSettingsList.append("127.0.0.1")
            DAQSettingsList.append(str(23))
            DAQSettingsList.append("0")
            DAQSettingsList.append("00:00")
            DAQSettingsList.append("00:00")
            print(DAQSettingsList)
            insertDAQSettings(DAQSettingsList)
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    try:
        conn.execute('''CREATE TABLE AppColorSettings
         (SrNo INTEGER PRIMARY KEY AUTOINCREMENT,
         Name               TEXT,
         HederColor         TEXT,
         BodyColor          TEXT,
         BackgroundColor    TEXT,
         BackImagePath      TEXT,
         TextColor          TEXT,
         Font               INT,
         TextStyle          TEXT,
         TextBGColor        TEXT);''')
        print ("AppColorSettings Table created successfully")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    try:
        conn.execute('''CREATE TABLE ParametterSettings
         (SrNo INTEGER PRIMARY KEY AUTOINCREMENT,
         DaqNumber          INT,
         ParNumber          INT,
         ParametterName     TEXT,
         units              TEXT,
         Visibility         CHAR,
         Controllable       CHAR,
         MinThreshold       DOUBLE,
         MaxThreshold       DOUBLE,
         Sequance           INT);''')
        print ("ParametterSettings Table created successfully")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    try:
        conn.execute('''CREATE TABLE DaqRecards
         (SrNo INTEGER PRIMARY KEY AUTOINCREMENT,
         DaqNumber          INT,
         DaqName            TEXT,
         DateTime     	    TEXT,
         Par1Value          DOUBLE,
         Par2Value          DOUBLE,
         Par3Value          DOUBLE,
         Par4Value          DOUBLE,
         Par5Value          DOUBLE,
         Par6Value          DOUBLE,
         Par7Value          DOUBLE,
         Par8Value          DOUBLE,
         Par9Value          DOUBLE,
         Par10Value          DOUBLE,
         Par11Value          DOUBLE,
         Par12Value          DOUBLE,
         Par13Value          DOUBLE,
         Par14Value          DOUBLE,
         Status       CHAR);''')
        print ("DaqRecards Table created successfully")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    #isAppTable = conn.execute('''SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'AppSettings\';''')
    #print ("isAppTable: ",isAppTable)
    conn.close()


def insertToDaqRecards(listDaq):
    '''countArg=len(listDaq)
    isUpdated =False
    if (countArg >=4 ):
            strInsert = "INSERT INTO DaqRecards (DaqNumber, DaqName, DateTime, \
Par1Value, Par2Value, Par3Value, Par4Value, Par5Value, Par6Value, Par7Value, \
Par8Value, Par9Value, Par10Value, Par11Value, Par12Value, Par13Value, Par14Value, Status) \
VALUES ('"+listDaq[0]+"', '"+listDaq[1]+"','"+listDaq[2]+"','"+listDaq[3]+"')"
            #print(strInsert)
        conn = sqlite3.connect('SmartDAQ.db')
        try :
            conn.execute(strInsert);
            conn.commit()
            print ("Records Updated AppSettings Table")
            isUpdated=True
        except sqlite3.Error as e:
            print ("Database error: {}".format(e))
        conn.close()
    return isUpdated'''


def insertToAppSettings(listApp):
    countArg=len(listApp)
    isUpdated =False
    if (countArg >=4 ):
        listSet = selectFromAppSettings()
        if( len(listSet) > 0):
            strInsert = "UPDATE AppSettings SET ApplicationName = '"+listApp[0]+"', \
LogoPath = '"+listApp[1]+"', Password = '"+listApp[2]+"', SignaturePath ='"+listApp[3]+"' where SrNo = 1"
            #print(strInsert)
        else :
            strInsert = "INSERT INTO AppSettings (ApplicationName, LogoPath, \
Password, SignaturePath) \
VALUES ('"+listApp[0]+"', '"+listApp[1]+"','"+listApp[2]+"','"+listApp[3]+"')"
            #print(strInsert)
        conn = sqlite3.connect('SmartDAQ.db')
        try :
            conn.execute(strInsert);
            conn.commit()
            print ("Records Updated AppSettings Table")
            isUpdated=True
        except sqlite3.Error as e:
            print ("Database error: {}".format(e))
        conn.close()
    return isUpdated

def insertToOperationSettings(listApp):
    countArg=len(listApp)
    isUpdated =False
    if (countArg >=5 ):
        listSet = selectFromAppSettings()
        if( len(listSet) > 0):
            strInsert = "UPDATE AppSettings SET NoOfDAQ = "+listApp[0]+", \
SwitchingTime = "+listApp[1]+", SuspemsionCount = "+listApp[2]+", AutoReport = \
"+listApp[3]+", MailIds = '"+listApp[4]+"', MailInterval = "+listApp[5]+"  where SrNo = 1"
            #print(strInsert)
        else :
            strInsert = "INSERT INTO AppSettings (NoOfDAQ, SwitchingTime, \
SuspemsionCount, AutoReport, MailIds, MailInterval) \
VALUES ("+listApp[0]+","+listApp[1]+","+listApp[2]+","+listApp[3]+",'"+listApp[4]+"',\
"+listApp[5]+")"
            #print(strInsert)
        conn = sqlite3.connect('SmartDAQ.db')
        try :
            conn.execute(strInsert);
            conn.commit()
            print ("Records Updated Operation settings Table")
            isUpdated=True
        except sqlite3.Error as e:
            print ("Database error: {}".format(e))
        conn.close()
    return isUpdated

def insertToSmtpSettings(listApp):
    countArg=len(listApp)
    isUpdated =False
    if (countArg >=3 ):
        listSet = selectFromAppSettings()
        print(len(listSet))
        if( len(listSet) > 0):
            strInsert = "UPDATE AppSettings SET SMTPserver = '"+listApp[0]+"', \
EMailId = '"+listApp[1]+"', EPassword = '"+listApp[2]+"' where SrNo = 1"
            #print(strInsert)
        else :
            strInsert = "INSERT INTO AppSettings (SMTPserver, EMailId, EPassword) \
VALUES ('"+listApp[0]+"', '"+listApp[1]+"','"+listApp[2]+"')"
            #print(strInsert)
        conn = sqlite3.connect('SmartDAQ.db')
        try :
            conn.execute(strInsert);
            conn.commit()
            print ("Records Updated to SMTP settings")
            isUpdated=True
        except sqlite3.Error as e:
            print ("Database error: {}".format(e))
        conn.close()
    return isUpdated


def selectFromAppSettings():
    argList=[]
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT * from AppSettings where SrNo = 1"

    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            for record in row:
                if str(record) != "None" :
                    argList.append(str(record))
                else :
                    argList.append("")
        print ("Records selected from AppSettings")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return argList

def selectFromOperationSettings():
    argList=[]
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT SwitchingTime,SuspemsionCount from AppSettings where SrNo = 1"

    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            for record in row:
                if str(record) != "None" :
                    argList.append(str(record))
                else :
                    argList.append("")
        print ("Records selected from AppSettings")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return argList


def getNoOfDAQs():
    noOfDev = 0
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT NoOfDAQ from AppSettings where SrNo = 1"

    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            for record in row:
                if(record != None):
                    noOfDev = int(str(record))
        print(noOfDev)
        print ("Records selected from AppSettings")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return noOfDev

def updateAppSettings(AppSettingsList):
    print(AppSettingsList)
    return insertToAppSettings(AppSettingsList)

def updateOperationSettings(OpSettingsList):
    print(OpSettingsList)
    return insertToOperationSettings(OpSettingsList)

def updateSmtpSettings(SmtpSettingsList):
    print(SmtpSettingsList)
    return insertToSmtpSettings(SmtpSettingsList)

#DAQ Settings

def insertDAQSettings(DAQSettingsList):
    countArg=len(DAQSettingsList)
    isUpdated =False
    if (countArg >=8 ):
        listSet = getDAQSettings(DAQSettingsList[1])
        print(len(listSet))
        if( len(listSet) > 0):
            strInsert = "UPDATE DAQSettings SET DateTime = '"+DAQSettingsList[0]+"', \
DeviceName = '"+DAQSettingsList[2]+"', IpAddress = '"+DAQSettingsList[3]+"', \
PortNumber = "+DAQSettingsList[4]+", isConnected = "+DAQSettingsList[5]+", StartTime = '"+DAQSettingsList[6]+"', \
StopTime = '"+DAQSettingsList[7]+"' where DeviceNumber == "+DAQSettingsList[1]
        else :
            strInsert = "INSERT INTO DAQSettings (DateTime, DeviceNumber, DeviceName, \
IpAddress, PortNumber, isConnected, StartTime, StopTime) \
VALUES ('"+DAQSettingsList[0]+"',"+DAQSettingsList[1]+",'"+DAQSettingsList[2]+"','"+DAQSettingsList[3]+"',\
"+DAQSettingsList[4]+","+DAQSettingsList[5]+",'"+DAQSettingsList[6]+"','"+DAQSettingsList[7]+"')"
        conn = sqlite3.connect('SmartDAQ.db')
        try :
            conn.execute(strInsert);
            conn.commit()
            print ("Records Updated to Daq settings devNo: "+str(DAQSettingsList[1]))
            isUpdated=True
        except sqlite3.Error as e:
            print ("Database error: {}".format(e))
        conn.close()
    return isUpdated

def getDAQSettings(deviceNumber):
    argList=[]
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT * from DAQSettings where DeviceNumber = "+str(deviceNumber)

    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            for record in row:
                argList.append(str(record))
        #print ("Records device details from DAQSettings")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return argList

def getDaqNames():
    argList=[]
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT DeviceNumber, DeviceName from DAQSettings"

    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            #for record in row:
            argList.append(row)
        #print("argList",argList)
        print ("Records selected from AppSettings")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return argList

def getDaqNamesfromList():
    argList=[]
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT DeviceName from DAQSettings"

    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            for record in row:
                argList.append(record)
        #print("argList",argList)
        print ("Records selected from AppSettings")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return argList

def getDaqIpfromList():
    argList=[]
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT IpAddress from DAQSettings"

    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            for record in row:
                argList.append(record)
        #print("argList",argList)
        print ("Records selected from AppSettings")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return argList

def getPortNumberfromList():
    argList=[]
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT PortNumber from DAQSettings"

    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            for record in row:
                argList.append(record)
        #print("argList",argList)
        print ("Records selected from AppSettings")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return argList

def validateDaqNames(daqName, isAddOrEdit):
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = ""
    if isAddOrEdit == False :
        strSelect = "SELECT DeviceNumber, DeviceName from DAQSettings"
    else :
        strSelect = "SELECT DeviceNumber, DeviceName from DAQSettings where DeviceName != "+daqName+""
    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            for record in row:
                if isinstance(record, str):
                    if record == daqName:
                        return False
        #print("argList",argList)
        print ("Records selected from AppSettings")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return True

def updateDAQSettings(DAQSettingsList):
    print(DAQSettingsList)
    return insertDAQSettings(DAQSettingsList)

def deleteDAQsettingsFrom(DeviceNumber):
    isDeleted = False
    conn = sqlite3.connect('SmartDAQ.db')
    strDelete = "DELETE FROM DAQSettings WHERE DAQSettings.DeviceNumber > "+str(DeviceNumber)+""
    print(strDelete)
    try:
        conn.execute(strDelete);
        isDeleted = True
        print ("Records deleted from DAQ settings")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return isDeleted

#App Color/Design Settings

def insertToAppColorsettings(listApp):
    countArg=len(listApp)
    isUpdated =False
    if (countArg >=9 ):
        listSet = getAppColorSettings()
        if( len(listSet) > 0):
            strInsert = "UPDATE AppColorSettings SET Name = '"+listApp[0]+"', \
HederColor = '"+listApp[1]+"', BodyColor = '"+listApp[2]+"', BackgroundColor = \
'"+listApp[3]+"', BackImagePath = '"+listApp[4]+"', TextColor = '"+listApp[5]+"' \
, Font = "+listApp[6]+", TextStyle = '"+listApp[7]+"', TextBGColor = '"+listApp[8]+"' where SrNo = 1"
        else :
            strInsert = "INSERT INTO AppColorSettings (Name, HederColor, BodyColor, \
BackgroundColor, BackImagePath, TextColor, Font, TextStyle, TextBGColor) \
VALUES ('"+listApp[0]+"','"+listApp[1]+"','"+listApp[2]+"','"+listApp[3]+"','"+listApp[4]+"',\
'"+listApp[5]+"',"+listApp[6]+",'"+listApp[7]+"','"+listApp[8]+"')"
        conn = sqlite3.connect('SmartDAQ.db')
        try :
            print(strInsert)
            conn.execute(strInsert);
            conn.commit()
            print ("Records Updated to Color settings Table")
            isUpdated=True
        except sqlite3.Error as e:
            print ("Database error: {}".format(e))
        conn.close()
    return isUpdated

def getAppColorSettings():
    argList=[]
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT * from AppColorSettings"
    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            for record in row:
                if str(record) != "None" :
                    argList.append(str(record))
                else :
                    argList.append("")
        print ("App Color Settings details from Table")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))
    conn.close()
    return argList

#Parameter settings
'''CREATE TABLE ParametterSettings
         (SrNo INTEGER PRIMARY KEY AUTOINCREMENT,
         DaqNumber          INT,
         ParNumber          INT,
         ParametterName     TEXT,
         units              TEXT,
         Visibility         CHAR,
         Controllable       CHAR,
         MinThreshold       DOUBLE,
         MaxThreshold       DOUBLE,
         Sequance           INT);'''

def updateParSettings(listApp):
    countArg=len(listApp)
    isUpdated =False
    if (countArg >=9 ):
        listSet = getParameterSettings(listApp[0],listApp[1])
        if( len(listSet) > 0):
            strInsert = "UPDATE ParametterSettings SET ParametterName = '"+listApp[2]+"', units = \
'"+listApp[3]+"', Visibility = "+listApp[4]+", Controllable  = "+listApp[5]+", MinThreshold = "+listApp[6]+", MaxThreshold = \
"+listApp[7]+", Sequance = "+listApp[8]+" where DaqNumber == "+listApp[0]+" and ParNumber = "+listApp[1]+""
        else :
            strInsert = "INSERT INTO ParametterSettings (DaqNumber, ParNumber, ParametterName, \
units, Visibility, Controllable, MinThreshold, MaxThreshold, Sequance) \
VALUES ("+listApp[0]+","+listApp[1]+",'"+listApp[2]+"','"+listApp[3]+"',"+listApp[4]+",\
"+listApp[5]+","+listApp[6]+","+listApp[7]+","+listApp[8]+")"
        conn = sqlite3.connect('SmartDAQ.db')
        try :
            print(strInsert)
            conn.execute(strInsert);
            conn.commit()
            print ("Records Updated to parameter settings Table")
            isUpdated=True
        except sqlite3.Error as e:
            print ("Database error: {}".format(e))
        conn.close()
    return isUpdated

def getParSettings(deviceNumber):
    argList=[]
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT ParametterName, units, Visibility, Controllable, MinThreshold, MaxThreshold, Sequance \
from ParametterSettings where DaqNumber == "+str(1)+" ORDER BY ParNumber ASC"
    print(strSelect)
    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            #for record in row:
            argList.append(row)
        #print("argList",argList)
        print ("Records selected from getParSettings")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return argList

def getParameterSettings(deviceNumber, ParNumber):
    argList=[]
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT ParNumber, ParametterName, units, Visibility, Controllable, MinThreshold, MaxThreshold, \
Sequance from ParametterSettings where DaqNumber == "+str(deviceNumber)+" and ParNumber == "+str(ParNumber)+""

    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            #for record in row:
            argList.append(row)
        #print("argList",argList)
        print ("Records selected from getParSettings")
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return argList

def getParNumber(deviceNumber):
    iParNumber = 0
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT MAX(ParNumber) from ParametterSettings where DaqNumber == "+str(deviceNumber)+""

    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            for record in row:
                if record != None:
                    iParNumber = record
        #print("argList",argList)
        print ("Records selected from getParNumber", iParNumber)
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return iParNumber

def getSeqNumber(deviceNumber):
    iSeqNumber = 0
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT MAX(Sequance) from ParametterSettings where DaqNumber == "+str(deviceNumber)+""

    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            for record in row:
                if record != None:
                    iSeqNumber = record
        #print("argList",argList)
        print ("Records selected from getSeqNumber", iSeqNumber)
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return iSeqNumber


def getParNumberWithseq(deviceNumber,seqNumber):
    iParNumber = 0
    conn = sqlite3.connect('SmartDAQ.db')
    strSelect = "SELECT ParNumber from ParametterSettings where DaqNumber == "+str(deviceNumber)+" \
and Sequance == "+str(seqNumber)+""

    try:
        cursor = conn.execute(strSelect);
        for row in cursor:
            for record in row:
                if record != None:
                    iParNumber = record
        #print("argList",argList)
        print ("Records selected from getParNumber", iParNumber)
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))

    conn.close()
    return iParNumber

def updateSeqNumber(deviceNumber, parNumber, seqNumber):
    isUpdated =False
    strInsert = "UPDATE ParametterSettings SET Sequance = "+str(seqNumber)+" \
where DaqNumber == "+str(deviceNumber)+" and ParNumber = "+str(parNumber)+""
    conn = sqlite3.connect('SmartDAQ.db')
    try :
        print(strInsert)
        conn.execute(strInsert);
        conn.commit()
        print ("Records Updated to parameter settings Table")
        isUpdated=True
    except sqlite3.Error as e:
        print ("Database error: {}".format(e))
    conn.close()
    return isUpdated
