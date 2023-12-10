with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = ['.' + line + '.' for line in data.split('\n')]
# Lines is a table of row elements
# It starts at position (0,0) and ends at position (139,139)

# Adds padding because lazy to deal with exceptions
pad = ''.join(['.' for _ in range(len(lines[0]))])
lines.insert(0, pad)
lines.append(pad)
length = len(lines)
# Tables containing the distance of both paths from the start
start = [[None] * length for _ in range(length)]
end = [[None] * length for _ in range(length)]

def get_starting_point(doc):
    for i, row in enumerate(doc):
        if 'S' in row:
            return i, row.index('S')

def get_max_dist(tab1, tab2):
    odd = 0
    # Difference between tab1 and tab2 where there is no None
    # If there is a 0 then the paths have even distances, if it is 1 then the paths have odd distances
    for i in range(len(tab1)):
        for j in range(len(tab2)):
            if tab1[i][j] is not None and tab2[i][j] is not None:
                if abs(tab1[i][j]-tab2[i][j]) == 0:
                    return tab1[i][j]
                elif abs(tab1[i][j]-tab2[i][j]) == 1:
                    odd = min(tab1[i][j], tab2[i][j])
    return odd


def get_next_direction(coordX, coordY, prev, doc):
    north, south, west, east = (coordX-1, coordY), (coordX+1, coordY), (coordX, coordY-1), (coordX, coordY+1)
    current_step = doc[coordX][coordY]
    if current_step == '-':
        if prev == west:
            return coordX, coordY + 1
        else:
            return coordX, coordY - 1

    elif current_step == '|':
        if prev == north:
            return coordX + 1, coordY
        else:
            return coordX - 1, coordY

    elif current_step == 'L':
        if prev == north:
            return coordX, coordY + 1
        else:
            return coordX - 1, coordY

    elif current_step == 'J':
        if prev == north:
            return coordX, coordY - 1
        else:
            return coordX - 1, coordY

    elif current_step == '7':
        if prev == south:
            return coordX, coordY - 1
        else:
            return coordX + 1, coordY

    elif current_step == 'F':
        if prev == south:
            return coordX, coordY + 1
        else:
            return coordX + 1, coordY

    elif current_step == 'S':
        list_of_possibles = []
        north, south, west, east = doc[coordX - 1][coordY], doc[coordX + 1][coordY], doc[coordX][coordY - 1], doc[coordX][coordY + 1]
        if north == '7' or north == '|' or north == "F":
            list_of_possibles.append((coordX - 1, coordY))
        if south == 'L' or south == 'J' or south == '|':
            list_of_possibles.append((coordX + 1, coordY))
        if west == '-' or west == 'L' or west == 'F':
            list_of_possibles.append((coordX, coordY - 1))
        if east == '-' or east == '7' or east == 'J':
            list_of_possibles.append((coordX, coordY + 1))
        return list_of_possibles

    return 'S'

def print_table(table):
    for row in table:
        formatted_row = " ".join(str(cell) if cell is not None else '.' for cell in row)
        print(formatted_row)


def path(starting_point, table_distances, doc):
    prev = get_starting_point(lines)
    distance = 1
    table_distances[starting_point[0]][starting_point[1]] = distance
    next_direction = starting_point
    while True:
        distance += 1
        to_handle_prev = next_direction
        next_direction = get_next_direction(next_direction[0], next_direction[1], prev, doc)
        next_direction_value = doc[next_direction[0]][next_direction[1]]
        if next_direction_value == 'S':
            break
        table_distances[next_direction[0]][next_direction[1]] = distance
        prev = (to_handle_prev[0],to_handle_prev[1])

    return table_distances

startX, startY = get_starting_point(lines)
first_circuit, second_circuit = get_next_direction(startX, startY, None, lines)
start = path(first_circuit, start, lines)
end = path(second_circuit, end, lines)

print("---------------------")
print_table(start)
print("---------------------")
print_table(end)

# Part 1: 6838
print(get_max_dist(start, end))
