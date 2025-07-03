def serie_nomi():

    lista_nomi = []
    nomi_inseriti = 0
    nome_maggiore = "" 

    while True:

        nome = input("inserisci un nome : ")

        if len(nome) >= 20 or nome == "" :
            print("nome non valido ")

        elif nome in lista_nomi :
            break

        else:
            lista_nomi.append(nome)
            nomi_inseriti +=1

        for i in lista_nomi:
            if len(i) > len(nome_maggiore):
                nome_maggiore = i

        
        if len(lista_nomi) == 4:
            break

                

                    


    print(f"hai inserito {nomi_inseriti} nomi  distinti")

    print(f"il più lungo è {nome_maggiore} con {len(nome_maggiore)} caratteri")
            

        


    
serie_nomi()