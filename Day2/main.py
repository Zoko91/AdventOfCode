# DAY 2
def calculRPS1(a,b):
  somme = 0
  if (b == 'Y'):
    somme += 2
  elif (b == 'X'):
    somme += 1
  elif (b == 'Z'):
    somme += 3
  if (a == 'A'):
    if (b=='X'):
      somme += 3
    elif (b=='Y'):
      somme += 6
    elif (b=='Z'):
      somme += 0
  elif (a == 'B'):
    if (b=='X'):
      somme += 0
    elif (b=='Y'):
      somme += 3
    elif (b=='Z'):
      somme += 6
  elif (a == 'C'):
    if (b=='X'):
      somme += 6
    elif (b=='Y'):
      somme += 0
    elif (b=='Z'):
      somme += 3
  return(somme)

def calculRPS2(a,b):
  somme = 0
  if (a == 'A'):
    if (b=='X'):
      somme += 3
    elif (b=='Y'):
      somme += 4
    elif (b=='Z'):
      somme += 8
  elif (a == 'B'):
    if (b=='X'):
      somme += 1
    elif (b=='Y'):
      somme += 5
    elif (b=='Z'):
      somme += 9
  elif (a == 'C'):
    if (b=='X'):
      somme += 2
    elif (b=='Y'):
      somme += 6
    elif (b=='Z'):
      somme += 7
  return(somme)


with open('input.txt') as f:
    lines = f.readlines()
print("Somme 1")
sum = 0
for i in range(len(lines)):
    sum += calculRPS1(lines[i][0],lines[i][2])

print(sum)
print("Somme 2")
sum2 = 0
for i in range(len(lines)):
    sum2 += calculRPS2(lines[i][0],lines[i][2])
print(sum2)
