f = open('input.txt')
data = f.read()
lines = data.splitlines()

line_info = []

for index, string in enumerate(lines):
    numbers = []
    symbols = []
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
            if char == '.':
                continue
            else:
                symbols.append((char_index, char))
    line_info.append({'numbers': numbers, 'symbols': symbols})

part_numbers = []

for index, line in enumerate(line_info):
    for number_info in line_info[index]['numbers']:
        number_indices = [x[0] for x in number_info]
        number = int(('').join([x[1] for x in number_info]))
        for symbol_info in line_info[index]['symbols']:
            symbol_indices = [symbol_info[0]]
            for symbol_index in symbol_indices:
                if (symbol_index == number_indices[0] - 1) or (symbol_index == number_indices[-1] + 1):
                    part_numbers.append(number)
        if index - 1 >= 0:
            for symbol_info in line_info[index - 1]['symbols']:
                symbol_indices = [symbol_info[0]]
                for symbol_index in symbol_indices:
                    if (number_indices[0] - 1 <= symbol_index <= number_indices[-1] + 1):
                        part_numbers.append(number)
        if index + 1 < len(line_info):
            for symbol_info in line_info[index + 1]['symbols']:
                symbol_indices = [symbol_info[0]]
                for symbol_index in symbol_indices:
                    if (number_indices[0] - 1 <= symbol_index <= number_indices[-1] + 1):
                        part_numbers.append(number)

print(sum(part_numbers))