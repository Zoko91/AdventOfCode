with open('input.txt') as inpt:
    data = inpt.read().strip()

lines = [line for line in data.split('\n')]

def numbers_block(line_index, line):
    val = ''
    val_and_indices = []
    i = 0
    while i < (len(line)):
        if line[i].isdigit():
            val += line[i]
            index = i
            while (i+1<len(line)) and (line[i+1].isdigit()):
                i = i + 1
                val += line[i]
            val_and_indices.append([val,line_index,index])
            val = ''
        i = i + 1
    return val_and_indices

def verify_number(val_index, doc):
    '''
    x x x x
    x 1 2 X
    X X X X
    '''
    verified = []
    for val in val_index:
        l = len(val[0])
        indices_to_check = []
        if val[1] == 0:
            # First row
            if val[2] == 0:
                '''
                1 2 X
                X X X
                '''
                indices_to_check.append([val[1],val[2]+l])
                for test in range(l+1):
                    indices_to_check.append([val[1]+1,val[2]+test])

            elif val[2]+len(val[0]) == len(doc[val[1]]):
                '''
                X 1 2
                X X X
                '''
                indices_to_check.append([val[1],val[2]-1])
                for test in range(l+1):
                    indices_to_check.append([val[1] + 1, val[2] + test - 1])

            else:
                '''
                x 1 2 X
                X X X X
                '''
                indices_to_check.append([val[1], val[2] - 1])
                indices_to_check.append([val[1] ,val[2]+l])
                for test in range(l+2):
                    indices_to_check.append([val[1] + 1, val[2] + test - 1])

        elif val[1] == len(doc)-1:
            # Last row
            if val[2] == 0:
                '''
                X X X
                1 2 X
                '''
                for test in range(l+1):
                    indices_to_check.append([val[1] - 1, val[2] + test])
                indices_to_check.append([val[1], val[2]+l])

            elif val[2]+len(val[0]) == len(doc[val[1]]):
                '''
                X X X
                x 1 2
                '''
                for test in range(l+1):
                    indices_to_check.append([val[1] - 1, val[2] + test - 1])
                indices_to_check.append([val[1], val[2] -1])

            else:
                '''
                X X X X
                x 1 2 X
                '''
                for test in range(l + 2):
                    indices_to_check.append([val[1] - 1, val[2] + test - 1])
                indices_to_check.append([val[1], val[2] - 1])
                indices_to_check.append([val[1], val[2] + l])

        else:
            if val[2]+len(val[0]) == len(doc[val[1]]):
                '''
                 X X X
                 x 1 2
                 X X X
                 '''
                for test in range(l + 1):
                    indices_to_check.append([val[1] - 1, val[2] + test - 1])
                indices_to_check.append([val[1], val[2] - 1])
                for test in range(l + 1):
                    indices_to_check.append([val[1] + 1, val[2] + test - 1])

            else:
                '''
                X X X X
                x 1 2 X
                X X X X
                '''
                for test in range(l + 2):
                    indices_to_check.append([val[1] - 1, val[2] + test - 1])
                indices_to_check.append([val[1], val[2] - 1])
                indices_to_check.append([val[1], val[2] + l])
                for test in range(l + 2):
                    indices_to_check.append([val[1] + 1, val[2] + test - 1])

        for index in indices_to_check:
            # checks if any of the indices to check has a star
            if lines[index[0]][index[1]] == '*':
                verified.append([index[0],index[1],val[0]])
    return verified

p = 0
stars = []
for line in lines:
    val_indices = numbers_block(p, line)
    star_for_line = verify_number(val_indices,lines)
    stars.extend(verify_number(val_indices,lines))
    p += 1

coordinate_values = {}
for star in stars:
    x, y, value = star
    coordinates = (x, y)
    if coordinates not in coordinate_values:
        coordinate_values[coordinates] = []
    coordinate_values[coordinates].append(value)

total_sum_product = 0
for coordinates, values in coordinate_values.items():
    print(f"Coordinates {coordinates}: {values}")
    if len(values) > 1:
        total_sum_product += int(values[0])*int(values[1])


# Part 2: 91031374
print(total_sum_product)
