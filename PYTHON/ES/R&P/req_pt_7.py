def baricentro(v: list[int],i:int = 0):

    if i >= len(v) - 1:
        return None


    somma_sinistra = sum(v[0:i+1])
    somma_destra = sum(v[i+1:])


    if somma_sinistra == somma_destra:
        return i 
    

    return baricentro(v, i + 1)
    

def printResult(v: list[int]) -> None:
    i = baricentro(v)

    if i is not None:
        print(f"Esiste il baricentro del vettore v={v} ed è dato dall'indice i={i}!")

    else:
        print(f"Il baricentro del vettore v={v} non esiste!")




def baricentroOttimizzato(v: list[int]):

    somma_totale = 0

    for i in range(len(v)):

        somma_totale += v[i]

    return somma_totale





print(baricentroOttimizzato([1,2,3]))        



