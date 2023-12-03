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
    verified = 0
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
            # checks if any of the indices to check has a special char
            if (lines[index[0]][index[1]] != '.') and (lines[index[0]][index[1]].isdigit() == False):
                verified += int(val[0])
                break
    return verified

p = 0
total_value = 0
for line in lines:
    val_indices = numbers_block(p, line)
    value_to_add = verify_number(val_indices,lines)
    total_value += value_to_add
    p += 1

# Part 1: 546563
print(total_value)
