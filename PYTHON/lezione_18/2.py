import string


def validate_password(password):

    somma_carattere_maiusc = 0

    for i in password:

        if i.isupper():
            somma_carattere_maiusc += 1


    cont_cs = 0

    for i in password:

        if i in string.punctuation:
            carattere_speciale = i
            cont_cs += 1

    if len(password) < 20 or somma_carattere_maiusc < 3 or cont_cs < 4:
        raise ValueError("la password deve essere lunga almeno 20 caratteri e deve avere almeno 3 lettere maiuscole")
    

    else : 
        print("password corretta")
    
try :
    validate_password("Ciao!!")

except ValueError as e:
    print(e)

    




    
