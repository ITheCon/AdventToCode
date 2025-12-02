import re
from pathlib import Path

input_string = Path("E:\\Repos\\AdventToCode\\Day2\\Input.txt").read_text()
# print (reports)
reports = re.findall(r'.+', input_string)
 
# Q2 Part 1
def is_safe(r):
    n = len(r)
    return ((all(1 <= r[i+1] - r[i] <= 3 for i in range(n - 1))) or (all(1 <= r[i] - r[i+1] <= 3 for i in range(n - 1))))
 
#Q2 Part 2
safe_count2 = 0
 
for report in reports:
    r = [int(num) for num in report.split()]
    safe_count2 += (is_safe(r) or any(is_safe(r[:i] + r[i+1:]) for i in range(len(r))))
 
print(safe_count2)