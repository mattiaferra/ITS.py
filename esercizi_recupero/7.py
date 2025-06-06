class ContactManager:
    def __init__(self):
        self.contacts: dict[str, list[str]] = {}

    def create_contact(self,name: str, phone_numbers: list[str]):
        
        if name not in self.contacts:
            self.contacts[name] = phone_numbers
            return {name: self.contacts[name]}
        
        else:
            return "errore il contatto esiste già"
        

    def  add_phone_number(self,contact_name: str, phone_number: str):

        if contact_name not in self.contacts :
            return "errore il contatto non esiste"
        
        elif phone_number in self.contacts[contact_name]:
            return "il numero di telefono esiste già"
        else:
            self.contacts[contact_name].append(phone_number)
            return {contact_name: self.contacts[contact_name]}
        
    def remove_phone_number(self,contact_name: str, phone_number: str):

        if contact_name not in self.contacts:
            return "errore il contatto non esiste"
        
        elif phone_number not in self.contacts[contact_name]:
            return "errore il numero di telefono non è presente"
        
        else:
            self.contacts[contact_name].remove(phone_number)
            return {contact_name: self.contacts[contact_name]}
        

    
    def update_phone_number(self,contact_name: str, old_phone_number: str,new_phone_number: str):

    

        if contact_name not in self.contacts:
            return "errore il contatto non esiste"
        
        elif old_phone_number not in self.contacts[contact_name]:
            return "errore il numero di telefono non è presente"
        
        else:
               
        