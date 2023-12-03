f = open('input.txt')
data = f.read()
lines = data.splitlines()

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
        colour_and_count = (cube[1], cube[0])
        hand.append(colour_and_count)

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

valid_game_ids = []
for (i, string) in enumerate(lines):
    game_id, hands = get_hands(i, string)
    if (is_game_valid(hands)):
        valid_game_ids.append(game_id)

answer = sum(valid_game_ids)
print('Answer: ', answer)