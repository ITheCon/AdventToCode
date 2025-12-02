
from pathlib import Path
reports  = []
 
import re
from pathlib import Path

input_string = Path("E:\\Repos\\AdventToCode\\Day3\\Input.txt").read_text()

multis = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input_string)

sum = 0;
for multi in multis:
    sum += int(multi[0])*int(multi[1])

print (sum)