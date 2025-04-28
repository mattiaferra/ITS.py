from lezione_8.eredarietà.persona import Persona
from lezione_8.eredarietà.studente import Studente


# creo un oggetto p della classe Persona

p: Persona = Persona("Mattia","Ferrandino",29)

# visualizzare le informazioni dell' oggetto p
print(p)

# creare un oggetto della classe Studente
studente1: Studente = Studente("Mario","Rossi",20,"0123456")


print(studente1)

#controllare se studente è istanza della classe Studente.
#isisntance(obj,Class) -> controlla se l'oggetto obj sia istanza della classe Class
#in caso affermativo -> TRUE
#in caso negativo -> FALSE


if isinstance(studente1,Studente):
    print("\nstudente1è istanza della classe Studente")


#controllo se studente1 sia anche istanza della classe Persona
if isinstance(studente1,Persona):
    print("\nstudente1 è un oggetto della classe Studente ma è anche un oggetto della classe Persona")


#controllo se l'oggetto p sia un istanza della classe Persona
if isinstance(p, Persona):
    print("\np è un oggetto della classe Persona")


#controllare se l'oggetto p sia anche un istanza della classe Studente
if isinstance(p,Studente):
    print("\np è un oggetto della classe Persona ma è anche un oggetto della classe Studente")

else:
    print("\np è un oggetto della classe Persona ma non è oggetto della classe Studente")


#controllare se una classe è sottoclasse di un'altra
# controllo che la classe Studente sia sottoclasse della classe Persona 
#inssubclass(Class1,Class2) -> controlla se la classe Class1 è la sottoclasse della classe Class2
#in caso affermativo -> True 
#in caso negativo -> False


if issubclass(Studente,Persona):
    print("\nLa classe Studente è sottoclasse della classe Persona")

