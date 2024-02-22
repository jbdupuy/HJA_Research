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
        if timeList[1].startswith("0") == False and timeList[1][1] == "/":
            timeList[1]="0"+timeList[1]
        #print(timeList[1])
        if timeList[1][3] != "0" and timeList[1][4] == "/":
            timeList[1]=timeList[1][0:3]+"0"+timeList[1][3:]
        #print(timeList[1])
        if timeList[1][6]=="2":
            slashyear=timeList[1][5:10]
            realslashyear=slashyear[0]+slashyear[3:]
            #print(slashyear)
            timeList[1]=timeList[1].replace(slashyear,"")
        elif timeList[1][5]=="/":
            slashyear=timeList[1][5:8]
            realslashyear=slashyear
            #print(slashyear)
            timeList[1]=timeList[1].replace(slashyear,"")
        if timeList[1].endswith("3:00 AM")==True or timeList[1].endswith("3:00:00 AM")==True or timeList[1].endswith("3:00")==True:
            timeList[1]=timeList[1][0:6]+"03:00"
        if timeList[1].endswith("9:00 AM")==True or timeList[1].endswith("9:00:00 AM")==True or timeList[1].endswith("9:00")==True:
            timeList[1]=timeList[1][0:6]+"09:00"
        if timeList[1].endswith("3:00 PM")==True or timeList[1].endswith("3:00:00 PM")==True or timeList[1].endswith("15:00:00")==True:
            timeList[1]=timeList[1][0:6]+"15:00"
        if timeList[1].endswith("9:00 PM")==True or timeList[1].endswith("9:00:00 PM")==True or timeList[1].endswith("21:00:00")==True:
            timeList[1]=timeList[1][0:6]+"21:00"
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
    MarTwenty=datesOnly.index('03/21 03:00')
    JanFirst=datesOnly.index('02/10 03:00')
    OctFirst=datesOnly.index('02/08 03:00')
    idxList=[MarTwenty,JanFirst,OctFirst]
    #print(MarTwenty)
    #print(JanFirst)
    return idxList

def snowNoSnow(listName,MarTwenty):
    ZeroOne=[]
    listNew=listName[MarTwenty:]
    # print(listNew)
    for i in range(len(listNew)):
        Snow=True
        # print("hello there")
        # print(listNew[i][1])
        # print("general greiviousi")
        if float(listNew[i][1]) <= 1:
            for j in range(4):
                # print(listNew[i+j][1])
                if float(listNew[i+j][1]) > 1:
                    Snow=False
            if Snow==True:
                ZeroOne.append(1)
                # print("True")
            else:
                ZeroOne.append(0)
                # print("False")
        else:
            ZeroOne.append(0)
    return ZeroOne, listNew
            

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
    for i in range(len(timesYN)):
        print(str(timesYN[i][0])+","+str(timesYN[i][1]))

for file in fileList:
    main(file)
