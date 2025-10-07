from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<p>Homepage. Vai su <a href='/about'>/about</a></p>"

@app.route('/about')
def about()-> str:

    return """

    <h1>Chi sono</h1>
    <p>Mi chiamo Mattia e questa è la mia prima app Flask.</p>
    <p>Sto imparando a creare applicazioni web in Python.</p>

    """


