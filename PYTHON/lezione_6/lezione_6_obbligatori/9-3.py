class User : 

    def __init__(self,first_name,last_name):

        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):

        print(f"Nome : {self.first_name}\nCognome : {self.last_name}")


    def greet_user(self):

        print(f"Ciao {self.first_name} {self.last_name}, è bello rivederti!")



utente = User("Mattia","Ferrandino")
utente2 = User("Edoardo","Levi")

utente.describe_user()
utente.greet_user()

print("--------------------------")

utente2.describe_user()
utente2.greet_user()




        