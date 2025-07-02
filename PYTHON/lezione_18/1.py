import math

def safe_sqrt(number):

    if number < 0:
        raise Exception("il numero non puo essere negativo")

    radice_quadrata = math.sqrt(number)
    
    print(radice_quadrata)

try:
    safe_sqrt(81)

except Exception as e :

    print(e)

