import os
import sys
SCRIPT_PATH = (os.path.dirname(os.path.realpath(__file__)))

DEBUG = (os.environ.get("DEBUG") == "1") or ((len(sys.argv) > 1 and sys.argv[1] == '-debug'))
TEST = (os.environ.get("TEST") == "1") or ((len(sys.argv) > 1 and sys.argv[1] == '-test'))
# print(f"Debug env var is {DEBUG}")

global valid_id
global id_accumulator

def debugprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def ceildiv(a, b):
    return -(a // -b)

def check_invalid_id(id):
    """
    IDs are INVALID if they are composed of some repeated sequence exactly TWICE. FFS
    Return True on invalid ID
    """
    id = str(id)
    id_len = len(id)

    if id_len % 2 != 0 or id_len == 0:
        return False

    half_id = id_len // 2
    return id[:half_id] == id[half_id:]

def check_invalid_id_part_two(id):
    """
    Old function, good for part 2...
    Actually done this for part 1 and banged my head there...
    """
    id = str(id)

    if len(id) == 1:
        debugprint("Assuming IDs of length 1 are valid. Return FAIL")
        return False

    digits = set(id)
    num_digits = len(digits)
    half_width = ceildiv(len(id),2)

    debugprint(num_digits, half_width)

    # Easy check: more digits than half width?
    # Can't be invalid, just return
    if num_digits > half_width:
        debugprint(f"Id '{int(id)}' is valid, too many different digits! Return FAIL")
        return False

    # Easy check: Identical digits
    # Use python set to "compress" the identical digits
    # If len of this set is 1, then ID is invalid
    if num_digits == 1:
        debugprint(f"Id '{int(id)}' looks invalid, identical digits! Return OK")
        return True

    # Brute force
    # Double the string and truncate extremities
    # If the original string appears there, it is a invalid ID
    # Truncating is necessary to eliminate the trivial matches resulting from concatenation
    if id in (id+id)[1:-1]:
        debugprint(f"Id '{int(id)}' looks invalid! Return OK")
        return True
    else:
        debugprint(f"Id '{int(id)}' is valid. Return FAIL")
        return False

def check_range(id_range):
    bot, top = str(id_range).split('-')
    print(f"Checking Range '{bot}-{top}' | ", end='')

    # if bot >= top:
    #     print("Invalid range!")
    #     return False

    global valid_id
    global id_accumulator
    valid_id = 0

    for id in range(int(bot), int(top) + 1):
        # if check_invalid_id(id):
        if check_invalid_id_part_two(id):
            debugprint(f"Found invalid ID: {id}")
            valid_id += 1
            id_accumulator += int(id)

    print(f"Found {valid_id} invalid ids in provided range {id_range}")

def main():
    global id_accumulator
    id_accumulator = 0

    input_file = "test" if (TEST) else "input"
    with open(f'{SCRIPT_PATH}/{input_file}') as f:
        while l := f.readline():
            id_ranges = l.split(',')

    for r in id_ranges:
        check_range(r)

    print(f"Given the found (invalid) IDs, their accumulated sum is: {id_accumulator}")
    # Part 1: 16793817782

if __name__ == '__main__':
    import sys
    sys.exit(main())