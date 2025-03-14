class Student : 


    def __init__(self, name : str , studyProgram : str):

        self.name = name
        self.studyProgram = studyProgram

    def printInfo(self):

        print(f"Name: {self.name}, Study Program: {self.studyProgram}")


student1 = Student("Mattia", "Informatica")
student2 = Student("Vicino Sinistra", "Matematica")
student3 = Student("Vicino Destra", "Fisica")

student1.printInfo()
student2.printInfo()
student3.printInfo()