import re
from pathlib import Path

input_string = Path("E:\\Repos\\AdventToCode\\2025\\Day1\\Input.txt").read_text()
 
# Use regex to find all numbers in the input string
turns = re.findall(r'(.+)\n', input_string)

totalDialNumbers = 100
dialIndex = 50

amountZeroed = 0

def incrementZeroed(increment):
    global amountZeroed
    amountZeroed = amountZeroed + increment
    
def turnDial(turnValue):
    global dialIndex
    if turnValue > 0:
        dialIndex = dialIndex + 1
        turnValue = turnValue - 1
    elif turnValue < 0:
        dialIndex = dialIndex - 1
        turnValue = turnValue + 1
    else:
        return
    dialIndex = dialIndex%totalDialNumbers
    if dialIndex == 0:
        incrementZeroed(1)
    turnDial(turnValue)

for turn in turns:
    turnDirection = turn[:1];
    turnAmount = turn[1:]

    turnAmountQuotient = int(turnAmount)//totalDialNumbers
    if turnAmountQuotient > 0:
        incrementZeroed(turnAmountQuotient)

    turnAmountRemainder = int(turnAmount)%totalDialNumbers
    
    if turnDirection == 'R':
        turnDial(turnAmountRemainder)
    else:
        turnDial(-turnAmountRemainder)

print(amountZeroed)