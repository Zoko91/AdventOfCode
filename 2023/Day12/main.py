with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]

def parse_input(line):
    conditions, groups = line.split(' ')
    groups = tuple(map(int,groups.split(',')))
    return conditions, groups

def find_combinations(cond, grp):
    '''
    The function recursively explores all possibilities
    - If Condition is empty, return 1 if there are no remaining groups otherwise return 0.
    - If no remaining groups, return 0 if '#' is present in the condition otherwise return 1 because incompatible !
    - Explore possibilities based on condition[0]:
        - If '.' or '?'
         => move to the next character and continue the recursion.
        - If '#' or '?'
         => Checks if group size is valid and there is no '.' before the group
         => Recursively explore possibilities for  remaining parts of cond and remaining groups
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
        if grp[0] <= len(cond) \
                and "." not in cond[:grp[0]] \
                and (grp[0] == len(cond)
                     or cond[grp[0]] != "#"):
            result += find_combinations(cond[grp[0] + 1:], grp[1:])

    return result

total = 0
for line in lines:
    condition, group = parse_input(line)
    total += find_combinations(condition, group)

# Part 1: 7169
print(total)
