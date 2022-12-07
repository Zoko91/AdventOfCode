# DAY 7

with open('input.txt') as inp:
    lignes = inp.readlines()
for i in range(len(lignes)):
    lignes[i] = lignes[i].rstrip()

class File:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.children = []
        self.parent = None

    def __str__(self):
        return f"Name: {self.name}, size is {self.size}"


sizes = {}
firstFile = File('/')
f = firstFile

for i in range(len(lignes)):

    if lignes[i].startswith('$'):
        cmdLine = lignes[i].split()
        ## Récupère toutes les parties de la ligne

        if cmdLine[1] == 'cd':
            ## Récupère le nom du dossier de la ligne

            if cmdLine[2] == '..':
                ## si c'est un cmd .. alors
                f = f.parent

            else:
                file = File(cmdLine[2])
                file.parent = f
                f.children.append(file)
                f = file

    else:
        size, name = lignes[i].split()
        if size != 'dir':
            file = File(name, int(size))
            f.children.append(file)


def getDirSize(data):

    if not data.children:
        return data.size
    totalsize = 0
    for child in data.children:
        totalsize += getDirSize(child)
    sizes[data] = totalsize
    return totalsize

getDirSize(firstFile) # Pour remplir sizes
print(len(sizes)) # taille de sizes

# 1st star
print(sum(sizeFile for sizeFile in sizes.values() if sizeFile < 100000)) # parcourt chaque valeur du dictionnaire
# Answer : 1908462
