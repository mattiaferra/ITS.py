def prodotti (dizionario:dict)-> dict:

    nuovo_dict = {}

    for chiave , valore in dizionario.items():
        if valore <= 50:
            nuovo_valore = valore*1.10
            nuovo_dict[chiave]=nuovo_valore

    return nuovo_dict




dizi = {'mela': 4, 'pera': 8}
risultato = prodotti(dizi)
print(risultato)