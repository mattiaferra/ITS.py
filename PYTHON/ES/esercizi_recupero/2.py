def dizionario_pos_neg(lista:list)-> dict:

    dizionario = {

        'positivi': [],
        'negativi': []
    }

    for item in lista:
        if item >= 0:
            dizionario['positivi'].append(item)
        
        else:
            dizionario['negativi'].append(item)

    return dizionario

numeri = [5, -2, 0, 8, -7, 3]
risultato = dizionario_pos_neg(numeri)
print(risultato)