with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [list(map(int, line.split(' '))) for line in data.split('\n')]

def extrapolate(line):
    extra_list = [line]
    extra_current = line
    while not all(e == 0 for e in extra_current):
        extra_current = [extra_current[i] - extra_current[i-1] for i in range(1, len(extra_current))]
        extra_list.append(extra_current)
    return extra_list

def predict(ex_l):
    prediction = 0
    for l in ex_l[::-1]:
        prediction += l[-1]
    return prediction

total = 0
for line in lines:
    total += predict(extrapolate(line))

# Part 1: 2043183816
print(total)

