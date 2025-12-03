import os
import sys
SCRIPT_PATH = (os.path.dirname(os.path.realpath(__file__)))

DEBUG = (os.environ.get("DEBUG") == "1") or ((len(sys.argv) > 1 and sys.argv[1] == '-debug'))
TEST = (os.environ.get("TEST") == "1") or ((len(sys.argv) > 1 and sys.argv[1] == '-test'))
# print(f"Debug env var is {DEBUG}")

def debugprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def max_substring(sub_bank: str):
    max_val = max(sub_bank)
    return max_val, sub_bank.index(max_val)+1

def largest_joltage(bank: str, num_batteries=2) -> int:
    """
    Given a string of digits (battery joltage bank)
    Return the highest 'num_batteries'-digits number that can be
    found in string order
    """
    joltage = 0

    print(f"> '{bank}' ", end="| ")

    for d in range(num_batteries - 1, -1, -1): # Iterate digit from max number
        max_battery = max(bank[:-d] if d >= 1 else bank) # get the highest digit in the truncated (or full) substring
        bank = bank[bank.index(max_battery) + 1:] # Reduce substring
        joltage += int(max_battery) * (10 ** d)

    print(f"Highest joltage ({num_batteries} digits) in this bank: {joltage}")
    return int(joltage)

def main():
    joltage_accumulator_1 = 0
    joltage_accumulator_2 = 0

    input_file = "test" if (TEST) else "input"
    with open(f'{SCRIPT_PATH}/{input_file}') as f:
        while bank := f.readline():
            joltage_accumulator_1 += largest_joltage(bank[:-1]) # Strip newline
            joltage_accumulator_2 += largest_joltage(bank[:-1],12) # Strip newline


    print(f"The accumulated joltage for part 1 is: {joltage_accumulator_1}")
    print(f"The accumulated joltage for part 2 is: {joltage_accumulator_2}")
    # Part 1: 17278

if __name__ == '__main__':
    import sys
    sys.exit(main())