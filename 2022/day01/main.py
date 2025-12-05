input_file_name = 'data/input'

if __name__ == "__main__":
    # Open file
    with open(input_file_name, 'r') as f:
        # A list "per elf"
        elves = f.read().split("\n\n")
    # Make elves a list of ints for each elf
    elves = [[int(l) for l in elf.split("\n") if l] for elf in elves]

    # List for enumerated tuples
    cal_list = []
    max_calories = 0

    for i, elf in enumerate(elves):
        calories = sum(cal for cal in elf)
        cal_list.append((calories, i))
        if calories > max_calories:
            max_calories = calories

    cal_list.sort(reverse=True)
    top_three_cals = sum(calories for calories, _ in cal_list[:3])

    print(f"Most calories carried: {max_calories}")
    print(f"Top three elves calories: {top_three_cals}")
