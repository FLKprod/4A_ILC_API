from flask import Flask
from flask import request
import json
import csv

class Personne:
    def __init__(self, nom:str, solde:float):
        self.nom=nom
        self.solde=solde
    def reception(self, somme:float):
        self.solde+=somme
    def debit(self, somme:float):
        self.solde-=somme
        
class Transaction:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    def __init__(self, P1:Personne, P2:Personne, t,s):
        self.P1 = P1
        self.P2 = P2
        self.t = t
        self.s = s

tab = []
#Ouverture du fichier CSV
with open('data.csv', newline='', encoding="utf-8-sig") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for rows in row:
            p = (str(rows).split(';'))
            tab.append(p)
transac = []

for i in range(1, 7):
    p1=Personne(tab[i][0],5000)
    p2=Personne(tab[i][1],4000)
    tempsT = tab[i][2]
    sommeS = tab[i][3]
    transac.append(Transaction(p1, p2, tempsT, sommeS))


dict = {0:transac[0], 1:transac[1]}

