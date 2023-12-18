from itertools import cycle
from math import lcm

f = open('input.txt')
DATA = f.read()
LINES = DATA.splitlines()

# --- Part One ---

# instructions = [*LINES[0]]
# print(instructions)

# node_dict = {}

# def generate_dict(nodes):
#     for node in nodes:
#         node_key = node[0:3]
#         node_instructions = (node[7:10], node[12:15])
#         node_dict[node_key] = node_instructions

# generate_dict(LINES[2:])

# instructions_cycle = cycle(instructions)

# curr_node = 'AAA'
# num_steps = 0

# while curr_node != 'ZZZ':
#     instruction = next(instructions_cycle)
#     if instruction == 'L':
#         next_node = node_dict[curr_node][0]
#     else:
#         next_node = node_dict[curr_node][1]
#     curr_node = next_node
#     num_steps += 1

# print(num_steps)

# --- Part Two ---

instructions = [*LINES[0]]
print(instructions)

curr_nodes = []
node_dict = {}

def generate_dict_and_curr_nodes(nodes):
    for node in nodes:
        node_key = node[0:3]
        node_instructions = (node[7:10], node[12:15])
        node_dict[node_key] = node_instructions
        if node_key[-1] == 'A':
            curr_nodes.append(node_key)

generate_dict_and_curr_nodes(LINES[2:])

print(curr_nodes)

num_steps_list = []

for curr_node in curr_nodes:
    instructions_cycle = cycle(instructions)
    curr = curr_node
    num_steps = 0
    while curr[-1] != 'Z':
        instruction = next(instructions_cycle)
        if instruction == 'L':
            next_node = node_dict[curr][0]
        else:
            next_node = node_dict[curr][1]
        curr = next_node
        num_steps += 1
    num_steps_list.append(num_steps)

print(num_steps_list)
print(lcm(*num_steps_list))