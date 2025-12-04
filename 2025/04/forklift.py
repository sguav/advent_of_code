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

def prettyprint(grid):
    testprint(f"    + ", end='')
    [testprint(f"{j:x}", end='') for j,c in enumerate([r for r in grid]) ]
    testprint()
    [testprint(f"{i:03} | {row}") for i, row in enumerate(grid)]

def eval_forklift_access(grid: list[str]) -> list[list]:

    prettyprint(grid)

    work = []

    n_rows = len(grid)
    n_cols = len(grid[0])

# Offsets for the eight neighboring cells
    offsets = [
        (-1, -1), (-1, 0), (-1, 1),     # Top-left, Top, Top-right
        ( 0, -1),          ( 0, 1),     # Left,          Right
        ( 1, -1), ( 1, 0), ( 1, 1)      # Bottom-left, Bottom, Bottom-right
    ]

    for i, row in enumerate(grid):
        work.append([])
        for j, col in enumerate(row):
            count_rolls = 0
            (work[i]).append(grid[i][j])
            if col == "@":
                # Check around, 8 positions
                # print(f"Check for grid[{i}][{j}]")
                for dr, dc in offsets:
                    r = i + dr
                    c = j + dc
                    if      0 <= r < n_rows \
                        and 0 <= c < n_cols \
                        and grid[r][c] == "@":
                            count_rolls += 1
                if count_rolls < 4:
                    work[i][j]= "x"

    prettyprint(work)
    return work

def remove_rolls(grid):
    work = grid
    removable_rolls = sum(row.count("x") for row in work)
    if removable_rolls:
        print(f"> Removing {removable_rolls} paper rolls")
        work = [[cell.replace("x", ".") for cell in row] for row in work]
    else:
        print(f"> Can't remove any more rolls!")
    return removable_rolls, work


def main():

    input_file = "test" if (TEST) else "input"
    with open(f'{SCRIPT_PATH}/{input_file}') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    visualized_grid = eval_forklift_access(lines)
    accessible_rolls = sum(row.count("x") for row in visualized_grid)
    print(f"For part 1, there are {accessible_rolls} accessible paper rolls")
    # Part 1: 1395
    removed, visualized_grid = remove_rolls(visualized_grid)
    prettyprint(remove_rolls(visualized_grid))
    total = removed
    while removed:
        visualized_grid = eval_forklift_access(visualized_grid)
        removed, visualized_grid = remove_rolls(visualized_grid)
        total += removed
    print(f"For part 2, removed a total of {total} paper rolls")

if __name__ == '__main__':
    import sys
    sys.exit(main())