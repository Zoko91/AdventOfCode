# DAY 11 2nd star

with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n\n')]

itemsVisited = [0 for i in range(8)]
mnumber = []
mval = []
operator = []
value = []
divisibleBy = []
ifTrue = []
ifFalse = []

# Data processing
for line in lines:
    minfos = line.split('\n')                                   # Example of data collecting
    mnumber.append(int(minfos[0].split()[1][0]))                # Monkey 0:
    mvalues = minfos[1].split(": ")[1].split(", ")              # Starting items: 65, 58, 93, 57, 66
    op, val = minfos[2].split("= old ")[1].split(' ')           # Operation: new = old * 7
    divisibleBy.append(int(minfos[3].split("by ")[1]))          # Test: divisible by 19
    ifTrue.append(int(minfos[4].split(' ')[9]))                 # If true: throw to monkey 6
    ifFalse.append(int(minfos[5].split(' ')[9]))                # If false: throw to monkey 4
    operator.append(op)
    value.append(val)
    mval.append(mvalues)


trackingModulo = 1
for val in divisibleBy:
    trackingModulo = (trackingModulo*val)

# Loop of 20 rounds
for i in range(10000):                                 # i for loop
    for j in range(len(lines)):                     # j for monkeys
        lenloop = len(mval[j])
        for k in range(lenloop):                    # k for item
            worry = 0
            if operator[j] == '*':
                if value[j] == 'old':
                    worry = int(mval[j][0]) * int(mval[j][0])
                else:
                    worry = int(mval[j][0]) * int(value[j])
            else:
                if value[j] == 'old':
                    worry = int(mval[j][0]) * 2
                else:
                    worry = int(mval[j][0]) + int(value[j])

            mval[j].pop(0)
            worry %= trackingModulo

            if worry % divisibleBy[j] == 0:
                mval[ifTrue[j]].append(str(worry))
            else:
                mval[ifFalse[j]].append(str(worry))
            itemsVisited[j] += 1

# Second star
itemsVisited.sort()
print(itemsVisited[-2]*itemsVisited[-1])
# Answer: 14081365540
