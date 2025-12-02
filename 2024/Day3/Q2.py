
from pathlib import Path
reports  = []
 
import re
from pathlib import Path

input_string = Path("E:\\Repos\\AdventToCode\\Day3\\Input.txt").read_text()

patterns = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)|don\'(t)\(\)|(d)o\(\)', input_string)

sum = 0
do = True
for pattern in patterns:
    if pattern[3] == 'd':
        do = True
    elif pattern[2] == 't':
        do = False
    elif do:
        sum += int(pattern[0])*int(pattern[1])

print (sum)