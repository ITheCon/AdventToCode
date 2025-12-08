import re
from pathlib import Path

input_string1 = Path("E:\\Repos\\AdventToCode\\2025\\Day5\\Input.txt").read_text()
input_string2 = Path("E:\\Repos\\AdventToCode\\2025\\Day5\\Input2.txt").read_text()

# Use regex to find all numbers in the input string
idRanges = re.findall(r'\d+-\d+', input_string1)
ingredientIds = re.findall(r'\d+', input_string2)

freshIds = []
freshIngredients = 0

for ingredientId in ingredientIds:
    iId = int(ingredientId)

    for idRange in idRanges:
        startAndStopId = str.split(idRange, '-');
        startId = int(startAndStopId[0])
        stopId = int(startAndStopId[1])

        if startId <= iId and iId <= stopId:
            freshIngredients += 1
            break

print(freshIngredients)