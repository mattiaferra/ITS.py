animali_domestici = [

{"proprietario":"Mattia","animale":"Cane","razza":"labrador retriver\n"},
{"proprietario":"Giovanni","animale":"Gatto","razza":"Maine Coon"}


]


for animale in animali_domestici:
    for key,value in animale.items():
        print(f"{key}:{value}")