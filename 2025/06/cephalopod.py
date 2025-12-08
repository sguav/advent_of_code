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

# Part 1
def compute_column(col: list[str]) -> int:
    op = col[-1]
    mac = 0 if op == '+' else 1
    for i in col[:-1]:
        mac = (mac + int(i)) if op == '+' else (mac * int(i))
        testprint(f"{i} {op} ", end='')

    testprint(f" | Mac: {mac}")

    return mac

def pretty_grid(grid):
    if TEST:
        for row in grid:
            print(row)

def grid_and_pad_cephalopod_sheet(filename):
    with open(filename) as f:
        grid = [list(line.rstrip("\n")) for line in f]

    # Max len for R padding columns
    max_length = max(len(row) for row in grid)

    # Pad with spaces
    padded_grid = [row + [' '] * (max_length - len(row)) for row in grid]

    # Print result
    # pretty_grid(padded_grid)

    return padded_grid

def cephalopod_math_RtoL_TtoB(padded_grid):
    pretty_grid(padded_grid)
    padded_nums_only = padded_grid[:-1]
    ops = [op for op in padded_grid[-1] if op != ' ']

    max_len = max(len(r) for r in padded_nums_only)

    pretty_grid(padded_nums_only)
    testprint(ops)

    testprint(f"Row 0 len: {len(padded_nums_only[0])} | Last row len {len(padded_nums_only[-1])}")

    transposed = [[padded_nums_only[j][i] for j in range(len(padded_nums_only))] for i in range(max_len)]
    pretty_grid(transposed)

    # Compact transposed
    compacted = []
    for r in transposed:
        item = ''
        for c in r:
            item += c
        item = item.split()
        compacted.append(int(item[0]) if item else '')

    testprint(compacted)

    idx = 0
    total_sum = 0
    op = ops[idx]
    mac = 0 if op == '+' else 1
    testprint(f"ops len: {len(ops)}")
    for n in compacted:
        if n:
            mac = (mac + int(n)) if op == '+' else (mac * int(n))
        else:
            testprint(f"Mac for {idx} op: {mac}")
            total_sum += mac
            if idx > len(ops) + 1:
                testprint(f"WTF: idx {idx} > {len(ops) + 1}. Breaking...")
            idx += 1
            op = ops[idx]
            mac = 0 if op == '+' else 1

    testprint(f"Mac for {len(ops) - 1} op: {mac}")
    total_sum += mac

    print(f"Accumulated sum for part 2 is: {total_sum}")





def main():

    lines = []

    input_file = "test" if (TEST) else "input"
    with open(f'{SCRIPT_PATH}/{input_file}') as f:
        for l in f:
            parts = l.strip().split()
            lines.append(parts)

    testprint(lines)
    total_sum = 0
    for i in range(len(lines[-1])):
        total_sum += compute_column([row[i] for row in lines])
    print(f"Accumulated result is: {total_sum}")
    # Part 1: 6171290547579

    padded_grid = grid_and_pad_cephalopod_sheet(f'{SCRIPT_PATH}/{input_file}')
    cephalopod_math_RtoL_TtoB(padded_grid)
    # Part 2: 8811937976367


if __name__ == '__main__':
    import sys
    sys.exit(main())