class ContactManager:
    def __init__(self,contacts: dict[str, list[str]]):

        self.contacts = contacts



    def  create_contact(self, name: str, phone_numbers: list[str]):

        if name in self.contacts:
            return f"Errore: il contatto {name} esiste già."
        else:
            self.contacts[name] = phone_numbers 
            return self.contacts
            
        
                
    def add_phone_number(self, contact_name: str, phone_number: str):

        if contact_name not in self.contacts:
            return f"Errore: il contatto {contact_name} non esiste."
        
        elif phone_number in self.contacts[contact_name]:
            return f"Errore: il numero di telefono esiste già"
        
        else:
            self.contacts[contact_name].append(phone_number)
            return self.contacts[contact_name]        
        
        
    def remove_phone_number(self, contact_name: str, phone_number: str):

        if contact_name not in self.contacts:
             return f"Errore: il contatto {contact_name} non esiste."
        
        elif phone_number not in self.contacts[contact_name]:
            return f"Errore: il numero di telefono non è presente"
        
        else:
            self.contacts[contact_name].remove(phone_number)
            return {contact_name: self.contacts[contact_name]}
        


    def update_phone_number(self, contact_name: str, old_phone_number: str,new_phone_number: str):

        if contact_name not in self.contacts:
            return f"Errore: il contatto {contact_name} non esiste."
        
        elif old_phone_number not in self.contacts[contact_name]:
            return f"Errore: il numero di telefono non è presente"
        
        else:
            self.contacts[contact_name].remove(old_phone_number)
            self.contacts[contact_name].append(new_phone_number)
            return {contact_name: self.contacts[contact_name]}



    def list_phone_numbers(self, contact_name: str):

        if contact_name not in self.contacts:
           return f"Errore: il contatto {contact_name} non esiste."
        
        else:
            return self.contacts[contact_name]
        

    def search_contact_by_phone_number(self, phone_number: str): 
            
            for  key,value in self.contacts.items():

                if phone_number in value:
                    return key
                
                else:
                    return "Nessun contatto trovato con questo numero di telefono."
                    
            

            