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

    print(f'Winning Numbers: {winning_numbers}')
    print(f'My Numbers: {my_numbers}')

    num_matches = 0
    for num in my_numbers:
        if num in winning_numbers:
            num_matches += 1

    if num_matches <= 1:
        return num_matches
    else:
        result = 1
        for _ in range(1, num_matches):
            result *= 2

    return result

for string in lines:
    points = split_card(string)
    total_points += points

print('Answer: ', total_points)