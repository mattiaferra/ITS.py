

persone = [

{"nome": "edoardo" , "cognome":"levi" ,"eta": 19, "citta":"roma\n"},
{"nome": "edoardo" , "cognome":"valentini" ,"eta": 21, "citta":"roma"}

]



for persona in persone:

    for key,value in persona.items():
        print(f"{key}:{value}")