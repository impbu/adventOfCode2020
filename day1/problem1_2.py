def get_elements_that_add_to_2020():
    for element in input:
        for operand in input:
            for second_operand in input:
                if input.index(element) == input.index(operand) or input.index(element) == input.index(second_operand) or input.index(operand) == input.index(second_operand):
                    pass
                if element + operand + second_operand == 2020:
                    return [element, operand, second_operand]


def multiply_elements():
    elements_to_multiply = get_elements_that_add_to_2020()
    return elements_to_multiply[0] * elements_to_multiply[1] * elements_to_multiply[2]

#input = [1721, 979, 366, 299, 675, 1456]
with open("day1/problem1_1.txt") as input_file:
    input = [int(line.strip()) for line in input_file]

print(multiply_elements())
