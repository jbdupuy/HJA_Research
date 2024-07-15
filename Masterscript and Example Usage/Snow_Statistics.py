import os
import csv
from datetime import datetime, timedelta

# Set the month and day for the start of the snow season here
START_MONTH = 3
START_DAY = 21

def nameOfFile(filename):
    return filename.replace(".csv", "")

def readtxt(filename):
    with open(filename, 'r') as file:
        return file.read()

def removeTitles(stringName):
    return "\n".join(stringName.split("\n")[2:])

def splitLines(stringName):
    return stringName.splitlines()

def parse_datetime(date_str):
    formats = ["%m/%d/%Y %I:%M:%S %p", "%m/%d/%Y %H:%M", "%m/%d/%y %I:%M:%S %p", "%m/%d/%y %H:%M"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

def timeTemp(listName):
    timeTemps = []
    for line in listName:
        timeList = line.split(",")
        time_str = timeList[1].strip()
        temp = timeList[2].strip()
        datetime_obj = parse_datetime(time_str)
        if not datetime_obj:
            continue
        try:
            temp_value = float(temp)
        except ValueError:
            continue
        timeTemps.append([datetime_obj, temp_value])
    return timeTemps

def getStartDate(listName):
    earliest_date = listName[0][0]
    start_date = datetime(earliest_date.year, START_MONTH, START_DAY)
    if start_date < earliest_date:
        start_date = datetime(earliest_date.year + 1, START_MONTH, START_DAY)
    return start_date

def getDateIndex(listName, start_date):
    for i, record in enumerate(listName):
        if record[0] >= start_date:
            return i
    return -1

def snowDuringPeriod(listName, start_index):
    snowRanges = []
    listNew = listName[start_index:]
    i = 0
    totalSnowCount = 0
    while i < len(listNew):
        snowCount = 0
        for j in range(len(listNew) - i):
            if i + j + 1 >= len(listNew):
                break
            if -1 <= listNew[i + j][1] <= 1:
                snowCount += 1
            else:
                break
        if snowCount >= 4:
            snowRange = [listNew[i][0], listNew[i + snowCount - 1][0]]
            snowRanges.append(snowRange)
            totalSnowCount += snowCount
        i += max(snowCount, 1)
    if not snowRanges:
        snowRanges = [["NA"], ["NA"]]
    return snowRanges, totalSnowCount

def listFiles():
    return [file for file in os.listdir() if file.endswith(".csv")]

def main(fileName):
    originaltext = readtxt(fileName)
    untitledtext = removeTitles(originaltext)
    fullList = splitLines(untitledtext)
    timeTemps = timeTemp(fullList)
    
    if not timeTemps:
        print(f"No valid data in {fileName}")
        return
    
    start_date = getStartDate(timeTemps)
    start_index = getDateIndex(timeTemps, start_date)
    if start_index == -1:
        print(f"No data starting from {start_date} in {fileName}")
        return
    
    snowRanges, totalSnowCount = snowDuringPeriod(timeTemps, start_index)
    totalSnowDays = totalSnowCount // 4
    
    fileName = nameOfFile(fileName)
    print(f"{fileName},{snowRanges[-1][-1] if snowRanges != [['NA'], ['NA']] else 'NA'},{totalSnowDays}")

if __name__ == "__main__":
    fileList = listFiles()
    for file in fileList:
        main(file)
