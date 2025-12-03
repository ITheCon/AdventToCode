from itertools import product
from lib2to3.pgen2.token import STRING
import re
from pathlib import Path
import string

input_string = Path("E:\\Repos\\AdventToCode\\2025\\Day2\\InputDod.txt").read_text()
 
# Use regex to find all numbers in the input string
productIds = re.findall(r'\d+-\d+', input_string)

invalidIdTotal = 0

for productId in productIds:
    startAndStopId = str.split(productId, '-');
    startId = int(startAndStopId[0])
    stopId = int(startAndStopId[1])
    currentId = startId
    while currentId <= stopId:
        currentStr = str(currentId)
        strLength = len(currentStr);
        # It can only repeat if string can be cut in half evenly
        if strLength%2 == 1:
            currentId = currentId + 1
            continue
        strHalf = int(strLength/2)
        
        currentStrSplit1 = currentStr[strHalf:]
        currentStrSplit2 = currentStr[:strHalf]
        if currentStrSplit1 == currentStrSplit2:
            invalidIdTotal = invalidIdTotal + currentId

        currentId = currentId + 1

print(invalidIdTotal)