"""
Snow Ranges
Prints 0 for no snow, 1 for snow
Copy/paste to create CSV
May be used to compare HOBOs to Cameras

Author: Charles Mullis
Version: 6/29/2020
"""

def nocsv(filename):
    filenocsv=str(filename).replace(".csv","")
    return(filenocsv)

def readtxt(filename):
    txtStr = str((open(filename)).read())
    return txtStr

def removeTitles(stringName):
    #Assumes title/headers are first two lines.
    #Removes first two lines.
    untitled="\n".join(stringName.split("\n")[2:])
    return untitled

def splitLines(stringName):
    fullList=stringName.splitlines()
    return fullList

def timeTemp(listName):
    timeTemps=[]
    timeTempsWithYear=[]
    for i in range(len(listName)): #-1?
        noEnd=listName[i].replace(",,,,,","")
        timeList=noEnd.split(",")
        #print(timeList)
        if len(timeList) < 2 or len(timeList[1]) < 2:
            return timeTemps, timeTempsWithYear
        if timeList[1].startswith("0") == False and timeList[1][1] == "/":
            timeList[1]="0"+timeList[1]
        #print(timeList[1])
        if timeList[1][3] != "0" and timeList[1][4] == "/":
            timeList[1]=timeList[1][0:3]+"0"+timeList[1][3:]
        #print(timeList[1])
        if timeList[1][6]=="2":
            slashyear=timeList[1][5:8]
            realslashyear=slashyear[0]+slashyear[3:]
            #print('1', slashyear)
            timeList[1]=timeList[1].replace(slashyear,"")
        elif timeList[1][5]=="/":
            slashyear=timeList[1][5:8]
            realslashyear=slashyear
            #print("2", slashyear)
            timeList[1]=timeList[1].replace(slashyear,"")
        if timeList[1].endswith("12:36 AM")==True or timeList[1].endswith("12:36:32 AM")==True or timeList[1].endswith("0:36")==True:
            timeList[1]=timeList[1][0:6]+"00:36"
        if timeList[1].endswith("6:36 AM")==True or timeList[1].endswith("6:36:32 AM")==True or timeList[1].endswith("6:36")==True:
            timeList[1]=timeList[1][0:6]+"06:36"
        if timeList[1].endswith("12:36 PM")==True or timeList[1].endswith("12:36:32 PM")==True or timeList[1].endswith("12:36")==True:
            timeList[1]=timeList[1][0:6]+"12:36"
        if timeList[1].endswith("6:36 PM")==True or timeList[1].endswith("6:36:32 PM")==True or timeList[1].endswith("18:36")==True:
            timeList[1]=timeList[1][0:6]+"18:36"
        #print(timeList[1])
        #print(timeList[1])
        timeTemp=[]
        timeTempWithYear=[]
        if timeList[2] != "" and timeList[2] != "Logged" and timeList[2] != "6+C1060:C1095775":
            timeTempWithYear.append(timeList[1][0:5]+realslashyear+timeList[1][5:])
            timeTempWithYear.append(timeList[2])
            timeTemp.append(timeList[1])
            timeTemp.append(timeList[2])
            timeTemps.append(timeTemp)
            timeTempsWithYear.append(timeTempWithYear)
    return timeTemps, timeTempsWithYear

def dateIndex(listName):
    #Some are "03", some are "3"--Must include both!
    datesOnly=[]
    for i in range(len(listName)):
        onlyDate=listName[i][0]
        datesOnly.append(onlyDate)
    #print(datesOnly)
    MarTwenty=datesOnly.index('03/21 00:36')
    JanFirst=datesOnly.index('01/01 00:36')
    OctFirst=datesOnly.index('10/16 00:36')
    idxList=[MarTwenty,JanFirst,OctFirst]
    #print(MarTwenty)
    #print(JanFirst)
    return idxList

def snowNoSnow(listName,MarTwenty):
    BackZeroOne=[]
    listNew=listName[MarTwenty:]
    # print(listNew)
    for i in range(len(listNew)):
        BackSnow=True
        #print(listNew[i])
        if float(listNew[i][1]) <= 1:
            for j in range(4):
                if float(listNew[i-j][1]) > 1:
                    BackSnow=False
            if BackSnow==True:
                BackZeroOne.append(1)
                #print("True")
            else:
                BackZeroOne.append(0)
                #print("False")
        else:
            BackZeroOne.append(0)
    ForwardZeroOne=[]
    for i in range(len(listNew)):
        ForwardSnow=True
        #print(listNew[i])
        if listNew[i][0][6:8] == "16":
            ForwardZeroOne.append(2016)
        else:
            if float(listNew[i][1]) <= 1:
            #print("VALUE LESS THAN 1")
                for j in range(4):
                    if float(listNew[i+j][1]) > 1:
                        ForwardSnow=False
                if ForwardSnow==True:
                    ForwardZeroOne.append(1)
                    #print("True")
                else:
                    ForwardZeroOne.append(0)
                    #print("False")
            else:
                ForwardZeroOne.append(0)
    FinalZeroOne = []
    for i in range(len(listNew)):
        if ForwardZeroOne[i] == 1 or BackZeroOne[i] == 1:
            FinalZeroOne.append(1)
        else:
            FinalZeroOne.append(0)
    return FinalZeroOne, listNew
            

def listFiles():
    import os
    fileList=[]
    for file in os.listdir():
        if file.endswith(".csv"):
            fileList.append(file)
    #fileList=os.listdir()
    #print(fileList)
    return(fileList)
            
fileList=listFiles()


def main(fileName):
    fileList=listFiles()
    originaltext=readtxt(fileName)
    untitledtext=removeTitles(originaltext)
    fullList=splitLines(untitledtext)
    #print(untitledtext)
    #print(fullList)
    timeTemps=timeTemp(fullList)[0]
    timeTempsWithYear=timeTemp(fullList)[1]
    filenocsv=nocsv(fileName)
    #print(timeTemps)
    dateIdx=dateIndex(timeTemps)
    MarTwenty=dateIdx[0]
    JanFirst=dateIdx[1]
    OctFirst=dateIdx[2]
    ZeroOne=snowNoSnow(timeTempsWithYear,OctFirst)[0]
    timeTempsinRange=snowNoSnow(timeTempsWithYear,OctFirst)[1]
    #print(ZeroOne)
    timesYN=[]
    for i in range(len(timeTempsinRange)):
        timeYN=[]
        timeYN.append(timeTempsinRange[i][0])
        timeYN.append(ZeroOne[i])
        timesYN.append(timeYN)
    #print(timesYN)
    print("----------"+filenocsv+"----------")
    NineList = []
    for i in range(len(timesYN)):
        #print(str(timesYN[i][0])+","+str(timesYN[i][1]))
        #print(timesYN[i])
        if timesYN[i][0].endswith("06:36")==True:
            NineList.append(timesYN[i][1])
        if timesYN[i][0].endswith("03/21/ 00:36"):
            NineList.append("This is the beginning of the snow season")
        if timesYN[i][0].endswith("06/30/ 12:36"):
            NineList.append("This is the end of the snow season")
    print("9:00 YN Values for File: " + filenocsv)
    print(*NineList, sep="\n")

for file in fileList:
    main(file)
