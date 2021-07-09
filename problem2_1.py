valid_password_counter = 0

file = open("problem2.txt")
while True:
    line = file.readline()
    if not line:
        break
    line = line.replace("-", " ")
    line = line.replace(":", "")
    line = line.split(" ")
    char_count = line[3].count(line[2])
    if char_count >= int(line[0]) and char_count <= int(line[1]):
        valid_password_counter = valid_password_counter + 1

file.close()
print(valid_password_counter)
