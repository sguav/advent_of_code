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

def check_ingredient_freshness(ingredient: int, ranges: list[tuple]) -> bool:
    """
    Return True if the ingredient is found in one of the given ranges
    Ranges are set as a list of tuples
    """
    ingredient = int(ingredient)

    for range in ranges:
        low, high = (int(v) for v in range)
        if low <= ingredient <= high:
            testprint(f"Ingredient {ingredient} is fresh")
            return True

    testprint(f"Ingredient {ingredient} is GONE BAD")
    return False

def get_fresh_ingredients_id(ranges: list[tuple]) -> int:
    # This will blow your memory out!
    # fresh_ids = set()
    # for low, high in ranges:
    #     low = int(low)
    #     high = int(high)
    #     fresh_ids.update(range(low, high + 1))

    # return fresh_ids

    intervals = [(int(a), int(b)) for a, b in ranges]
    intervals.sort()

    testprint(f"Sorted intervals:")
    testprint(intervals)

    merged = []
    cur_low, cur_high = intervals[0]

    for low, high in intervals[1:]:
        testprint(f"current lo, hi: {cur_low}, {cur_high} ", end="| ")
        if low <= cur_high + 1:
            testprint(f"Updating current high with {high}")
            cur_high = max(cur_high, high)
        else:
            testprint(f"Merging and updating currents with:  {low},{high}")
            merged.append((cur_low, cur_high))
            cur_low, cur_high = low, high

    merged.append((cur_low, cur_high))

    return sum(h - l + 1 for l, h in merged)

def main():

    ranges = []
    ingredients = []

    input_file = "test" if (TEST) else "input"
    with open(f'{SCRIPT_PATH}/{input_file}') as f:
        for l in f:
            stripped_l = l.strip()
            if stripped_l == "":
                break # Stop and save next ingredient lines into another list
            ranges.append(tuple(stripped_l.split('-')))

        for l in f:
            stripped_l = l.strip()
            if stripped_l:      # ignore extra blank lines, up to you
                ingredients.append(stripped_l)

        fresh_ingredients = 0
        for ingredient in ingredients:
            fresh_ingredients += 1 if check_ingredient_freshness(ingredient, ranges) else 0

    debugprint(f"Ranges: {ranges}")
    debugprint(f"Ingredients to check: {ingredients}")
    print(f"Fresh ingredients: {fresh_ingredients}")
    # Part 1: 707

    fresh_ids_num = get_fresh_ingredients_id(ranges)
    print(f"The are {fresh_ids_num} IDs in the given ranges")
    # Part 2: 361615643045059

if __name__ == '__main__':
    import sys
    sys.exit(main())