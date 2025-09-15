from math import prod

def fattori_primi(numero):


        divisore = 2

        numeri_primi1 = []

        while numero > 1:
            
            if numero % divisore == 0 :

                numeri_primi1.append(divisore)
                numero = numero // divisore

                

            else : 
                divisore += 1

        return numeri_primi1

        


        

def massimo_comune_divisore(n1,n2):
     
     n1 = fattori_primi(n1)
     n2 = fattori_primi(n2)


     fattori_comuni = []


     for i in n1:
          if i in n2:
               fattori_comuni.append(i)
               n2.remove(i)
         

     if fattori_comuni:
          return prod(fattori_comuni)
     else:
          return 1
     
   
print(massimo_comune_divisore(12, 18))  # Output: 6
print(massimo_comune_divisore(4, 5))   # output 1
     
    
          
        


     
     

    
