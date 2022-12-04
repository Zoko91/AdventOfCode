# DAY 4

# defining functions

# Function for star 1
def howManyContained(lines):

    compteur = 0
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].split(',')
        # [['49-51', '31-50'],...]
        num1 = lines[i][0].split('-')
        num2 = lines[i][1].split('-')
        # num1 = ['49','51']
        # num2 = ['31','50']
        if int(num1[0]) == int(num2[0]):
            compteur += 1

        elif int(num1[1]) == int(num2[1]):
            compteur += 1

        elif int(num1[0]) < int(num2[0]):
            if int(num1[1]) > int(num2[1]):
                compteur += 1

        elif int(num2[0]) < int(num1[0]):
            if int(num2[1]) > int(num1[1]):
                compteur += 1

    return compteur

# Function for star 2
def howManyPairs(lines):

    compteur = 0
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].split(',')
        # [['49-51', '31-50'],...]
        num1 = lines[i][0].split('-')
        num2 = lines[i][1].split('-')
        # num1 = ['49','51']
        # num2 = ['31','50']
        if int(num2[0]) <= int(num1[0]) <= int(num2[1]):
            compteur += 1
        elif int(num2[0]) <= int(num1[1]) <= int(num2[1]):
            compteur += 1
        elif int(num1[0]) <= int(num2[0]) <= int(num1[1]):
            compteur += 1
        elif int(num1[0]) <= int(num2[1]) <= int(num1[1]):
            compteur += 1
    return compteur

# importing data
with open('input.txt') as f:
    lignes = f.readlines()

####################################
# First star
# print(howManyContained(lignes))
# Answer : 453
####################################
# Second star
# print(howManyPairs(lignes))
# Answer : 919

