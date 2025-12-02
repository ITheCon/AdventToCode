
import re
from pathlib import Path

input_string = Path("E:\\Repos\\AdventToCode\\Day2\\Input.txt").read_text()
 
# Use regex to find all numbers in the input string
reports = re.findall(r'.+', input_string)

safeReports = 0

for report in reports:
    i = 0
    r = [int(num) for num in report.split()]
    ascending = True

    if r[i] < r[i + 1]:
        ascending = True
    elif r[i] > r[i + 1]:
        ascending = False
    safe = False

    while i < len(r) - 1:
        if ascending:
            safeCheck1 = r[i] < r[i + 1]
        else:
            safeCheck1 = r[i] > r[i + 1]
        safeCheck2 = 0 < abs(r[i] - r[i + 1]) <= 3
        safe = safeCheck1 & safeCheck2
        if not safe:
            break
        i += 1

    if safe:
        safeReports += 1


# Print the sorted columns
print("Safe Reports: ", safeReports)