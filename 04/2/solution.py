f = open('input.txt')
data = f.read()
lines = data.splitlines()

total_points = 0

def split_card(string):
    numbers = string.split('|')
    numbers[0] = numbers[0].split(': ')[1]
    numbers = [n.split(' ') for n in numbers]
    numbers = [list(filter(lambda x : x != '', n)) for n in numbers]
    numbers = [list(map(lambda x: int(x), n)) for n in numbers]
    winning_numbers = numbers[0]
    my_numbers = numbers[1]

    num_matches = 0
    for num in my_numbers:
        if num in winning_numbers:
            num_matches += 1

    return num_matches

matches = []
for string in lines:
    num_matches = split_card(string)
    matches.append(num_matches)

# f = open('test.txt')
# data = f.read()
# lines = data.splitlines()

# matches = []
# for string in lines:
#     num_matches = split_card(string)
#     matches.append(num_matches)

# print(matches)

# def resolve_card(index, num_matches):
#     print(f'Resolving Card {index + 1} (Matches = {num_matches})')
#     total = 1
#     print(f'Loop from {index + 1} to {index + 1 + num_matches}')
#     for i in range(index + 1, index + 1 + num_matches):
#         print(f'Resolving Card {index + 1}\'s copy of Card {i + 1}')
#         total += resolve_card(i, matches[i])
#     return total

def resolve_card(index, num_matches):
    print(f'Resolving Card {index + 1} (Matches = {num_matches})')
    total = 1
    print(f'Loop from {index + 1} to {index + 1 + num_matches}')
    for i in range(index + 1, index + 1 + num_matches):
        print(f'Resolving Card {index + 1}\'s copy of Card {i + 1}')
        total += resolve_card(i, matches[i])
    return total

total_cards = 0

for index, num_matches in enumerate(matches):
    total_cards += resolve_card(index, num_matches)

print(total_cards)