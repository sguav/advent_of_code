#!/usr/bin/python3
# Part 1

DEBUG=0

def debugprint(s):
    if DEBUG:
        print(s)

# Parse input
if DEBUG:
    filename="./test"
else:
    filename="./input"

columns = []
with open(f"{filename}", "r") as file:
    for line in file:
        values = line.split()
        for i, value in enumerate(values):
            if len(columns) <= i:
                columns.append([])
            columns[i].append(value)

debugprint(columns)

for l in columns:
    l.sort()

debugprint(columns)

total_distance = []
for i in range(len(columns[0])):
    total_distance.append(abs(int(columns[0][i])-int(columns[1][i])))

debugprint(total_distance)
print(sum(total_distance))
