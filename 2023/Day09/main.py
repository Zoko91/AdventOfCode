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

def predict_inverted(ex_l):
    prediction = 0
    for l in ex_l[::-1]:
        prediction = l[0] - prediction
    return prediction

total = 0
total_inverted = 0
for line in lines:
    ex_line = extrapolate(line)
    total += predict(ex_line)
    total_inverted += predict_inverted(ex_line)

# Part 1: 2043183816
print(total)

# Part 2: 1118
print(total_inverted)
