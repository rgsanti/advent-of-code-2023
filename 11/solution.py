from itertools import combinations
import copy

f = open('input.txt')
DATA = f.read()
LINES = DATA.splitlines()

# def expand_universe(universe):
#     no_galaxy_row_indices = []
#     for index, row in enumerate(universe):
#         if '#' not in row:
#             no_galaxy_row_indices.append(index)
#     columns = zip(*universe)
#     no_galaxy_column_indices = []
#     for index, column in enumerate(columns):
#         if '#' not in column:
#             no_galaxy_column_indices.append(index)

#     for i in range(0, len(no_galaxy_row_indices)):
#         universe.insert(no_galaxy_row_indices[i] + i, '..........')
    
#     for line in universe:
#         print(line)

#     for i in range(0, len(no_galaxy_column_indices)):
#         for j, row in enumerate(universe):
#             universe[j] = row[:no_galaxy_column_indices[i] + i] + '.' + row[no_galaxy_column_indices[i] + i:]

#     return universe

# def get_galaxy_positions(universe):
#     galaxy_positions = []
#     for i, row in enumerate(universe):
#         print(row)
#         for j, char in enumerate(row):
#             if char == '#':
#                 galaxy_positions.append((j, i))
#     return galaxy_positions

# expanded_universe = expand_universe(LINES)

# galaxy_positions = get_galaxy_positions(expanded_universe)
# print(galaxy_positions)

# pairings = list(combinations(galaxy_positions, 2))

# distances = []

# for (position_a, position_b) in pairings:
#     x_coord_diff = abs(position_a[0] - position_b[0])
#     y_coord_diff = abs(position_a[1] - position_b[1])
#     distance = x_coord_diff + y_coord_diff
#     distances.append(distance)

# print(sum(distances))

##### Part Two

def expand_universe(lines):
    universe = copy.deepcopy(lines)
    no_galaxy_row_indices = []
    for index, row in enumerate(universe):
        if '#' not in row:
            no_galaxy_row_indices.append(index)
    columns = zip(*universe)
    no_galaxy_column_indices = []
    for index, column in enumerate(columns):
        if '#' not in column:
            no_galaxy_column_indices.append(index)

    for i in range(0, len(no_galaxy_row_indices)):
        for j in range(10):
            universe.insert(no_galaxy_row_indices[i] + (i * 10), '..........')

    for i in range(0, len(no_galaxy_column_indices)):
        for j, row in enumerate(universe):
            universe[j] = row[:no_galaxy_column_indices[i] + (i * 10)] + '..........' + row[no_galaxy_column_indices[i] + (i * 10):]

    return universe, no_galaxy_row_indices, no_galaxy_column_indices

def get_galaxy_positions(universe):
    galaxy_positions = []
    for i, row in enumerate(universe):
        for j, char in enumerate(row):
            if char == '#':
                galaxy_positions.append((j, i))
    return galaxy_positions

expanded_universe, no_galaxy_rows, no_galaxy_columns = expand_universe(LINES)

for line in expanded_universe:
    print(line)

print()

expanded_universe = LINES

galaxy_positions = get_galaxy_positions(expanded_universe)
print(galaxy_positions)

pairings = list(combinations(galaxy_positions, 2))
print(len(pairings))

distances = []

for (position_a, position_b) in pairings:
    x_coord_diff = abs(position_a[0] - position_b[0])
    y_coord_diff = abs(position_a[1] - position_b[1])
    
    num_no_galaxy_rows_between = len(list(filter(lambda i: min(position_a[1], position_b[1]) < i < max(position_a[1], position_b[1]), no_galaxy_rows)))
    num_no_galaxy_columns_between = len(list(filter(lambda i: min(position_a[0], position_b[0]) < i < max(position_a[0], position_b[0]), no_galaxy_columns)))

    distance = (x_coord_diff + num_no_galaxy_columns_between * 999999) + (y_coord_diff + num_no_galaxy_rows_between * 999999)

    print(f'{position_a}, {position_b}.\nX Difference = {x_coord_diff}, Y Difference = {y_coord_diff}\nNumber of Columns between: {num_no_galaxy_columns_between}\nNumber of Rows between: {num_no_galaxy_rows_between}\nDistance: {distance}')

    distances.append(distance)

print(no_galaxy_rows)
print(no_galaxy_columns)
print(sum(distances))