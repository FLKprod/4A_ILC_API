from flask import Flask
from flask import request

app = Flask(__name__)

class Transaction:
    def __init__(self,P1:str,P2:str,t:str,s:float):
        self.P1=P1
        self.P2=P2
        self.t=t
        self.s=s

t1=Transaction(5,5,5,5)
t2=Transaction(5,5,5,5)
dict={1:t1,2:t2}

@app.route("/", methods=['GET']) #appel dans un aurtre terminal avec : curl -X GET http://127.0.0.1:5000
def login():
    if request.method == 'GET':
        vueDict=""
        for i in range(len(dict)+1):
            if(i>0):
                vueDict+="Transaction de : "+str(dict[1].P1)+" vers : "+str(dict[1].P2)+" a l'heure "+str(dict[1].t)+" de la somme :"+str(dict[1].s)+"€"
        return vueDict
'''
@app.route("/<P1>/<P2>/<t>/<s>/", methods=['PUT']) #appel dans un aurtre terminal avec : curl -X GET http://127.0.0.1:5000
def ajoutTransaction(P1=None,P2=None,t=None,s=None): #E2 : méthode permettant d'enregistrer une transaction
    if request.method == 'PUT':
        transaction=Transaction(P1,P2,t,s)
        dict[len(dict)]=transaction
        return dict'''

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