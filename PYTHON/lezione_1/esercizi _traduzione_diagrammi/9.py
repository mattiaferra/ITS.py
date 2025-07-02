max_nome = 1 
max_vendite = -10000000000000
min_nome = 1
min_vendite = +10000000000000

CONT = 0
for CONT in range(3):
    new_nome = input("Inserisci il nome: ")
    new_vendite = int(input("Inserisci la vendita: "))
    if new_vendite > max_vendite:
        max_nome = new_nome
        max_vendite = new_vendite
    else:
        if new_vendite < min_vendite:
            min_nome = new_nome
            min_vendite = new_vendite
    CONT += 1

print(max_nome, max_vendite)
print(min_nome, min_vendite)
