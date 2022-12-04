# DAY 3
dictionnary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
               'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

somme = 0
with open('input.txt') as f:
    lines = f.readlines()

for i in range (0,len(lines),3):
    line = lines[i]+lines[i+1]+lines[i+2]
    line = line.split('\n')
    for j in range (len(line[0])):
        if(line[0][j] in line[1]):
            if (line[0][j] in line[2]):
                somme += dictionnary.index(line[0][j])+1
                break
print(somme)
