from itertools import product
from lib2to3.pgen2.token import STRING
import re
import math
from pathlib import Path
import string

input_string = Path("E:\\Repos\\AdventToCode\\2025\\Day2\\Input.txt").read_text()
 
# Use regex to find all numbers in the input string
productIds = re.findall(r'\d+-\d+', input_string)

invalidIdTotal = 0

def AddIdTotal(value):
    global invalidIdTotal
    invalidIdTotal = invalidIdTotal + value

def checkRepeats(strGroups):
    i = 1
    while i < len(strGroups):
        if strGroups[i-1] != strGroups[i]:
            break
        if i == len(strGroups) - 1:
            print(currentId)
            AddIdTotal(currentId)
            return True
        i = i + 1
    return False

for productId in productIds:

    # Segment out to start and stop of range of id's
    startAndStopId = str.split(productId, '-');
    startId = int(startAndStopId[0])
    stopId = int(startAndStopId[1])

    # Start iterating between all the id's
    currentId = startId
    while currentId <= stopId:
        
        currentStr = str(currentId)
        strLength = len(currentStr)

        if strLength == 1:
            None
        else:
            # It can only repeat single digits if id string length is a prime
            if checkRepeats(currentStr):
                currentId = currentId + 1
                continue

            if strLength%2 == 0:
                pattern = re.compile(".{"+str(int(strLength/2))+"}")
                splitSegments = re.findall(pattern, currentStr)
                if checkRepeats(splitSegments):
                    currentId = currentId + 1
                    continue
            elif strLength%3 == 0:
                pattern = re.compile(".{"+str(int(strLength/3))+"}")
                splitSegments = re.findall(pattern, currentStr)
                if checkRepeats(splitSegments):
                    currentId = currentId + 1
                    continue

            if strLength == 6 or strLength == 8 or strLength == 10:
                splitSegments = re.findall(r'.{2}', currentStr)
                checkRepeats(splitSegments)

        currentId = currentId + 1

print("Total: "+ str(invalidIdTotal))