with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]


def parse_input(doc):
    '''
    Directions: LR ...
    Maps: ['input_network', 'left_network', 'right_network']
    '''
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

distance = 0
directions, maps = parse_input(lines)
current_node = "AAA"

while not (current_node == "ZZZ"):
    current_node = get_next_position(directions[distance%len(directions)], maps, current_node)
    distance += 1


# Part 1:
print(distance)
