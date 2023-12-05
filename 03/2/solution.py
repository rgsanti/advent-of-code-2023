f = open('input.txt')
data = f.read()
lines = data.splitlines()

line_info = []

for index, string in enumerate(lines):
    numbers = []
    gears = []
    curr_number = []
    for char_index, char in enumerate(string):
        if char.isnumeric():
            curr_number.append((char_index, char))
            if char_index == len(string) - 1:
                numbers.append(curr_number)
                continue
        else:
            if curr_number != []:
                numbers.append(curr_number)
            curr_number = []
            if char == '*':
                gears.append((char_index, char))
            else:
                continue
    line_info.append({'numbers': numbers, 'gears': gears})

for index, info in enumerate(line_info):
    print(f'Line {index} Info:')
    print(info)

gear_ratios = []

for index, line in enumerate(line_info):

    if len(line_info[index]['gears']) == 0:
        continue

    for gear_info in line_info[index]['gears']:
        adjacent_numbers = []
        gear_index = gear_info[0]
        for number_info in line_info[index]['numbers']:
            number_indices = [x[0] for x in number_info]
            number = int(('').join([x[1] for x in number_info]))
            if (gear_index == number_indices[0] - 1) or (gear_index == number_indices[-1] + 1):
                adjacent_numbers.append(number)
        if index - 1 >= 0:
            for number_info in line_info[index - 1]['numbers']:
                number_indices = [x[0] for x in number_info]
                number = int(('').join([x[1] for x in number_info]))
                if (number_indices[0] - 1 <= gear_index <= number_indices[-1] + 1):
                    adjacent_numbers.append(number)
        if index + 1 < len(line_info):
            for number_info in line_info[index + 1]['numbers']:
                number_indices = [x[0] for x in number_info]
                number = int(('').join([x[1] for x in number_info]))
                if (number_indices[0] - 1 <= gear_index <= number_indices[-1] + 1):
                    adjacent_numbers.append(number)
        if len(adjacent_numbers) == 2:
            gear_ratios.append(adjacent_numbers[0] * adjacent_numbers[1])

print(gear_ratios)
print(sum(gear_ratios))

    # for number_info in line_info[index]['numbers']:
    #     number_indices = [x[0] for x in number_info]
    #     number = int(('').join([x[1] for x in number_info]))
    #     for symbol_info in line_info[index]['symbols']:
    #         symbol_indices = [symbol_info[0]]
    #         for symbol_index in symbol_indices:
    #             if (symbol_index == number_indices[0] - 1) or (symbol_index == number_indices[-1] + 1):
    #                 part_numbers.append(number)
    #     if index - 1 >= 0:
    #         for symbol_info in line_info[index - 1]['symbols']:
    #             symbol_indices = [symbol_info[0]]
    #             for symbol_index in symbol_indices:
    #                 if (number_indices[0] - 1 <= symbol_index <= number_indices[-1] + 1):
    #                     part_numbers.append(number)
    #     if index + 1 < len(line_info):
    #         for symbol_info in line_info[index + 1]['symbols']:
    #             symbol_indices = [symbol_info[0]]
    #             for symbol_index in symbol_indices:
    #                 if (number_indices[0] - 1 <= symbol_index <= number_indices[-1] + 1):
    #                     part_numbers.append(number)

# part_numbers = []

# for index, line in enumerate(line_info):
#     for number_info in line_info[index]['numbers']:
#         number_indices = [x[0] for x in number_info]
#         number = int(('').join([x[1] for x in number_info]))
#         for symbol_info in line_info[index]['symbols']:
#             symbol_indices = [symbol_info[0]]
#             for symbol_index in symbol_indices:
#                 if (symbol_index == number_indices[0] - 1) or (symbol_index == number_indices[-1] + 1):
#                     part_numbers.append(number)
#         if index - 1 >= 0:
#             for symbol_info in line_info[index - 1]['symbols']:
#                 symbol_indices = [symbol_info[0]]
#                 for symbol_index in symbol_indices:
#                     if (number_indices[0] - 1 <= symbol_index <= number_indices[-1] + 1):
#                         part_numbers.append(number)
#         if index + 1 < len(line_info):
#             for symbol_info in line_info[index + 1]['symbols']:
#                 symbol_indices = [symbol_info[0]]
#                 for symbol_index in symbol_indices:
#                     if (number_indices[0] - 1 <= symbol_index <= number_indices[-1] + 1):
#                         part_numbers.append(number)

# print(sum(part_numbers))