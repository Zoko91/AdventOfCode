# DAY 8

with open('input.txt') as inpt:
    lignes = inpt.readlines()
for i in range(len(lignes)):
    lignes[i] = lignes[i].rstrip()

numberOfTress = 0

for i in range(99):
    val = str(lignes[i])
    for j in range(99):
        data = val[j]
        ####################### Need optimize
        isVisibleHaut = True
        isVisibleBas = True
        isVisibleGauche = True
        isVisibleDroit = True
        #######################
        for haut in range(i-1, -1, -1):
            if str(lignes[haut])[j] >= data:
                isVisibleHaut = False
                break
        for bas in range(i+1, 99, 1):
            if str(lignes[bas])[j] >= data:
                isVisibleBas = False
                break
        for gauche in range(j-1, -1, -1):
            if str(lignes[i])[gauche] >= data:
                isVisibleGauche = False
                break
        for droite in range(j+1, 99, 1):
            if str(lignes[i])[droite] >= data:
                isVisibleDroit = False
                break
        if isVisibleDroit + isVisibleGauche + isVisibleHaut + isVisibleBas >0:
            numberOfTress += 1

# 1st star
print(numberOfTress)
# Answer : 1901 is too high

