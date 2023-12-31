"""
Snowmelt
Analyzes csv files to determine Last Day of Snow and Number of Days of Snow during snow season.
This version works for 2022 HOBOs
Runs through all the .csvs in the folder
Author: Jack DuPuy
Version: 6/23/2022
"""

import sys

def nameOfFile(filename):
    fileName=str(filename).replace(".csv","")
    return(fileName)

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
    # print(listName)
    for i in range(1250): #-1?
    # for i in range(5):
        noEnd=listName[i].replace(",,,,,","")
        timeList=noEnd.split(",")
        # print(timeList[1])
        # print(timeList[1][1])
        if timeList[1].startswith("0") == False and timeList[1][1] == "/":
            timeList[1]="0"+timeList[1]
        # print(timeList[1])
        if timeList[1][3] != "0" and timeList[1][4] == "/":
            timeList[1]=timeList[1][0:3]+"0"+timeList[1][3:]
        # print(timeList[1])
        if timeList[1][6]=="2":
            timeList[1]=timeList[1].replace("2022","22")
            timeList[1]=timeList[1].replace("2021","21")
        if timeList[1].endswith("3:00 AM")==True or timeList[1].endswith("12:36:32 AM")==True or timeList[1].endswith("3:00")==True:
            timeList[1]=timeList[1][0:9]+"0:36"
        if timeList[1].endswith("9:00 AM")==True or timeList[1].endswith("6:36:32 AM")==True or timeList[1].endswith("9:00")==True:
            timeList[1]=timeList[1][0:9]+"6:36"
        if timeList[1].endswith("3:00 PM")==True or timeList[1].endswith("12:36:32 PM")==True or timeList[1].endswith("15:00:00")==True:
            timeList[1]=timeList[1][0:9]+"12:36"
        if timeList[1].endswith("9:00 PM")==True or timeList[1].endswith("6:36:32 PM")==True or timeList[1].endswith("21:00:00")==True:
            timeList[1]=timeList[1][0:9]+"18:36"
        # print(timeList[1])
        # print(timeList[1])
        timeTemp=[]
        if timeList[2] != "" and timeList[2] != "Logged" and timeList[2] != "6+C1060:C1095775":
            timeTemp.append(timeList[1])
            timeTemp.append(timeList[2])
            timeTemps.append(timeTemp)
    return(timeTemps)

def dateIndex(listName):
    #Some are "03", some are "3"--Must include both!
    datesOnly=[]
    for i in range(len(listName)):
        onlyDate=listName[i][0]
        datesOnly.append(onlyDate)
    #print(datesOnly)
    MarTwenty=datesOnly.index('03/21/22 0:36')
    JanFirst=datesOnly.index('01/01/22 0:36')
    idxList=[MarTwenty,JanFirst]
    #print(MarTwenty)
    #print(JanFirst)
    return idxList

def snowDuringPeriod(listName,MarTwenty):
    snowRanges=[]
    listNew=listName[MarTwenty:]
    i=0
    totalSnowCount=0
    while i <= len(listNew):
        snowCount=0
        for j in range(len(listNew)-i):
            if i+j+1 >= len(listNew):
                break
            if float(listNew[i+j][1]) <= 1:
                snowCount=snowCount+1
            else:
                break
        if snowCount >= 4:
            snowRange=[listNew[i][0],listNew[i+snowCount-1][0]]
            snowRanges.append(snowRange)
            totalSnowCount+=snowCount
        if snowCount > 1:
            i=i+snowCount
        else:
            i+=1
    if len(snowRanges) < 1:
        snowRanges=[["NA"],["NA"]]
    #print(listName[0])
    return(snowRanges),totalSnowCount
    #Returns ranges (date and time) with snow, inclusive, after March 20th at 3:00
    #Based on abs. temp. of 0 +- 1 for 8 consecutive time periods
    #Change number in "if snowCount >= 4:" based on how short a time we want to count as snow.

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
    #if len(argv) != 2:
        #print("Usage:\npython3 txtfile.txt")
        #print("You must enter 1 file name to run this program.")
        #sys.exit()

    originaltext=readtxt(fileName)
    untitledtext=removeTitles(originaltext)
    fullList=splitLines(untitledtext)
    timeTemps=timeTemp(fullList)
    dateIdx=dateIndex(timeTemps)
    MarTwenty=dateIdx[0]
    JanFirst=dateIdx[1]
    snowRanges=snowDuringPeriod(timeTemps,MarTwenty)[0]
    totalSnowCount=snowDuringPeriod(timeTemps,MarTwenty)[1]
    if snowRanges==[["NA"],["NA"]]:
        snowRanges=snowDuringPeriod(timeTemps,JanFirst)[0]
        totalSnowCount=0
    totalSnowDays=totalSnowCount//4
    #Just assumes that 4 time periods, whenever they occur, is one day.

    fileName=nameOfFile(fileName)
    print(fileName+","+snowRanges[-1][-1]+","+str(totalSnowDays))
    #for i in range(len(snowRanges)):
    #   print(snowRanges[i][0]+"-"+snowRanges[i][1]+",",end="")
    #print("\n")
    
for file in fileList:
    main(file)
    