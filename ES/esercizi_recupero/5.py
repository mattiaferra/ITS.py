def moltiplica_num_iferiori_a_threshold (lista:list):

    threshold = 8
    ris = 1

    for numero in lista:
        if numero < threshold:
            ris*=numero
    return ris


li = [2,3,8]
test = moltiplica_num_iferiori_a_threshold(li)
print(test)

    