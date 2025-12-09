import os
import sys
SCRIPT_PATH = (os.path.dirname(os.path.realpath(__file__)))

DEBUG = (os.environ.get("DEBUG") == "1") or ((len(sys.argv) > 1 and sys.argv[1] == '-debug'))
TEST = (os.environ.get("TEST") == "1") or ((len(sys.argv) > 1 and sys.argv[1] == '-test'))
# print(f"Debug env var is {DEBUG}")

def debugprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def testprint(*args, **kwargs):
    if TEST:
        print(*args, **kwargs)

def find_max_in_col(l, col=0):
    largest = int(l[0][col])

    for row in l:
        if int(row[col]) > largest:
            largest = int(row[col])

    return int(largest)

def visualize_pattern(l):
    if TEST:
        width = find_max_in_col(l, 0)
        height = find_max_in_col(l, 1)

        testprint(f"W {width} H {height}")

        tiles = [['.' for _ in range(width+1)] for _ in range(height+1)]

        for coord in l:
            print(int(coord[1]),int(coord[0]))
            tiles[int(coord[1])][int(coord[0])] = '#'

        print_tiles(tiles)

def print_tiles(l):
    if TEST:
        for row in l:
            print(' '.join(str(item) for item in row))

def prettyprint(l):
    if TEST:
        for row in l:
            print(row)

def get_area(coord0, coord1):
    """
    Area which accounts for the CELL NUMBER,
    not plain distance (add +1)
    """
    return (abs(int(coord1[0]) - int(coord0[0]))+1) * (abs(int(coord1[1]) - int(coord0[1]))+1)

def main():

    lines = []

    input_file = "test" if (TEST) else "input"
    with open(f'{SCRIPT_PATH}/{input_file}') as f:
        for l in f:
            lines.append(l.strip().split(','))

    prettyprint(lines)
    visualize_pattern(lines)

    max_area = 1
    for p1 in lines:
        for p2 in lines:
            if  p1[0] != p2[0] or \
                p1[1] != p2[1]:
                temp_area = get_area(p1, p2)
                if temp_area > max_area:
                    testprint(f"Found greater area from ({p1[0]},{p1[1]}) and ({p2[0]},{p2[1]}) -> {temp_area}")
                    max_area = temp_area

    print(f"Max area from two red tiles found: {max_area}")

    # Part 1: 4763040296

    # Part 2: 8811937976367


if __name__ == '__main__':
    import sys
    sys.exit(main())