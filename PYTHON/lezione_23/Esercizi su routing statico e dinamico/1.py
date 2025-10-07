'''
Route dinamica per profilo utente

Creare un percorso /user/<nome> che restituisca “Benvenuto, <nome>!”.

Testare con nomi diversi nell’URL.

'''





from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<p>Homepage</p>"


@app.route('/user/<string:nome>')
def Welcome(nome:str):
    return f"Benvenuto {nome}"




