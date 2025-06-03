class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of the employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("this is python language")

e1 = Employee("Priyal", 45)
e1.showDetails()

e2 = Programmer("Priya", 4)
e2.showDetails()
e2.showLanguage()
