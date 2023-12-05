f = open('input.txt')
data = f.read()
lines = data.splitlines()

def get_seeds(string):
    numbers = string.split(': ')[1]
    seeds = [int(char) for char in numbers.split(' ')]
    return seeds

seeds = get_seeds(lines[0])

def get_seed_ranges(first_val, range_length):
    return (first_val, first_val + range_length)

seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append(get_seed_ranges(seeds[i], seeds[i+1]))

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

def get_mapped_values(value_ranges, maps, map_name):
    mapped_ranges = []

    for value_range in value_ranges:

        for mapping in maps:
            dest_start, source_start, range_length = mapping
            source_end = source_start + range_length

            mapped_range = None

            if (value_range[0] < source_end and value_range[1] >= source_start):
                candidate_range = (max(value_range[0], source_start), min(value_range[1], source_end))
                mapped_range = ((dest_start + (candidate_range[0] - source_start)), dest_start + (candidate_range[1] - source_start))

            if mapped_range is not None:
                mapped_ranges.append(mapped_range)

    if (len(mapped_ranges) > 0):
        if 'humidity-to-location' in map_name:
            mapped_ranges += value_ranges
        return mapped_ranges
    else:
        return value_ranges

location_number_ranges = []
for seed_range in seed_ranges:
    running_ranges = [seed_range]
    for mapping in map_dict.keys():
        if len(running_ranges) == 0:
            continue
        running_ranges = get_mapped_values(running_ranges, map_dict[mapping], mapping)
    for running_range in running_ranges:
        location_number_ranges.append(running_range)

print(f'Answer: {min(x[0] for x in location_number_ranges)}')