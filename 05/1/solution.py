f = open('test.txt')
data = f.read()
lines = data.splitlines()

# Get seed numbers

seeds = [int(char) for char in lines[0].split(': ')[1].split(' ')]

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

for key in map_dict:
    print(key)
    print(map_dict[key])

