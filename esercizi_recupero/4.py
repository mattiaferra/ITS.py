def verifica_condizioni(x:bool,y:bool,z:bool):

    if x==True and (y== True or z == True):
        return "Azione Permessa"
    
    else:
        return "Azione Negata"
    


x = True
y = False
z = True

test = verifica_condizioni(x,y,z)
print(test)