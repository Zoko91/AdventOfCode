with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]

def expending_universe(galaxy):
    # Expand galaxy if no #
    new_galaxy = []

    # For rows
    for row in galaxy:
        if '#' not in row:
            new_galaxy.append(row)
            new_galaxy.append('.' * len(row))
        else:
            new_galaxy.append(row)

    num_rows = len(new_galaxy)
    num_columns = len(new_galaxy[0])

    new_new_galaxy = new_galaxy.copy()
    added_columns = 0

    # For columns
    for i in range(num_columns):
        column = ''.join(new_galaxy[j][i] for j in range(num_rows))
        if '#' not in column:
            for j in range(num_rows):
                new_new_galaxy[j] = new_new_galaxy[j][:i + added_columns] + '.' + new_new_galaxy[j][i + added_columns:]
            # Update the added_columns count
            added_columns += 1

    return new_new_galaxy

def get_star_positions(univ):
    position = []
    for i, row in enumerate(univ):
        for j, cell in enumerate(row):
            if cell == '#':
                position.append((i, j))
    return position

def get_manhattan_distance(position1, position2):
    return abs(position2[0] - position1[0]) + abs(position2[1] - position1[1])

universe = expending_universe(lines)
positions = get_star_positions(universe)

distance = 0
for i in range(0, len(positions)):
    for j in range(i + 1, len(positions)):
        distance += get_manhattan_distance(positions[i], positions[j])

# Part 1: 9329143
print(distance)


