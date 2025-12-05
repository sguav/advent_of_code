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

#####################################################################
''' A report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
'''
reports = []
with open(f"{filename}", "r") as file:
    for line in file:
        reports.append([int(value) for value in line.split()])

debugprint(reports)

def is_report_safe(lst):

    deltas = [lst[i+1] - lst[i] for i in range(len(lst) - 1)]

    # Check if the list is strictly increasing or decreasing
    if all(delta > 0 for delta in deltas):
        direction = "increasing"
    elif all(delta < 0 for delta in deltas):
        direction = "decreasing"
    else:
        return False  # Not ordered

    # Check if deltas are within the allowed range
    if direction == "increasing" and all(1 <= delta <= 3 for delta in deltas):
        return True
    elif direction == "decreasing" and all(-3 <= delta <= -1 for delta in deltas):
        return True

    return False

safe_reports = 0
for r in reports:
    safe_reports += 1 if is_report_safe(r) else 0

print(f"Safe reports: {safe_reports}")
# 230 on final input

# Part 2

def can_be_made_safe(lst):
    def is_safe_after_removal(index):
        # Create a new list excluding the item at the given index
        modified_lst = lst[:index] + lst[index+1:]
        return is_report_safe(modified_lst)

    for i in range(len(lst)):
        if is_safe_after_removal(i):
            return True  # Found an item that can be removed to make the list valid

    return False  # No single removal makes the list valid

safe_reports = 0
for r in reports:
    if is_report_safe(r):
        safe_reports += 1
    else:
        safe_reports += 1 if can_be_made_safe(r) else 0

print(f"Safe reports after problem dampener: {safe_reports}")
# 301
