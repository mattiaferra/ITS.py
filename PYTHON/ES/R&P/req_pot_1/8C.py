class Frazioni : 
    def __init__(self, l : list):
        
        self.l = l 
        self.i = [] # 'i' sta a significare  lista frazioni irriducibili

    def semplifica(self):


        divisore = 2

        for j in self.l:
                
                ris = j % divisore
                
                if ris != 0 : 
                    divisore += 1


                

                    