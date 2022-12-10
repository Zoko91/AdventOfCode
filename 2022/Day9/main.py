# DAY 9

with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [ligne for ligne in data.split('\n')]


def action(H, T):
    dX = abs(H[0]-T[0]) # dX = difference rows
    dY = abs(H[1]-T[1]) # dY = difference cols
    # (if dX and/or dY =1) means it is on an adjacent cell
    up = T[0] > H[0]
    right = T[1] > H[1]
    if dX >= 2 & dY >= 2:
        # because if dX or dY =1 and the other >=2 then it is on the diagonal
        T = (H[0]+1 if up else H[0]-1, H[1]+1 if right else H[1]-1)
    elif dX >= 2:  # straight line configuration
        T = (H[0]+1 if up else H[0]-1, H[1])
    elif dY >= 2:  # straight line configuration
        T = (H[0], H[1]+1 if right else H[1]-1)
    return T


# Initialisation
H = (0, 0)
T = (0, 0)
listT = []
for i in range(9):
    listT.append((0, 0))

position = [(0, 0)]
positionListT = [(0, 0)]

for line in lines:
    direction, nb = line.split()
    col = 0
    row = 0

    if direction == 'U':
        row = 1
    elif direction == 'D':
        row = -1
    elif direction == 'R':
        col = 1
    elif direction == 'L':
        col = -1

    for i in range(int(nb)):
        H = (H[0] + row, H[1]+col)
        T = action(H, T)
        position.append(T)
        for j in range(9):
            if j == 0:
                listT[0] = T
            else:
                listT[j] = action(listT[j-1], listT[j])
        positionListT.append(listT[8])

newList = []
newListT = []
for i in range(len(position)):
    if position[i] not in newList:
        newList.append(position[i])
for i in range(len(positionListT)):
    if positionListT[i] not in newListT:
        newListT.append(positionListT[i])


# 1st star
print(len(newList))
# Answer: 5907

# 2nd star
print(len(newListT))
# Answer:
