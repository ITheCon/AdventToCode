from itertools import product
from lib2to3.pgen2.token import STRING
import re
from pathlib import Path
import string

input_string = Path("E:\\Repos\\AdventToCode\\2025\\Day3\\Input.txt").read_text()
 
# Use regex to find all numbers in the input string
batteryBanks = re.findall(r'\d+', input_string)

totalOutputJoltage = 0

for bank in batteryBanks:
    totalBatteries = len(bank)
    currentBattery = 0
    battery1 = 0
    battery2 = 0
    while currentBattery < totalBatteries:
        batteryJoltage = int(bank[currentBattery])
        if batteryJoltage > battery1 and currentBattery < (totalBatteries - 1):
            battery1 = batteryJoltage
            battery2 = 0
        elif batteryJoltage > battery2:
            battery2 = batteryJoltage
        currentBattery = currentBattery + 1

    bankJoltage = int(str(battery1)+str(battery2))
    totalOutputJoltage = totalOutputJoltage + bankJoltage

print(totalOutputJoltage)
