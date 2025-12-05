#!/usr/bin/python3

import os

# Part 1

dbg = os.getenv("DEBUG", 0)

def debugprint(s):
    if dbg:
        print(s)

debugprint(f"In debug mode")

# Parse input
if dbg:
    filename="./test"
else:
    filename="./input"

#####################################################################
contents = []
def txt_as_char_matrix(filename):
    with open(f"{filename}", "r") as file:
        return [list(line.rstrip('\n')) for line in file]
#####################################################################
'''
find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words.
It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them.
'''

# Map input to look for XMAS sequentially
# When an 'X' is found, look around the cell for 'M' and so forth
# Should find optimizations to map relevant cells only...

xmatrix = txt_as_char_matrix(filename)
debugprint(xmatrix)

def traverse(coord, dir, word="XMAS"):
    '''
        This function traverses a given direction starting from a given point.
        It looks for all letters in the word, and exits at the first mismatch.
        If it finds a valid word, it returns first and last char's coordinates.

        args:
            coord: tuple (row, col)
            dir: tuple in the form:
                        Directions: up, down, left, right, and diagonals
                        directions = [
                        (-1, 0), (1, 0), (0, -1), (0, 1),  # Cardinal directions
                        (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal directions
                    ]
            word: optional string value for word to match

        retval:
            vect: list of tuples with start and end character's coordinates
    '''
    global xmatrix

    row, col = coord
    for i, c in enumerate(word):
        if (row >= 0 and col >= 0) and (row < len(xmatrix) and col < len(xmatrix[row])):
            if xmatrix[row][col] != c:
                # Mismatch, return None
                debugprint(f"## Warning: Mismatching character {c} at ({row}, {col})")
                return None
            else:
                # Match, look for next in given direction
                debugprint(f">> Found matching character '{c}' at ({row}, {col})")
                if (i + 1) == len(word):
                    # Last char, need to save and return in case of match
                    debugprint(f">> Found matching word. Returning start and end coordinates: ({coord}, {(row, col)})")
                    return [coord, (row, col)]
                else:
                    # Not last char, continue with direction
                    # zip pairs corresponding elements from the tuples, then sum them and assign to new values
                    row, col = [x + y for x, y in zip((row, col), dir)]
                    # if row < 0 or col < 0:
                        # debugprint(f"WTF is happening here? <{row}, {col}>")
                        # debugprint(f"i: {i}, c: {c}, coord: {coord}")
                        # pass
        else:
            debugprint(f"## Index larger than matrix: <{row}, {col}>")
            return None

    print(f"!! ERROR: {traverse.__name__} function reached an unexpected state.")

# Directions: up, down, left, right, and diagonals
directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1),  # Cardinal directions
    (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal directions
]

# Each word is mapped as a list of 2-tuples
# Store the coordinate for 'X' and for 'S' in a list,
# all lists go into xmases so that len(xmases) is the solution to Part 1
xmases = []

for row, l in enumerate(xmatrix):
    for col, c in enumerate(xmatrix[row]):
        for d in directions:
            match = traverse((row, col), d)
            if match:
                debugprint(f"= Match coordinates to append: {match}")
                xmases.append(match)
            else:
                debugprint(f"- No match for {row, col}")
                continue

print(f"Found {len(xmases)} instances of valid `XMAS` words")
# 2642

# Part 2
# Use only diagonals only and change word to MAS
diagonals = [
    (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal directions
]

# Reset list
xmases = []

for row, l in enumerate(xmatrix):
    for col, c in enumerate(xmatrix[row]):
        for d in diagonals:
            match = traverse((row, col), d,word="MAS")
            if match:
                debugprint(f"= Match coordinates to append: {match}")
                xmases.append(match)
            else:
                debugprint(f"- No match for {row, col}")
                continue

# This returns all diagonal "MAS" words, need to find the ones that cross

# Transpose coordinates to then match in set intersection
def transform_coordinates(coordinates):
    if len(coordinates) != 2:
        raise ValueError("Function requires exactly two coordinates for transposition.")
    (x0, y0), (x1, y1) = coordinates
    debugprint(f"*** orig: {coordinates} transformed: {[(x0, y1), (x1, y0)]}")
    return (x0, y1), (x1, y0)

# Function to find crossing coordinates

def find_crossing_coordinates(diagonals):
    crossings = []
    for i, diag1 in enumerate(diagonals):
        for j, diag2 in enumerate(diagonals):
            if i >= j:  # Avoid redundant checks and self-comparison
                continue

            xed = transform_coordinates(diag1)

            # Check if they cross by sharing a common point
            debugprint(f"Check: {xed[0], xed[1]} & {diag2[0], diag2[1]}")
            # if {xed[0], xed[1]} & {diag2[0], diag2[1]}:
            if set(xed) == set(diag2):
                debugprint(f"``` Found match X-shape! {diag1[0], diag1[1]} & {diag2[0], diag2[1]}")
                crossings.append([diag1, diag2])

    return crossings

def print_crossing_words(matrix_size, coordinate_pairs):
    global xmatrix
    # Initialize the matrix with '.'
    matrix = [['.' for _ in range(matrix_size[1])] for _ in range(matrix_size[0])]

    # Fill the matrix based on the given coordinates
    for pair in coordinate_pairs:
        for coord_set in pair:
            start, end = coord_set
            matrix[start[0]][start[1]] = xmatrix[start[0]][start[1]] #'M'
            matrix[end[0]][end[1]] = xmatrix[end[0]][end[1]] #'S'

            # Calculate the midpoints
            mid_row = (start[0] + end[0]) // 2
            mid_col = (start[1] + end[1]) // 2

            # Mark the midpoint with 'A'
            matrix[mid_row][mid_col] = xmatrix[mid_row][mid_col]

    # Print the resulting matrix
    for row in matrix:
        print(' '.join(row))
    # By using this on the test input...I see that I'm matchin too loosely
    # Need to check that intersection is for both coordinates


x_mas = find_crossing_coordinates(xmases)
print(f"Found {len(x_mas)} instances of X-shaped `MAS` words")
# 1974, after too much memory used...!