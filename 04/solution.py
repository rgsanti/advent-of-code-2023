f = open('input.txt')
DATA = f.read()
LINES = DATA.splitlines()

# --- Part One ---

def get_numbers(card):
    strings = card.split(': ')[1]
    char_lists = [s.split(' ') for s in strings.split('|')]
    number_char_lists = [filter(lambda x : x != '', cl) for cl in char_lists]
    numbers = [list(map(lambda x: int(x), ncl)) for ncl in number_char_lists]
    [winning_numbers, drawn_numbers] = numbers
    return winning_numbers, drawn_numbers

def calculate_points(winning_numbers, drawn_numbers):
    num_matches = 0
    for num in drawn_numbers:
        if num in winning_numbers:
            num_matches += 1

    if num_matches <= 1:
        return num_matches
    else:
        points = 1
        for _ in range(1, num_matches):
            points *= 2

    return points

def part_one():
    total_points = 0
    for card in LINES:
        winning_numbers, drawn_numbers = get_numbers(card)
        points = calculate_points(winning_numbers, drawn_numbers)
        total_points += points
    print(f'Part One: {total_points}')

part_one()

# --- Part Two ---

def get_num_matches(winning_numbers, drawn_numbers):
    num_matches = 0
    for num in drawn_numbers:
        if num in winning_numbers:
            num_matches += 1
    return num_matches

def generate_matches_array(cards):
    matches = []
    for card in cards:
        winning_numbers, drawn_numbers = get_numbers(card)
        num_matches = get_num_matches(winning_numbers, drawn_numbers)
        matches.append(num_matches)
    return matches

MATCHES = generate_matches_array(LINES)

def resolve_card(index, num_matches):
    total = 1
    for i in range(index + 1, index + 1 + num_matches):
        total += resolve_card(i, MATCHES[i])
    return total

def part_two():
    total_cards = 0
    for index, num_matches in enumerate(MATCHES):
        total_cards += resolve_card(index, num_matches)
    print(f'Part Two: {total_cards}')

part_two()