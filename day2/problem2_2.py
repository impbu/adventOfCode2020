valid_password_counter = 0

file = open("day2/problem2_input.txt")
while True:
    line = file.readline()
    if not line:
        break
    line = line.replace("-", " ")
    line = line.replace(":", "")
    line = line.split(" ")

    pos_1 = int(line[0]) - 1
    pos_2 = int(line[1]) - 1
    if line[3][pos_1] == line[2] and line[3][pos_2] == line[2]:
        pass
    elif line[3][pos_1] == line[2]:
        valid_password_counter = valid_password_counter + 1
    elif line[3][pos_2] == line[2]:
        valid_password_counter = valid_password_counter + 1

file.close()
print(valid_password_counter)
