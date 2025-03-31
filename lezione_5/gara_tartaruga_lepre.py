import random

traguardo = 70 

posizione_tartaruga = 1 
posizione_lepre = 1

def movimento_tartaruga(posizione):

    mossa = random.randint(1,10)

    if 1 <= mossa <= 5 :    #passo veloce tartaruga 50%
        posizione += 3

    elif 6 <= mossa <= 7 :  #scivolata tartaruga 20%
        posizione -=6 

    else : 
        posizione += 1 #passo lento 30%

    return max(1,posizione)



def movimento_lepre(posizione):

    mossa = random.randint(1,10)

    if 1 <= mossa <= 2 : # 20% la lepre non si muove
        pass

    elif 3 <= mossa <= 4 : # 20% grande balzo lepre
        posizione += 9

    elif mossa == 5 :   # 10% grande scivolata lepre
        posizione -= 12

    elif 6 <= mossa <= 8 :  # 30% piccolo balzo lepre
        posizione += 1

    else :                  # 20 % scivola indietro 
        posizione -= 2

    return max(1,posizione)


def pista()

    
