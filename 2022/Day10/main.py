# DAY 10

with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]

cycles = ['1']
X = 1
CRT = " # "
countCRT = 1
for line in lines:
    if line.startswith('addx'):
        instruction, val = line.split()
        # One cycle
        if countCRT in [X-1, X, X+1]:
            CRT += " # "
        else:
            CRT += " . "
        cycles.append(str(X))
        countCRT += 1
        if countCRT == 40:
            CRT += '\n'
            countCRT = 0

        # Second cycle
        X += int(val)
        if countCRT in [X-1, X, X+1]:
            CRT += " # "
        else:
            CRT += " . "
        countCRT += 1
        if countCRT == 40:
            CRT += '\n'
            countCRT = 0
        cycles.append(str(X))
    else:
        # Noop takes one cycle
        if countCRT in [X-1, X, X+1]:
            CRT += " # "
        else:
            CRT += " . "
        countCRT += 1
        if countCRT == 40:
            CRT += '\n'
            countCRT = 0
        cycles.append(str(X))


signalStrength = 0
for i in range(20, 221, 40):
    signalStrength += int(cycles[i-1])*i

# 1st star
print(signalStrength)
# Answer: 12980 non et non plus 14760


# 2nd star
CRT.split('\n')
print(CRT)
# Answer:


