stringa = input("inserire la frase da cifrare : ")
key = int(input("Inserire la chiave di decriptazione (numero): "))

lista_caratteri_cifrati_in_numeri = []

for carattere_singolo in stringa : 

    numero_carattere_singolo = ord(carattere_singolo)

    carattere_cifrato = numero_carattere_singolo ^ key

    lista_caratteri_cifrati_in_numeri.append(carattere_cifrato)


print(lista_caratteri_cifrati_in_numeri)