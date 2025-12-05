def get_score(opponent_move, your_move):
    if opponent_move == your_move:
        return 3  # Draw
    elif (opponent_move == 'A' and your_move == 'Y') or \
         (opponent_move == 'B' and your_move == 'X') or \
         (opponent_move == 'C' and your_move == 'Z'):
        return 6  # Win
    else:
        return 1  # Loss

def calculate_total_score(strategy_guide):
    total_score = 0
    for opponent_move, your_move in strategy_guide:
        score = get_score(opponent_move, your_move)
        total_score += score
    return total_score

# Read the strategy guide from the file
file_path = "data/test"
with open(file_path, 'r') as f:
    strategy_guide = [line.strip().split() for line in f]

total_score = calculate_total_score(strategy_guide)
print("Total score according to the strategy guide:", total_score)
