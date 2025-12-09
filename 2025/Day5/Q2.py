import re
from pathlib import Path

input_string = Path("E:\\Repos\\AdventToCode\\2025\\Day5\\Input.txt").read_text()

# Use regex to find all numbers in the input string
idRanges = re.findall(r'\d+-\d+', input_string)

freshRanges = []
freshIngredientIds = 0

for idRange in idRanges:
    startAndStopId = str.split(idRange, '-');
    startId = int(startAndStopId[0])
    stopId = int(startAndStopId[1])

    start = startId
    stop = stopId

    currentRange = []
    currentRange.append(startId)
    currentRange.append(stopId)

    rangeExists = False
    for freshRange in freshRanges:
        if freshRange[0] <= startId and stopId <= freshRange[1]:
            start = 1
            stop = 0
            rangeExists = True
            break
        elif freshRange[0] <= startId and startId <= freshRange[1]:
            start = freshRange[1] + 1
            freshRange[1] = stopId
            rangeExists = True
        elif freshRange[0] <= stopId and stopId <= freshRange[1]:
            stop = freshRange[0] - 1
            freshRange[0] = startId
            rangeExists = True

    if rangeExists == False:
        freshRanges.append(currentRange)

    if stop - start == 0:
        rangeToAdd = 0
    else:
        rangeToAdd = stop - start + 1
    print(rangeToAdd)

    freshIngredientIds += rangeToAdd


print(freshIngredientIds)