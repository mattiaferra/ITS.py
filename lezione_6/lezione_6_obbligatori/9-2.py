class Ristorante:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        print(f"Nome Ristorante : {self.restaurant_name}")
        print(f"Tipo Cucina : {self.cuisine_type}")

    def open_restaurant(self):

        print(f"il ristorante {self.restaurant_name} è OPEN")


ristorante = Ristorante("Da Vittorio a Portuense","Italiana")
ristorante2 = Ristorante("EQUO Hostaria","italiana")
ristorante3 = Ristorante("Macalè Osteria Moderna","italiana")
ristorante4 = Ristorante("Le Tre Zucche la bottega","italiana")

print(ristorante.restaurant_name)
print(ristorante.cuisine_type)

print("------------------")


ristorante.describe_restaurant()
ristorante.open_restaurant()


print("-----------------------")

ristorante2.describe_restaurant()
print("-----------------------")
ristorante3.describe_restaurant()
print("-----------------------")
ristorante4.describe_restaurant()
