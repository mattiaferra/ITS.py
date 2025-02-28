def make_car(produttore, modello, **opzioni):
    
    car_info = {"produttore": produttore , "modello": modello }
    

    for key, value in opzioni.items():
        car_info[key] = value
    
    return car_info

dizionario = make_car("subaru", "outback", color="blue", tow_package=True)

print(dizionario)
