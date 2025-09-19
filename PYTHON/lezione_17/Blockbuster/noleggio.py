class Noleggio :
     
     def __init__(self, film_list):

        self.film_list = film_list  
        self.rented_film = {}

     def isAvaible(self,film): 
         
         if film in self.film_list:
             print(f"Il film scelto è disponibile: {film}!")
             return True
             
         else:
             print(f"Il film scelto NON è disponibile: {film}!")


             
     