with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]

def parse_input(doc):
    times = list(map(int,doc[0].split(':')[1].replace('  ', '').strip().split(' ')))
    distances = list(map(int, doc[1].split(':')[1].replace('  ', '').strip().split(' ')))
    return times, distances


def get_distance(time, max_dist):
    how_many = 0
    for hold in range(1, time,1):
        remaining_time = time - hold
        d = remaining_time * hold
        if d > max_dist:
            how_many += 1
    return how_many

# --- 1 ---
times, distances = parse_input(lines)
total = 1
i = 0
for i in range(len(distances)):
    total *= get_distance(times[i], distances[i])

# --- 2 ---
time, distance = parse_input(lines)
time = int(''.join(map(str, time)))
distance = int(''.join(map(str, distance)))

# Part1: 3316275
print(total)

# Part2: 27102791
print(get_distance(time,distance))
