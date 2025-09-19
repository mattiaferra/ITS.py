from dottore import Dottore
from paziente import Paziente

class Fattura : 

    def __init__(self,patient : list , doctor : Dottore):

         if doctor.isAValidDoctor():
              
            self.fatture = len(patient)
            self.salary = 0
            self.patient = patient
            self.doctor = doctor
        
         else:

            self.fatture = None
            self.salary = None
            self.patient = None
            self.doctor = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")


    def getSalary(self):

        parcella = self.doctor.getParcel()

        self.salary = parcella * len(self.patient)

        return self.salary
    

    def getFatture(self):

        self.fatture = len(self.patient)
        return self.fatture
        
    def addPatient(self, newPatient):
        if not isinstance(newPatient, Paziente):
            print("Errore: il paziente passato non è un oggetto Paziente!")
            return

        self.patient.append(newPatient)
        self.getFatture()
        self.getSalary()

        cognome_dott = self.doctor.getLastName()
        codice_paziente = newPatient.getIdCode()

        print(f"Alla lista del Dottor {cognome_dott} è stato aggiunto il paziente {codice_paziente}")
    

    def removePatient(self,idCode):

        self.patient.remove(idCode)
        self.getFatture()
        self.getSalary()

        print(f"Alla lista del Dottor {self.doctor.getLastName()} è stato rimosso il paziente {idCode}")