città = {
    "roma": {
        "paese": "Italia",
        "popolazione": "2.8 milioni",
        "fatto": "Roma è conosciuta come la 'Città Eterna'."
    },
    "new york": {
        "paese": "Stati Uniti",
        "popolazione": "8.3 milioni",
        "fatto": "New York è soprannominata 'La Grande Mela'."
    },
    "tokyo": {
        "paese": "Giappone",
        "popolazione": "14 milioni",
        "fatto": "Tokyo è la città più popolosa del mondo."
    }
}


for citta_nome, citta_info in città.items():
    print(f"Info su {citta_nome.capitalize()}:")
    print(f"Paese: {citta_info['paese']}")
    print(f"Popolazione: {citta_info['popolazione']}")
    print(f"Fatto: {citta_info['fatto']}")
    print("----------------------------------------")

