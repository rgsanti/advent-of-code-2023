f = open('input.txt')
DATA = f.read()
LINES = DATA.splitlines()

# --- Part One ---

BAG = [('red', 12), ('green', 13), ('blue', 14)]
COLOURS = [colour for (colour, _) in BAG]

def get_hands(index, string):
    game_id = index + 1
    hands = string.split('; ')
    hands[0] = hands[0][hands[0].index(': ')+2:len(hands[0])]
    return (game_id, hands)

def is_hand_valid(hand):
    cubes = hand.split(', ')
    hand = []
    for cube in cubes:
        cube = cube.split(' ')
        colour_count_tuple = (cube[1], cube[0])
        hand.append(colour_count_tuple)

    for (colour, count) in hand:
        colour_index = COLOURS.index(colour)
        if int(count) > BAG[colour_index][1]:
            return False
        
    return True

def is_game_valid(hands):
    valid_hands = []
    for hand in hands:
        if is_hand_valid(hand):
            valid_hands.append(hand)

    if len(valid_hands) == len(hands):
        return True
    else:
        return False

def part_one():
    valid_game_ids = []
    for (i, string) in enumerate(LINES):
        game_id, hands = get_hands(i, string)
        if (is_game_valid(hands)):
            valid_game_ids.append(game_id)
    print(f'Part One: {sum(valid_game_ids)}')

part_one()

# --- Part Two ---

def flatten_hands(hands):
    return [colour_count_tuple for hand in hands for colour_count_tuple in hand]

def get_colour_counts(hands):
    hands_list = []
    for hand in hands:
        cubes = hand.split(', ')
        hand = []
        for cube in cubes:
            cube = cube.split(' ')
            colour_count_tuple = (cube[1], int(cube[0]))
            hand.append(colour_count_tuple)
        hands_list.append(hand)
    return hands_list

def get_min_cubes(hands):
    mins = {'red': 0, 'green': 0, 'blue': 0}
    all_hands = flatten_hands(hands)

    for (colour, count) in all_hands:
        if count > mins[colour]:
            mins[colour] = count
    
    return mins

def get_power(min_cubes):
    values = min_cubes.values()
    power = 1
    for value in values:
        power *= value
    return power

def part_two():
    powers = []

    for (i, string) in enumerate(LINES):
        _, hands = get_hands(i, string)
        hands = get_colour_counts(hands)
        min_cubes = get_min_cubes(hands)
        power = get_power(min_cubes)
        powers.append(power)

    answer = sum(powers)
    print(f'Part Two: {answer}')

part_two()