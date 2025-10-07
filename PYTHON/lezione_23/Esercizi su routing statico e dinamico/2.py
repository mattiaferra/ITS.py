'''
Route con parametri numerici

Definire /square/<int:n> che ritorni il quadrato di n.

'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<p>Homepage</p>"


@app.route('/square/<int:n>')
def RadiceQuadrata(n:int):
    return  f"radice quadrata: {n**2}"