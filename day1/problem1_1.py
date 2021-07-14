def get_elements_that_add_to_2020():
    for element in input:
        for operand in input:
            if input.index(element) == input.index(operand):
                pass
            if element + operand == 2020:
                return [element, operand]


def multiply_elements():
    elements_to_multiply = get_elements_that_add_to_2020()
    return elements_to_multiply[0] * elements_to_multiply[1]


with open("day1/problem1_1.txt") as input_file:
    input = [int(line.strip()) for line in input_file]

print(multiply_elements())
