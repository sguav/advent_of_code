import os
import sys
SCRIPT_PATH = (os.path.dirname(os.path.realpath(__file__)))

DEBUG = (os.environ.get("DEBUG") == "1") or ((len(sys.argv) > 1 and sys.argv[1] == '-debug'))
TEST = (os.environ.get("TEST") == "1") or ((len(sys.argv) > 1 and sys.argv[1] == '-test'))
# print(f"Debug env var is {DEBUG}")

def debugprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

global joltage_accumulator

def max_substring(sub_bank: str):
    max_val = max(sub_bank)
    return max_val, sub_bank.index(max_val)+1

def largest_joltage(bank: str) -> int:
    """
    Given a string of digits (battery joltage bank)
    Return the highest 2 digits number that can be
    found in string order
    """

    d, i = max_substring(bank[:-1])
    first_digit = d
    first_index = i
    second_digit = 0

    print(f"Bank: {bank} - Initial: {first_digit}(bank[{first_index}])")
    # print(f"Bank: {bank} - Initial: {first_digit}{second_digit}")

    while i < len(bank):
        d, ii = max_substring(bank[i:])
        i += ii
        d = int(d)
        if i < len(bank[i:-1]):
            if d > int(first_digit):
                first_digit = str(d)
            elif d > int(second_digit):
                second_digit = str(d)
        else:
            second_digit = str(d) if d > int(second_digit) else second_digit

    print(f"Highest joltage in this bank: {first_digit}{second_digit}")
    return int(first_digit+second_digit)




def main():
    global joltage_accumulator
    joltage_accumulator = 0

    input_file = "test" if (TEST) else "input"
    with open(f'{SCRIPT_PATH}/{input_file}') as f:
        while bank := f.readline():
            joltage_accumulator += largest_joltage(bank[:-1]) # Strip newline


    print(f"The accumulated joltage is: {joltage_accumulator}")
    # Part 1: 17278

if __name__ == '__main__':
    import sys
    sys.exit(main())