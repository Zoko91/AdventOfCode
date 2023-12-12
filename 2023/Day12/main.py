with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]

def parse_input(line):
    conditions, groups = line.split(' ')
    groups = list(map(int,groups.split(',')))
    return conditions, groups

def find_combinations(cond, grp):
    '''
    Recursive function to explore all possibilities based on current letter of condition (., #, ?)
    - If '.' or '?'
        => move to the next character and continue the recursion
    - If '#' or '?'
        => checks if group size is valid and there is no '.' before the group
        => recursively explore possibilities for  remaining parts of cond and remaining groups
    '''
    if not cond:
        if not grp:
            return 1
        else:
            return 0
    if not grp:
        if '#' in cond:
            return 0
        else:
            return 1

    result = 0
    if cond[0] in ".?":
        result += find_combinations(cond[1:], grp)

    if cond[0] in "#?":
        if grp[0] <= len(cond): # if length of current group not matching with the needed length then continue...
            if "." not in cond[:grp[0]]: # if no '.' in the next length of block then still in current block, all good
                if grp[0] == len(cond) or cond[grp[0]] != "#": # if end of block and not a # but rather . or ? then good
                    result += find_combinations(cond[grp[0] + 1:], grp[1:])

    return result

total = 0
for line in lines:
    condition, group = parse_input(line)
    total += find_combinations(condition, group)

# Part 1: 7169
print(total)
