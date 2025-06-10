from string import ascii_lowercase

lista_lettere_alfabeto = list(ascii_lowercase)
lettere_cifr = []




def caesar_cypher_encrypt(s, key):



    s : str = s                    # s = ciao
    key : int = key                 #key = 2

    for i in s:
        if i in lista_lettere_alfabeto:

            indice = lista_lettere_alfabeto.index(i)
            indice_nuovo = (indice + key) % 26
            lettere_cifr .append(lista_lettere_alfabeto[indice_nuovo])
        else:
            lettere_cifr.append(i)


        


#da completare


