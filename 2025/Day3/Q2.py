from itertools import product
from lib2to3.pgen2.token import STRING
import re
from pathlib import Path
import string

input_string = Path("E:\\Repos\\AdventToCode\\2025\\Day3\\Input.txt").read_text()
 
# Use regex to find all numbers in the input string
batteryBanks = re.findall(r'\d+', input_string)

totalOutputJoltage = 0

def ResetBatteryJoltage(i, bList):
    while i < 12:
        bList[i] = 0
        i = i + 1

for bank in batteryBanks:
    totalBatteries = len(bank)
    currentBattery = 0
    batteryList = [0] * 12
    while currentBattery < totalBatteries:
        batteryJoltage = int(bank[currentBattery])

        bI = 0
        while bI < 12:
            if batteryJoltage > batteryList[bI] and currentBattery < (totalBatteries - (11-bI)):
                batteryList[bI] = batteryJoltage
                ResetBatteryJoltage(bI+1, batteryList)
                break
            bI = bI + 1
        currentBattery = currentBattery + 1

    bankJoltageStr = ""
    for battery in batteryList:
        bankJoltageStr = bankJoltageStr + str(battery)
    print(bankJoltageStr)
    totalOutputJoltage = totalOutputJoltage + int(bankJoltageStr)

print(totalOutputJoltage)
