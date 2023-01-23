from flask import Flask
from flask import request
import json
import sys
import csv

app = Flask(__name__)

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
    def __init__(self,P1:Personne,P2:Personne,t:str,s:float):
        self.P1=P1
        self.P2=P2
        self.t=t
        self.s=s

#Création des comptes
p1=Personne("jean",5000)
p2=Personne("louis",4000)
p3=Personne("Paul",4000)
p4=Personne("Luke",4000)
p5=Personne("Jean",4000)
p6=Personne("Nicolas",4000)
p7=Personne("Mathis",4000)
p8=Personne("Nasser",4000)

#Instanciation des dictionnaires : personne (composé d'objets 'Personne'), dict (composé par la suite d'objet 'Transaction')
personne={0:p1,1:p2,2:p3,3:p4,4:p5,5:p6,6:p7,7:p8}
dict={}
tab = []

#Ouverture du fichier CSV
with open('data.csv', newline='', encoding="utf-8-sig") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for rows in row:
            p = (str(rows).split(';'))
            tab.append(p)

#Boucle permettant de parcourir le fichier CSV, et de créer les transactions définies, en cherchant pour chaque transactions les personnes associées
for i in range(1, 7):
    for j in range(len(personne)):
            if(personne[j].nom == str(tab[i][0])):
                _P1=personne[j]
                personne[j].debit(float(tab[i][3]))
            if(personne[j].nom == str(tab[i][1])):
                _P2=personne[j]
                personne[j].reception(float(tab[i][3]))
    tempsT = tab[i][2]
    sommeS = tab[i][3]
    transaction=Transaction(_P1,_P2,str(tempsT),float(sommeS))
    dict[len(dict)+1]=transaction

@app.route("/", methods=['GET']) #appel dans un aurtre terminal avec : curl -X GET http://127.0.0.1:5000
def affichage(): #afficher toutes les transactions
    if request.method == 'GET':
        vueDict=""
        for i in range(len(dict)+1):
            if(i>0):
                vueDict+="Transaction de : "+str(dict[i].P1.nom)+" vers : "+str(dict[i].P2.nom)+" a l'heure "+str(dict[i].t)+" de la somme :"+str(dict[i].s)+"€"+"<br>"
        return vueDict

@app.route("/nom/<_p>", methods=['GET']) #appel dans un aurtre terminal avec : curl -X GET http://127.0.0.1:5000
def affichageNom(_p=None): #afficher toutes les transactions liées à une personne
    if request.method == 'GET':
        vueDict=""
        for i in range(len(dict)+1):
            if(i>0 and ((dict[i].P1.nom == str(_p)) or (dict[i].P2.nom == str(_p)))):
                vueDict+="Transaction de : "+str(dict[i].P1.nom)+" vers : "+str(dict[i].P2.nom)+" a l'heure "+str(dict[i].t)+" de la somme :"+str(dict[i].s)+"€"+"<br>"
        return vueDict

@app.route("/solde/<_p>", methods=['GET']) #appel dans un aurtre terminal avec : curl -X GET http://127.0.0.1:5000
def affichageSolde(_p=None): #afficher le solde d'une personne
    if request.method == 'GET':
        vuePersonne=""
        for i in range(len(personne)):
            if(personne[i].nom == str(_p)):
                vuePersonne+="Solde actuel de : "+str(personne[i].solde)+" € sur le compte à "+str(personne[i].nom)
        return vuePersonne

@app.route("/<_P1>/<_P2>/<_t>/<_s>", methods=['PUT']) #appel dans un aurtre terminal avec : curl -X GET http://127.0.0.1:5000
def ajoutTransaction(_P1=None,_P2=None,_t=None,_s=None): #E2 : méthode permettant d'enregistrer une transaction
    if request.method == 'PUT':
        for i in range(len(personne)):
            if(personne[i].nom == str(_P1)):
                _P1=personne[i]
                personne[i].debit(float(_s))
            if(personne[i].nom == str(_P2)):
                _P2=personne[i]
                personne[i].reception(float(_s))
        transaction=Transaction(_P1,_P2,str(_t),float(_s))
        dict[len(dict)+1]=transaction
        return str(dict)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build [OK]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run()