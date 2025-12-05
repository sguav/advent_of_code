#!/usr/bin/python3
# Part 2

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
            columns[i].append(int(value))

debugprint(columns)

for l in columns:
    l.sort()

debugprint(columns)

total_distance = []
similarity_score = 0
for i in range(len(columns[0])):
    total_distance.append(abs(int(columns[0][i])-int(columns[1][i])))
    num = int(columns[0][i])
    similarity_score += num * columns[1].count(num)

debugprint(total_distance)
print("Total distance: ", sum(total_distance))
print("Similarity score: ", similarity_score)
