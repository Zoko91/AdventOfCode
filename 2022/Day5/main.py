# DAY 5

# Opens the document and selects every line
with open('input.txt') as f:
    lignes = f.readlines()

# Dictionnary of characters
dictionnary = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Extract list is a method that selects the char from the piles and creates as much list as there are piles
def extractList (data):
    tab = data[0:9]
    lenTab = len(tab)
    res = []
    taille = int(tab[8][-3])
    for i in range(taille):
        val = 1+4*i
        liste = []
        for j in range(lenTab-1):
            if(tab[j][val] in dictionnary):
                liste.append(tab[j][val])
        liste.reverse()
        res.append(liste)
    return res

def instructions(data,piles):
    tab = data[10:]
    for i in range(len(tab)):
        tab[i] = tab[i].rstrip().split(' ')
        moveCrates(piles, int(tab[i][1]), int(tab[i][3])-1, int(tab[i][5])-1)
    return piles

def moveCrates(piles,x,a,b):
    for i in range(x):
        if(len(piles[a])>0):
            val = piles[a].pop()
            piles[b].append(val)

# Extract the top crate of each pile
def extractTopCrate(listes):
    res = ''
    for i in range(len(listes)):
        res += listes[i][-1]
    return res

# 1 star
print(extractTopCrate(instructions(lignes,extractList(lignes))))
# Answer: WHTLRMZRC

