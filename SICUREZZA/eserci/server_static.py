from flask import Flask, make_response, redirect, request
from pathlib import Path
import requests

app = Flask(__name__)
STATIC_DIR = Path("static")

def serve_html(filename: str):
    path = STATIC_DIR / filename
    if not path.exists():
        return make_response("<h1>404 - File non trovato</h1>", 404)
    html = path.read_text(encoding="utf-8")
    resp = make_response(html, 200)
    resp.headers["Content-Type"] = "text/html; charset=utf-8"
    return resp

@app.route("/")
def home():
    return serve_html("home.html")

# pagina protetta
@app.route("/area_protetta")
def area_protetta():
    sessionid = request.cookies.get("sessionid")

    if not sessionid:
        return redirect("http://localhost:10000/login")

    r = requests.get(f"http://localhost:10000/validate/{sessionid}").json()

    if not r.get("valid"):
        return redirect("http://localhost:10000/login")

    return serve_html("area_protetta.html")

# pagine statiche generiche
@app.route("/html/<page>")
def html_page(page):
    if page == "riservata":
        pass
    else:
        return serve_html(f"{page}.html")

@app.route("/logout")
def logout():
    return redirect("http://localhost:10000/logout")

if __name__ == "__main__":
    STATIC_DIR.mkdir(exist_ok=True)
    app.run(host="0.0.0.0", port=9000, debug=True)
