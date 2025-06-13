def is_valid_ipv4(address: str) -> bool:

    indirizzi_diviso_in_parti : list[str] = address.split(".")

    if len(indirizzi_diviso_in_parti) != 4 :
        return False
    

    for i in indirizzi_diviso_in_parti: 

        if not i.isdigit():
            return False


        parte = int(i)
        
        if i < 0  or i > 255:
            return False
        
        
    
   
    



    






