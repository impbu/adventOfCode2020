with open("day3/problem_3_input.txt") as file:
    data = [[ch for ch in line if ch != '\n'] for line in file]

cols = len(data[0])
rows = len(data)
tree_counter = 0
current_row = 0
current_col = 0
RIGHT = 3
DOWN = 1

for i in range(rows-1):
    current_col = (current_col + RIGHT) % cols
    current_row += DOWN
    if data[current_row][current_col] == "#":
        tree_counter += 1

print(tree_counter)
