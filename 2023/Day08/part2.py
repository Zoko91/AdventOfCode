with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]


def parse_input(doc):
    directions = doc[0]
    maps = [line.replace('(','').replace(')','').split(' = ') for line in doc[2:]]
    maps = [[line[0]] + line[1].split(', ') for line in maps]
    return directions, maps

def get_next_position(instruction, network, node):
    for line in network:
        if line[0] == node:
            if instruction == "L":
                return line[1]
            else:
                return line[2]

def get_nodes_part_start(network):
    nodes = []
    for line in network:
        if line[0][2] == "A":
            nodes.append(line[0])
    return nodes

def verify_nodes_ending(node):
    if node.endswith("Z"):
        return True
    return False

directions, maps = parse_input(lines)
nodes = get_nodes_part_start(maps)

loops = []
for node in nodes:
    loop = 1
    while loop < 1000000000000:
        node = get_next_position(directions[(loop-1)%len(directions)], maps, node)
        if verify_nodes_ending(node):
            loops.append(loop)
            break
        loop += 1

def least_common_multiple(nb1, nb2):
    init_x = nb1
    init_y = nb2
    # PGCD
    while nb2:
        nb1, nb2 = nb2, nb1 % nb2
    # LCM
    return (init_x*init_y)//nb1

lcm = 1
for nb in loops:
    lcm = least_common_multiple(lcm,nb)


# Part 2: 12357789728873
print(lcm)
