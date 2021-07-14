with open("day3/problem_3_input.txt") as file:
    data = [[ch for ch in line if ch != '\n'] for line in file]

cols = len(data[0])
rows = len(data)

tree_counter = [0, 0, 0, 0, 0]
current_row = [0, 0, 0, 0, 0]
current_col = [0, 0, 0, 0, 0]
RIGHT = [1, 3, 5, 7, 1]
DOWN = [1, 1, 1, 1, 2]

for i in range(rows-1):
    current_col[0] = (current_col[0] + RIGHT[0]) % cols
    current_row[0] += DOWN[0]
    if data[current_row[0]][current_col[0]] == "#":
        tree_counter[0] += 1

    current_col[1] = (current_col[1] + RIGHT[1]) % cols
    current_row[1] += DOWN[1]
    if data[current_row[1]][current_col[1]] == "#":
        tree_counter[1] += 1

    current_col[2] = (current_col[2] + RIGHT[2]) % cols
    current_row[2] += DOWN[2]
    if data[current_row[2]][current_col[2]] == "#":
        tree_counter[2] += 1

    current_col[3] = (current_col[3] + RIGHT[3]) % cols
    current_row[3] += DOWN[3]
    if data[current_row[3]][current_col[3]] == "#":
        tree_counter[3] += 1

for i in range(int((rows-1)/2)):
    current_col[4] = (current_col[4] + RIGHT[4]) % cols
    current_row[4] += DOWN[4]
    if data[current_row[4]][current_col[4]] == "#":
        tree_counter[4] += 1

print(tree_counter[0] * tree_counter[1] * tree_counter[2] * tree_counter[3] * tree_counter[4])
