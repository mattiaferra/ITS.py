def converti_lista_di_tuple_in_dict(list:list[tuple])-> dict:

    dizionario = {}

    for chiave , valore in list:
        if chiave in dizionario:
            dizionario[chiave] += valore

        else:
            dizionario[chiave] = valore

    return dizionario

lista = [('a', 1), ('b', 2), ('a', 3), ('c', 5), ('b', 4)]
risultato = converti_lista_di_tuple_in_dict(lista)
print(risultato)


    
