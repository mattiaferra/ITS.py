n_tutor = 10
attesa = 0

while True:

    if n_tutor == 0 and attesa > 50 :

        break

    studente : str = input("inserire nome studente da assegnare al tutor : ")

    if n_tutor > 0 :
        
        n_tutor = n_tutor - 1
        
        print("tutor assegnato con successo ! ")

    else : 

        attesa = attesa + 1
        
        print("studente in attesa...")

    
    


        


