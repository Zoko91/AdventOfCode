with open('input.txt') as inpt:
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

def mapping_to_result(block, seed):
    for line in block:
        destination, source, step = map(int, line.split(' '))
        upper_bound_source = source + step
        if source <= seed <= upper_bound_source:
            return str(destination + (seed-source)) # destination + current step
    return str(seed)

seeds = get_block(blocks[0])
for block in blocks[1:]:
    current_block = get_block(block)
    results = []
    for seed in seeds:
        results.append(mapping_to_result(current_block, int(seed)))
    seeds = results

seeds = [int(seed) for seed in seeds]

# Part1 : 196167384
print(min(seeds))
