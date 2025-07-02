class Person :
 


    def __init__(self, name, age):

        self.name = name
        self.age = age



alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
giovanni = Person("Giovanni C.", 48)
alfredo = Person("Alfredo D." , 89)
federica = Person("Federica D.", 17) 

persone = [alice,bob,giovanni,alfredo,federica]




if alice.age > bob.age : 

    print("alice è piu grande di bob")

else:

    print("bob è piu grande di alice ")


youngest_person = persone[0]


for i in persone:
    
    if i.age < youngest_person.age:
         
         youngest_person = i


print(f"la persona piu giovane è {youngest_person.name}")



