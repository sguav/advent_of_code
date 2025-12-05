#!/usr/bin/python3
import re

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
'''
consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
'''

pattern = r"mul\(\d+,\d+\)"
with open(filename, "r") as data:
    content = data.read()
    matches = re.findall(pattern, content)

debugprint(content)

def MAC_from_exp(lst):
    ''' Input a list with valid `mul(x,y)` expressions
        Will multiply and accumulate the result
    '''
    MAC = 0

    for m in lst:
        mulTuple = tuple(map(int, m[4:-1].split(',')))
        # debugprint(mulTuple)
        MAC += mulTuple[0] * mulTuple[1]
        # debugprint(MAC)

    return MAC


debugprint(matches)
MAC = MAC_from_exp(matches)
print(f"Memory MAC: {MAC}")
# 170778545

# Part 2

patterns = [
    r"mul\(\d+,\d+\)",
    r"don't\(\)",
    r"do\(\)"
]

def find_first_match_from_list(patterns, s):
    matches = []
    for pattern in patterns:
        debugprint(f"Pattern: {pattern}\tString: {s[:len(pattern)]}")
        match = re.search(pattern, s)
        if match:
            debugprint(f"===== Found a match: {match}")
            matches.append((match.start(), match.group(), match.end()))

    if matches:
        debugprint(f"========= List tokens found: {matches}")
        # Return the match with the smallest starting index, along with its start and end positions
        return min(matches, key=lambda x: x[0])[1], min(matches, key=lambda x: x[0])[0], min(matches, key=lambda x: x[0])[2]

    return None

def parse_mul_with_toggle(input_text):
    matches = []
    enabled = True  # mul is enabled initially
    i = 0
    while i < len(input_text):
        match = find_first_match_from_list(patterns, input_text[i:])
        if match == None:
            debugprint(f"No match found, end of string searching")
            return matches
        debugprint(match)
        m, start, end = match
        debugprint(m)
        i += end
        if m.startswith("don't()"):
            debugprint(">>>>>>>>>>`don't()` token: disable mul")
            enabled = False
        elif m.startswith("do()"):
            debugprint(">>>>>>>>>>`do()` token: enable mul")
            enabled = True
        elif m.startswith("mul") and enabled == True:
            debugprint(f"Appending to matches: {m}")
            matches.append(m)

    return matches
    # return matches


test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
debugprint(test_input)
# matches = parse_mul_with_toggle(test_input)
matches = parse_mul_with_toggle(test_input if DEBUG else content)
debugprint(matches)

print(f"Recovered Memory MAC: {MAC_from_exp(matches)}")
# 82868252
