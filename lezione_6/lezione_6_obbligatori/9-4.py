class Ristorante:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):

        print(f"Nome Ristorante : {self.restaurant_name}")
        print(f"Tipo Cucina : {self.cuisine_type}")

    def open_restaurant(self):

        print(f"il ristorante {self.restaurant_name} è OPEN")

    
    def set_number_served(self,n):

        self.number_served = n
        print(f"incremento clienti serviti : {self.number_served}")



    def show_number_served(self):

        print(f"Numero clienti serviti: {self.number_served}")


    def increment_number_served(self,n):

        self.number_served += n


ristorante = Ristorante("Da Vittorio a Portuense","Italiana")



print(ristorante.restaurant_name)
print(ristorante.cuisine_type)

print("------------------")


ristorante.describe_restaurant()
ristorante.open_restaurant()


ristorante.show_number_served()       

print(f"Clienti serviti: {ristorante.number_served}")

ristorante.number_served = 25
print(f"Clienti serviti dopo modifica diretta: {ristorante.number_served}")


ristorante.set_number_served(50)
print(f"Clienti serviti dopo set_number_served(): {ristorante.number_served}")


ristorante.increment_number_served(30)
print(f"Clienti serviti incrementati : {ristorante.number_served}")