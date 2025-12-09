import re
from pathlib import Path

input_string = Path("E:\\Repos\\AdventToCode\\2025\\Day6\\Input.txt").read_text()

# Use regex to find all numbers in the input string
rows = re.findall(r'.+', input_string)

i = 0
while i < len(rows):
    columns = re.findall(r'\S+', rows[i])
    rows[i] = [string for string in columns]
    i += 1

problemTotal = 0
j = 0
while j < len(rows[0]):
    i = 0
    columnTotal = 0
    sign = rows[len(rows)-1][j]
    while i < len(rows)-1:
        value = int(rows[i][j])
        if sign == '+' or columnTotal == 0:
            columnTotal += value
        elif sign == '*':
            columnTotal = columnTotal * value
        i += 1
    problemTotal += columnTotal
    j += 1

print(problemTotal)