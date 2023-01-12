from flask import Flask
from flask import request
import json

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

p1=Personne("jean",5000)
p2=Personne("louis",4000)

personne={0:p1,1:p2}
dict={}

@app.route("/", methods=['GET']) #appel dans un aurtre terminal avec : curl -X GET http://127.0.0.1:5000
def affichage():
    if request.method == 'GET':
        vueDict=""
        for i in range(len(dict)+1):
            if(i>0):
                vueDict+="Transaction de : "+str(dict[1].P1.nom)+" vers : "+str(dict[1].P2.nom)+" a l'heure "+str(dict[1].t)+" de la somme :"+str(dict[1].s)+"€"+" solde actuel : "+str(personne[0].solde)+" "+str(personne[1].solde)
        return vueDict

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

'''@app.route("/", methods=['GET','PUT']) #appel dans un aurtre terminal avec : curl -X GET http://127.0.0.1:5000
def login():
    if request.method == 'GET':
        vueDict=str(dict)
        return vueDict
    if request.method == 'PUT':
        dict[len(dict)]="Nass"
        return dict

@app.route("/<key>", methods=['DELETE']) #appel dans un aurtre terminal avec : curl -X DELETE http://127.0.0.1:5000/'un chiffre'
def loge(key=None):
    if request.method == 'DELETE':
        dict.pop(int(key))
        return dict

@app.route("/<key>/<nom>", methods=['POST']) #appel dans un aurtre terminal avec : curl -X POST http://127.0.0.1:5000/'un chiffre'/'un nom'
def loinPost(key=None, nom=None):
    if request.method == 'POST':
        dict[int(key)]=nom
        return dict'''


if __name__ == '__main__':
    app.run()