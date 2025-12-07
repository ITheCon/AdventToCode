import re
from pathlib import Path

input_string = Path("E:\\Repos\\AdventToCode\\2025\\Day4\\Input.txt").read_text()
 
# Use regex to find all numbers in the input string
rollRows = re.findall(r'(.+)', input_string)

def NearbyRoll(rollrows, j,i, y, x):
    try:
        if (j + y) < 0 or (i + x) < 0:
            return 0
        if (rollrows[j +   y])[i +   x] == '@':
            return 1
        return 0
    except:
        return 0

accesibleRolls = 0
j = 0
while j < len(rollRows):
    rollRows[j] = [char for char in rollRows[j]]
    j += 1

j = 0
while j < len(rollRows):
    redo = False
    i = 0
    while i < len(rollRows[j]):
        nearbyRolls = 0
        if rollRows[j][i] == '@':
            #                           1                            2                             3                               4                           5                            6                             7                              8
            nearbyRolls += NearbyRoll(rollRows, j, i, 1, 0) + NearbyRoll(rollRows, j, i, 1, 1) + NearbyRoll(rollRows, j, i, 0, 1) + NearbyRoll(rollRows, j, i, 0, -1) + NearbyRoll(rollRows, j, i, -1, 0) + NearbyRoll(rollRows, j, i, -1, -1) + NearbyRoll(rollRows, j, i, 1, -1) + NearbyRoll(rollRows, j, i, -1, 1)
            if nearbyRolls < 4:
                accesibleRolls += 1
                rollRows[j][i] = 'X'
                j = 0
        i += 1
    j += 1

print(accesibleRolls)