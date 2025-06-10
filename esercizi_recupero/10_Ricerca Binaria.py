def ricerca_binaria(num_cercato, lista):


     lista.sort()  # Assicurati che la lista sia ordinata

     sinistra =0
     destra = len(lista)-1


     while sinistra <= destra : # finchè sinistra è minore uguale a destra significa che devi ancora controllare altri elementi
          
          medio = (sinistra+destra)//2

          if num_cercato == lista[medio]: # se è nel punto medio l'hai trovato
               return True
          
          elif num_cercato < lista[medio]:
                                                    #se il numero cercato è piu piccolo del numero che sta nel punto medio essendo una lista ordinata in modo crescente
              destra = medio -1
          

          else:
               sinistra = medio + 1


     return False



test = ricerca_binaria(7,[1,7,8,9,10,12])
print(test)
               

       



    
           
           

        


