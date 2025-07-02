from lezione_8.eredarietà.persona import Persona
from lezione_8.eredarietà.alieno import Alieno

# creare un oggetto p della classe Persona
p: Persona = Persona("Mattia","Ferrandino",19)


# visualizzare informazioni oggetto p
print(p)


# creare un oggetto et della classe Alieno
et: Alieno = Alieno("Andromeda")


# visualizzare informazioni oggetto et
print(et)


# l'oggetto p invochi il metodo speak()
p.speak()


# invochiamo metodo speak dall'oggetto et
et.speak()

