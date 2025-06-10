from string import ascii_lowercase
from string import ascii_uppercase

lista_minuscole = list(ascii_lowercase)
lista_maiuscole = list(ascii_uppercase)
lettere_cifr = []
lettere_decifr = []




def caesar_cypher_encrypt(s, key):

    i = 0
    s = s #frase da cifrare
    key = key #chiave



    while i < len(s):

        carattere = s[i]

        if carattere in lista_minuscole:

            posizione_carattere = (lista_minuscole.index(carattere) + key) % 26
            lettere_cifr.append(lista_minuscole[posizione_carattere])


        elif carattere in lista_maiuscole:

             posizione_carattere = (lista_maiuscole.index(carattere) + key) % 26
             lettere_cifr.append(lista_maiuscole[posizione_carattere])    

        
        else:
            lettere_cifr.append(carattere)

        i+=1
    return ''.join(lettere_cifr)
    


def caesar_cypher_decrypt(s, key):
    i = 0
    s = s #frase da cifrare
    key = key #chiave



    while i < len(s):

        carattere = s[i]

        if carattere in lista_minuscole:

            posizione_carattere = (lista_minuscole.index(carattere) - key) % 26
            lettere_decifr.append(lista_minuscole[posizione_carattere])


        elif carattere in lista_maiuscole:

             posizione_carattere = (lista_maiuscole.index(carattere) - key) % 26
             lettere_decifr.append(lista_maiuscole[posizione_carattere])    

        
        else:
            lettere_decifr.append(carattere)

        i+=1
    return ''.join(lettere_decifr)
    





              
              
lettere_chiave = caesar_cypher_encrypt("ciao",2)
lettere_chiave2 = caesar_cypher_decrypt(lettere_chiave,2)
print(lettere_chiave)
print(lettere_chiave2)
        








