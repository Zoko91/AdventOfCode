with open('input2.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]
blocks = ['seeds', 'seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

def get_block(name):
    block = ""
    found = False
    for line in lines:

        if found:
            if line == '':
                # Stops at end of a block
                break
            # Get other blocks
            block += line + '\n'

        if line.startswith(name):
            if name == 'seeds':
                # Get the first line: seed
                return line.split(':')[1][1:].split(' ')
            else:
                found = True

    return block[:-1].split('\n')

def get_initial_range(initial_seeds):
    range_of_seeds = []
    for i in range(0, len(initial_seeds),2):
        range_of_seeds.append([int(initial_seeds[i]),int(initial_seeds[i])+int(initial_seeds[i+1])])
    return range_of_seeds

def get_new_ranges(seed_range, block_line):
    destination, source, step = map(int, block_line.split(' '))
    source = [source, source + step]
    destination = [destination, destination + step]

    if seed_range[1] < source[0] or seed_range[0] > source[1]:
        return [seed_range]  # No overlapping => return seed

    if seed_range[0] >= source[0] and seed_range[1] <= source[1]:
        gap = seed_range[0] - source[0]  # Gap between seed and source
        gap_range = seed_range[1] - seed_range[0]
        return [[destination[0] + gap, destination[0] + gap + gap_range]]  # Complete overlap return the mapping from seed to destination

    result = []

    # Check for non-overlapping range before y
    if seed_range[0] < source[0]:
        result.append([seed_range[0], min(seed_range[1], source[0]) - 1])

    # Check for the overlapping range
    # START
    start_diff = seed_range[0] - source[0]  # -2
    if start_diff >= 0:
        lower_bound = seed_range[0] - (source[0]-destination[0])
    else:
        lower_bound = destination[0]
    # END
    end_diff = seed_range[1] - source[1]
    if end_diff >= 0:
        upper_bound = destination[1]
    else:
        upper_bound = seed_range[1] - (source[0] -  destination[0])

    overlap = [lower_bound, upper_bound]
    result.append(overlap)

    # Check for non-overlapping range after y
    if seed_range[1] > source[1]:
        result.append([max(seed_range[0], source[1]) + 1, seed_range[1]])

    return result



test = None
seeds_ranges = get_initial_range(get_block(blocks[0]))

for block in blocks[1:]:
    current_block = get_block(block)
    range_updated = []
    print("BLOCK")
    for seed in seeds_ranges:
        for block_line in current_block:
            test = get_new_ranges(seed,block_line)
            print("Seed", seed)
            print("b", block_line)
            print("a", test, '\n')
            if seed != test[0]:
                break
            else:
                continue
        range_updated.extend(test)
    seeds_ranges = range_updated

print("Seeds ranges: ", seeds_ranges)

# Part 2: 231 910 859 too high
print(min(min(seeds_ranges)))
