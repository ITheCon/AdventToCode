import re
from pathlib import Path

input_string = Path("E:\\Repos\\AdventToCode\\2025\\Day1\\Input.txt").read_text()

lines = re.findall(r'.+', input_string)

def is_xmas(lines, j,i, y, x):
    try:
        if (lines[j])[i] != 'X':
            return 0
        if (lines[j +   y])[i +   x] != 'M':
            return 0
        if (lines[j + 2*y])[i + 2*x] != 'A':
            return 0
        if (lines[j + 3*y])[i + 3*x] != 'S':
            return 0
        return 1
    except:
        return 0

sum = 0

j = 0
while j < len(lines):
    lines[j] = [char for char in lines[j]]
    j += 1


j = 0
while j < len(lines):
    i = 0
    while i < len(lines[j]):
        #                  1                            2                             3                               4                           5                            6                             7                              8
        sum += is_xmas(lines, j, i, 1, 0) + is_xmas(lines, j, i, 1, 1) + is_xmas(lines, j, i, 0, 1) + is_xmas(lines, j, i, 0, -1) + is_xmas(lines, j, i, -1, 0) + is_xmas(lines, j, i, -1, -1) + is_xmas(lines, j, i, 1, -1) + is_xmas(lines, j, i, -1, 1)
        i += 1
    j += 1
    print(sum)

print(sum)
