from math import prod

class Frazioni:

    def __init__(self, numeratore : int , denominatore : int):

        self._numeratore = numeratore
        self._denominatore = denominatore


    def set_numeratore(self, valore):

        if isinstance(valore, int):

            self._numeratore = valore
        else:

            self._numeratore = 13

    def set_denominatore(self, valore):

        if isinstance(valore, int) and valore != 0:

            self._denominatore = valore

        else:

            self._denominatore = 5

    def get_numeratore(self):

        return self._numeratore

    def get_denominatore(self):

        return self._denominatore

    def value(self):

        return round(self._numeratore/ self._denominatore, 3)


    def __str__(self):
        
        return f"numeratore : {self._numeratore} / denominatore : {self._denominatore}"
    




    def fattori_primi(self,numero):


            divisore = 2

            numeri_primi = []

            while numero > 1:
                
                if numero % divisore == 0 :

                    numeri_primi.append(divisore)
                    numero = numero // divisore

                    

                else : 
                    divisore += 1

            return numeri_primi

            


            

    def massimo_comune_divisore(self,n1,n2):
        
        n1 = Frazioni.fattori_primi(n1)
        n2 = Frazioni.fattori_primi(n2)


        fattori_comuni = []


        for i in n1:
            if i in n2:
                fattori_comuni.append(i)
                n2.remove(i)
            

        if fattori_comuni:
            return prod(fattori_comuni)
        else:
            return 1            
        
    
   
        
        


