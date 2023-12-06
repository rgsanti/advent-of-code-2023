f = open('input.txt')
DATA = f.read()
LINES = DATA.splitlines()

# --- Part One ---

def get_seeds(string):
    numbers = string.split(': ')[1]
    seeds = [int(char) for char in numbers.split(' ')]
    return seeds

def generate_map_dict(lines):
    map_dict = {}
    curr_map = ''
    for string in lines:
        if len(string) == 0:
            continue
        if 'map' in string:
            map_dict[string] = []
            curr_map = string
            continue
        map_tuple = tuple([int(char) for char in string.split(' ')])
        map_dict[curr_map].append(map_tuple)
    return map_dict    

def get_mapped_value(value, maps):
    for (dest_start, source_start, range_length) in maps:
        if source_start <= value < source_start + range_length:
            mapped_value = dest_start + (value - source_start)
            return mapped_value
    return value

def get_location_numbers(seeds, map_dict):
    location_numbers = []
    for seed in seeds:
        running_value = seed
        for mapping in map_dict.keys():
            running_value = get_mapped_value(running_value, map_dict[mapping])
        location_numbers.append(running_value)
    return location_numbers

def part_one():
    seeds = get_seeds(LINES[0])
    map_dict = generate_map_dict(LINES[2:])
    location_numbers = get_location_numbers(seeds, map_dict)
    answer = min(location_numbers)
    print(f'Part One: {answer}')

part_one()

# --- Part Two ---

def get_seed_ranges(seeds):
    seed_ranges = []

    for i in range(0, len(seeds), 2):
        seed_range_start = seeds[i]
        seed_range_length = seeds[i+1]
        seed_range = (seed_range_start, seed_range_start + seed_range_length)
        seed_ranges.append(seed_range)

    return seed_ranges

def get_mapped_range(value_range, map):
    dest_start, source_start, range_length = map
    source_end = source_start + range_length
    mapped_range = None

    if (value_range[0] < source_end and value_range[1] >= source_start):
        candidate_range = (max(value_range[0], source_start), min(value_range[1], source_end))
        mapped_range = ((dest_start + (candidate_range[0] - source_start)), dest_start + (candidate_range[1] - source_start))

    return mapped_range

def get_mapped_ranges(value_ranges, maps, map_name):
    mapped_ranges = []

    for value_range in value_ranges:
        for map in maps:
            mapped_range = get_mapped_range(value_range, map)
            if mapped_range is not None:
                mapped_ranges.append(mapped_range)

    if (len(mapped_ranges) > 0):
        if 'humidity-to-location' in map_name:
            mapped_ranges += value_ranges
        return mapped_ranges
    else:
        return value_ranges

def part_two():
    seeds = get_seeds(LINES[0])
    seed_ranges = get_seed_ranges(seeds)
    map_dict = generate_map_dict(LINES[2:])

    location_number_ranges = []
    for seed_range in seed_ranges:
        running_ranges = [seed_range]
        for mapping in map_dict.keys():
            if len(running_ranges) == 0:
                continue
            running_ranges = get_mapped_ranges(running_ranges, map_dict[mapping], mapping)
        for running_range in running_ranges:
            location_number_ranges.append(running_range)

    answer = min(x[0] for x in location_number_ranges)
    print(f'Part Two: {answer}')

part_two()