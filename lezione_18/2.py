def validate_password(password):

    somma_carattere_maiusc = 0

    for i in password:

        if i.isupper():
            somma_carattere_maiusc += 1


    if len(password) <= 20 or somma_carattere_maiusc <= 3:
        raise Exception("la password deve essere lunga almeno 20 caratteri e deve avere almeno 3 lettere maiuscole")
    

    
            
    
    
    