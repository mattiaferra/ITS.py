'''#dal file persona.py importa la classe Persona
from persona import Persona

mf:Persona = Persona("Mattia" ,"Ferrandino" ,19)

print(mf)
print(mf.name,mf.lastname,mf.age)


#sfrutto la funzione nella displayData della classe Persona per visualizzare in output i dati relativi alla persona mf
mf.displayData()'''

#dal file persona2.py importa la classe Persona
from persona2 import Persona

mf:Persona = Persona()

mf.displayData()

print("------------")

#imposto il nome della persona mf
mf.setName("Mattia")
mf.displayData()

print("------------")

#imposto il cognome della persona mf

mf.setLastname("Ferrandino")
mf.displayData()

print("------------")

#imposto l'età della persona mf

mf.setAge(19)
mf.displayData()

print("------------")

mf.displayData()

print("------------")

print(mf.getName() ,mf.getLastname() ,mf.getAge())

