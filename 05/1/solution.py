f = open('input.txt')
data = f.read()
lines = data.splitlines()

def get_seeds(string):
    numbers = string.split(': ')[1]
    seeds = [int(char) for char in numbers.split(' ')]
    return seeds

seeds = get_seeds(lines[0])

map_dict = {}

curr_map = ''
for string in lines[2:]:
    if len(string) == 0:
        continue
    if 'map' in string:
        map_dict[string] = []
        curr_map = string
        continue
    map_tuple = tuple([int(char) for char in string.split(' ')])
    map_dict[curr_map].append(map_tuple)

def get_mapped_value(value, maps):
    for map in maps:
        dest_start, source_start, range_length = map
        if source_start <= value < source_start + range_length:
            mapped_value = dest_start + (value - source_start)
            return mapped_value
    return value

location_numbers = []

for seed in seeds:
    print(f'Processing Seed: {seed}')
    running_value = seed
    for mapping in map_dict.keys():
        running_value = get_mapped_value(running_value, map_dict[mapping])
    print(f'Location Number: {running_value}')
    location_numbers.append(running_value)

print(min(location_numbers))