import csv

transac = []
class Transaction:
    
    def __init__(self, P1, P2, t,s):
        self.P1 = P1
        self.P2 = P2
        self.t = t
        self.s = s

tab = []
     #Ouverture du fichier CSV
with open('data.csv', newline='', encoding="utf-8-sig"  ) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for rows in row:
            print(rows)
            p = (str(rows).split(';'))
            tab.append(p)
    
    #print(tab[1][2])

print(tab[4][1])
for i in range(1, 7):
    nomP1 = tab[i][0]
    nomP2 = tab[i][1]
    tempsT = tab[i][2]
    sommeS = tab[i][3]
    transac.append(Transaction(nomP1, nomP2, tempsT, sommeS))

print(transac[1].t)

