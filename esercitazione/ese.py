def blackjack_hand_total(cards: list[int]) -> int:
   
    somma_carte = sum(cards)
    
   
    while somma_carte > 21 and 11 in cards:
       
        cards[cards.index(11)] = 1
        
        somma_carte = sum(cards)
    
    
        return somma_carte



        