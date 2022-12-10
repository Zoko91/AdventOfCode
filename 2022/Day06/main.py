# DAY 6

with open('input.txt') as f:
    lignes = f.readlines()

data = lignes[0]

def findIndice(data,num):
    length = len(data)
    for i in range(length):
        if hasAnEqualCharacter(data[i:i+num])==False:
            return i+num

def hasAnEqualCharacter(chaine):
    count = 0
    isManyTime = False
    for i in range(len(chaine)):
        val = 0
        for j in range(len(chaine)):
            if chaine[i] == chaine[j]:
                val += 1
                if val>1:
                    isManyTime = True
                    break
    return isManyTime

# 1st star
print(findIndice(data,14))
# Answer : 1080

# 2nd star
print(findIndice(data,14))
# Answer : 3645







