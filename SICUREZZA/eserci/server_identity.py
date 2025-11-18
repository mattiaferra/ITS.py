# server_identity.py
from flask import Flask, request, redirect, make_response, session
from pathlib import Path
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Chiave segreta per sessioni

# Helper per servire file HTML
def serve_html(filename: str):
    path = Path("static") / filename
    if not path.exists():
        return make_response("<h1>404 - File non trovato</h1>", 404)
    html = path.read_text(encoding="utf-8")
    resp = make_response(html, 200)
    resp.headers["Content-Type"] = "text/html; charset=utf-8"
    return resp

# Funzione di login (autenticazione)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Esempio di controllo di autenticazione (puoi sostituirlo con il tuo metodo)
        if username == "admin" and password == "password123":
            session["user"] = username  # Salviamo il nome utente nella sessione
            return redirect("/area_protetta")
        else:
            return "<h1>Login fallito!</h1><a href='/login'>Torna al login</a>"

    return '''
        <form method="POST">
            <label for="username">Username:</label>
            <input type="text" name="username" required><br>
            <label for="password">Password:</label>
            <input type="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
    '''

# Pagina protetta
@app.route("/area_protetta")
def area_protetta():
    if "user" not in session:
        return redirect("/login")  # Se non è autenticato, rimanda al login
    
    # Se l'utente è autenticato, mostra la pagina protetta
    return '''
        <h1>Benvenuto nell'area protetta, {}</h1>
        <a href="/logout">Logout</a>
    '''.format(session["user"])

# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)  # Rimuove l'utente dalla sessione
    return redirect("/login")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
