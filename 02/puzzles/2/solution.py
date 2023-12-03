f = open('input.txt')
data = f.read()
lines = data.splitlines()

def get_hands(index, string):
    game_id = index + 1
    hands = string.split('; ')
    hands[0] = hands[0][hands[0].index(': ')+2:len(hands[0])]
    return (game_id, hands)

def flatten_hands(hands):
    return [colour_and_count for hand in hands for colour_and_count in hand]

def get_colour_counts(hands):
    hands_list = []
    for hand in hands:
        cubes = hand.split(', ')
        hand = []
        for cube in cubes:
            cube = cube.split(' ')
            colour_and_count = (cube[1], int(cube[0]))
            hand.append(colour_and_count)
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

powers = []

for (i, string) in enumerate(lines):
    game_id, hands = get_hands(i, string)
    hands = get_colour_counts(hands)
    min_cubes = get_min_cubes(hands)
    power = get_power(min_cubes)
    powers.append(power)

answer = sum(powers)
print('Answer: ', answer)