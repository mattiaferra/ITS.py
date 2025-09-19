from persona import Persona



class Dottore(Persona):
    def __init__(self, first_name, last_name,specialization : str , parcel : float):
        super().__init__(first_name, last_name)

        if isinstance(specialization,str):
            self.__specialization = specialization

        else:
            self.__specialization = None
            print("la specializzazione inserita non è di tipo string!")


        if isinstance(parcel,float):
            self.__parcel = parcel
        
        else:
            self.__parcel = None
            print( "La parcella inserita non è un float!")



    def setSpecialization(self,specialization):

         if isinstance(specialization,str):
            self.__specialization = specialization

         else:
            self.__specialization = None
            print("la specializzazione inserita non è di tipo string!")


    def setParcel(self,parcel):
          
         if isinstance(parcel,float):
            self.__parcel = parcel
        
         else:
            self.__parcel = None
            print( "La parcella inserita non è un float!")

    
    def getSpecialization(self):
        return self.__specialization

    def getParcel(self):
        return self.__parcel
    

    def isAValidDoctor(self):

        age = self.getAge()

        if self.__age <= 30:
            print(f"Doctor {self.__first_name} {self.__last_name} is not valid!")
        else:
            print(f"Doctor {self.__first_name} {self.__last_name} is valid!")



    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self.__specialization}")


