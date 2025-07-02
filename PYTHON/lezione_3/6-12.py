

#per questo esercizio ho ripreso il 6-11 e ho aggiunto al dizionario "piatto tipico" e "attrazioni principali"

citta = {
    "Roma": {
        "paese": "Italia",
        "popolazione": "2.8 milioni",
        "fatto": "È conosciuta come la Città Eterna.",
        "attrazioni": ["Colosseo", "Fontana di Trevi", "Piazza San Pietro"],
        "piatto_tipico": "Carbonara"
    },
    "New York": {
        "paese": "Stati Uniti",
        "popolazione": "8.4 milioni",
        "fatto": "Ha la Statua della Libertà e Times Square.",
        "attrazioni": ["Statua della Libertà", "Central Park", "Times Square"],
        "piatto_tipico": "Pizza New York Style"
    },
    "Tokyo": {
        "paese": "Giappone",
        "popolazione": "14 milioni",
        "fatto": "È una delle città più tecnologicamente avanzate al mondo.",
        "attrazioni": ["Shibuya", "Tempio Senso-ji", "Torre di Tokyo"],
        "piatto_tipico": "Sushi"
    }
}

for citta_nome, dettagli in citta.items():
    print(f"\nCittà: {citta_nome}")
    print(f"Paese: {dettagli['paese']}")
    print(f"Popolazione: {dettagli['popolazione']}")
    print(f"Fatto interessante: {dettagli['fatto']}")
    print(f"Attrazioni principali: {', '.join(dettagli['attrazioni'])}")
    print(f"Piatto tipico: {dettagli['piatto_tipico']}")
