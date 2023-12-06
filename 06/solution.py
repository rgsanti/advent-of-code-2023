f = open('input.txt')
DATA = f.read()
LINES = DATA.splitlines()

# --- Part One ---

def get_values(string):
    values_string = string.split(': ')[1]
    values_string = values_string.split(' ')
    values = filter(lambda x: not x == '', values_string)
    values = [int(value) for value in values]
    return values

def get_times_and_distances(lines):
    times = get_values(lines[0])
    distances = get_values(lines[1])
    return times, distances

def calculate_num_ways(time, distance):
    num_ways = 0
    for i in range(1, time):
        if i * (time - i) > distance:
            num_ways += 1
    return num_ways

def calculate_array_product(array):
    result = array[0]
    for value in array[1:]:
        result *= value
    return result

def part_one():
    num_ways_array = []
    times, distances = get_times_and_distances(LINES)
    for (time, distance) in zip(times, distances):
        num_ways = calculate_num_ways(time, distance)
        num_ways_array.append(num_ways)
    answer = calculate_array_product(num_ways_array)
    print(f'Part One: {answer}')

part_one()

# --- Part Two ---

def get_value(string):
    string = string.split(': ')[1]
    string = string.split(' ')
    value_chars = filter(lambda x: not x == '', string)
    value_string = ('').join(value_chars)
    value = int(value_string)
    return value

def get_time_and_distance(lines):
    time = get_value(lines[0])
    distance = get_value(lines[1])
    return time, distance

def get_min_charge_time(time, distance):
    for i in range(1, time):
        if i * (time - i) > distance:
            return i
        
def get_max_charge_time(time, distance):
    for i in range(time, 1, -1):
        if i * (time - i) > distance:
            return i
        
def part_two():
    time, distance = get_time_and_distance(LINES)
    minimum = get_min_charge_time(time, distance)
    maximum = get_max_charge_time(time, distance)
    answer = 1 + maximum - minimum
    print(f'Part Two: {answer}')

part_two()