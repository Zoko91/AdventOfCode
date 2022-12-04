# DAY 1
with open('input.txt') as f:
  s = " ".join([l.rstrip() for l in f])

dataSplitted = s.split("  ")

for w in range (len(dataSplitted)):
    dataSplitted[w] = dataSplitted[w].split(" ")

top1 = 2
top2 = 1
top3 = 0

for i in range(len(dataSplitted)):
    sumCal = 0
    for j in range(len(dataSplitted[i])):
        sumCal += int(dataSplitted[i][j])
    if top3 < sumCal:
        if top2 < sumCal:
            if top1 < sumCal:
                top1 = sumCal
            else:
                top2 = sumCal
        else:
            top3 = sumCal
print(top1)
print(top2)
print(top3)
somme = top1+top2+top3
print(somme)
