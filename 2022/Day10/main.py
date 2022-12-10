# DAY 10

with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]
print(lines)

cycles = ['1']
X = 1
for line in lines:
    if line.startswith('addx'):
        instruction, val = line.split()
        cycles.append(str(X))
        X += int(val)
        cycles.append(str(X))
    else:
        cycles.append(str(X))

print(cycles)

signalStrength = 0
for i in range(20, 221, 40):
    print(i)
    print(cycles[i-1])
    print("------------------")
    signalStrength += int(cycles[i-1])*i

# 1st star
print(signalStrength)
# Answer: 12980 non et non plus 14760


# 2nd star

# Answer:


