f = open('test.txt')
DATA = f.read()
LINES = DATA.splitlines()

def find_starting_position(maze):
    for i, row in enumerate(maze):
        if 'S' in row:
            for j, symbol in enumerate(row):
                if symbol == 'S':
                    return (i, j)

MAZE = LINES

# Left = 'L' or '-' or 'F' 
# Right = 'J' or '-' or '7'
# Up = '|'
# Down = '|'

direction_dict = {'UP': ['|'], 'DOWN': ['|'], 'LEFT': ['L', '-', 'F'], 'RIGHT': ['J', '-', '7']}
symbol_dict = {'|': ['UP', 'DOWN'], '-': ['LEFT', 'RIGHT'], 'L': ['UP', 'RIGHT'], 'F': ['DOWN', 'RIGHT'], 'J': ['UP', 'LEFT'], '7': ['DOWN', 'LEFT']}

main_pipe = []
prev_positions = []

def next_pipe(curr_symbol, curr, prev):
    print(f'Finding Next Pipe (Curr_Symbol: {curr_symbol}, Curr: {curr}, Prev: {prev})')

    curr_row = curr[0]
    curr_col = curr[1]

    up = ('UP', curr_row - 1, curr_col)
    down = ('DOWN', curr_row + 1, curr_col)
    left = ('LEFT', curr_row, curr_col - 1)
    right = ('RIGHT', curr_row, curr_col + 1)

    directions = [up, down, left, right]
    next_symbol = None

    for (direction, next_row, next_col) in directions:
        print(f'({direction}, {next_row}, {next_col})')
        print('Condition 1: ', 0 <= next_row < len(MAZE))
        print('Condition 2: ', (0 <= next_col < len(MAZE[0])))
        print('Condition 3: ', (next_row, next_col) != prev)
        
        if (0 <= next_row < len(MAZE)) and (0 <= next_col < len(MAZE[0])) and (next_row, next_col) != prev:
            next_symbol = MAZE[next_row][next_col]
            if direction in symbol_dict[curr_symbol] and next_symbol in direction_dict[direction]:
            # if next_symbol in direction_dict[direction]:
                # print(next_symbol)
                main_pipe.append(next_symbol)
                previous_position = curr
                current_position = (next_row, next_col)
                current_symbol = next_symbol
                return next_symbol, current_position, previous_position

    print('Returning None...')
    return None

starting_position = find_starting_position(MAZE)
current_position = starting_position
previous_position = None
current_symbol = 'F'
completed = False

while not completed:
    next_symbol, current_position, previous_position = next_pipe(current_symbol, current_position, previous_position)
    main_pipe.append(next_symbol)
    if current_symbol == 'S':
        completed = True

print(main_pipe)