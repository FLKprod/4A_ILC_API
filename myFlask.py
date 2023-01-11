from flask import Flask
from flask import request

app = Flask(__name__)
dict={ 0:"henru",1: "romain", 2:"quentin"}

@app.route("/", methods=['GET','PUT']) #appel dans un aurtre terminal avec : curl -X GET http://127.0.0.1:5000
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
        return dict


if __name__ == '__main__':
    app.run()